from CodeBuilder import *
import re

class Templite:

    def __init__(self, text, *contexts):
        """ 通过给定的text, 创建一个Templite对象.
            text: template文本.
            context是字典. 用于filters和global values. contexts 
            是打包成tuple的 (*operator)!
        """

        self.context = {}
        for context in contexts:
            self.context.update(context)
            # 把外来的context的 key/value对添加到self.context中.
            # 需要这一步的原因是, 许多template text中的name并没有定义.

        # 创建两个集合
        self.all_vars = set()
        # 所有模板中的变量都会记录在all_vars中.
        self.loop_vars = set()
        # 所有模板中的loop中的变量都会记录在loop_vars中.
        # eg: for s in seq: 这句中, s会被存储进去, 但是seq不会.

        #code: 通过text生成的python函数源代码.
        code = CodeBuilder()

        code.add_line("def render_function(context, do_dots):")
        code.indent()

        vars_code = code.add_section()
        # 一个区域 以后可以在函数中添加更多的信息..
        # 后面的程序在继续parse整个template text时会发现更多的变量名, 
        # 到时候变量名的赋值会添加到此处.

        code.add_line("result = []")
        code.add_line("append_result = result.append")
        code.add_line("extend_result = result.extend")
        code.add_line("to_str = str")
        # 以上都是生成的python函数的固定部分.

        # The buffered list holds strings that are yet to be written to our function source code. 
        # As our template compilation proceeds, we'll append strings to buffered, and flush them 
        # to the function source when we reach control flow points, like if statements, or the 
        # beginning or ends of loops.
        buffered = []

        def flush_output():
            """ Force `buffered` to the code builder.
                We'd like to combine repeated append calls into one extend call.
            """
            # 这是一个闭包函数, 引用了code和buffered.
            if len(buffered) == 1:
                code.add_line("append_result(%s)" % buffered[0])
            elif len(buffered) > 1:
                code.add_line("extend_result([%s])" % ", ".join(buffered))
            del buffered[:]         # 删除buffered中的元素, 但不删除它本身.

        # ####################################################################
        # text 的解析
        # ####################################################################

        # 1. 词法分析:
        # 把模板源文件看成是str, 用正则表达式去parse成一系列token
        ops_stack = []
        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)
        # 把text解析成tokens. tokens是一系列str的list.

        # 2. 句法分析和翻译
        # case analysis
        for token in tokens:
            if token.startswith('{#'):
                # it's just a comment. ignore it.
                continue

            elif token.startswith('{{'):
                # 表达式. 需要转化为python表达式
                # eg: {{ variable }}

                expr = self._expr_code(token[2:-2].strip())
                # 掐头去尾, 删掉空格, 换行, 制表符
                buffered.append("to_str(%s)" % expr)   # 转译为python代码

            elif token.startswith('{%'):
                # Control Structrures.
                # eg: {% for i in items %}
                flush_output()
                words = token[2:-2].strip().split()

                if words[0] == 'if':
                    # if statement
                    if len(words) != 2:
                        self._syntax_error("Don't understand if", token)   
                    ops_stack.append('if')
                    code.add_line("if %s:" % self._expr_code(words[1]))
                    code.indent()

                elif words[0] == 'for':
                    # loop statement
                    if len(words) != 4 or words[2] != 'in':
                        self._syntax_error("Don't understand for", token)
                    ops_stack.append('for')
                    self._variable(words[1], self.loop_vars) #?
                    code.add_line(
                        "for c_%s in %s:" % (
                            words[1],
                            self._expr_code(words[3])
                        )
                    )
                    code.indent()

                # end tag, 例如{%endfor%} {%endif%}
                elif words[0].startswith('end'):
                    if len(words) != 1:
                        self._syntax_error("Don't understand end", token)
                    end_what = words[0][3:]
                    if not ops_stack:
                        self._synatax_error("Too many ends", token)
                    start_what = ops_stack.pop()
                    if start_what != end_what:
                        self._syntax_error("Mismatched end tag", end_what)
                    code.dedent()

                else:
                    self._syntax_error("Don't understand tag", words[0])

            else:
                # Literal content.
                if token:
                    # repr()是个好东西, 它能自动添加反斜杠, 还能处理其他转义字符.
                    buffered.append(repr(token))

        # token遍历结束..

        # if there are still op in stack:
        if ops_stack:
            self._syntax_error("Unmatched action tag", ops_stack[-1])

        flush_output()

        # 把除了loop 部分变量以外的所有变量拿出来, 将这些变量的初始化定义添加到生成的python code的开头.:
        for var_name in self.all_vars - self.loop_vars:
            vars_code.add_line("c_%s = context[%r]" % (var_name, var_name)) 

        code.add_line("return ''.join(result)")
        code.dedent()

        self._render_function = code.get_globals()['render_function']

    def _expr_code(self, expr):
        """ generate a Python exp for 'expr'. """
        # 具体做法是, 把a|b|c 或者item.property 这样的表达式翻译为对应的python表达式,
        # 另外每个name也要变成python code中带c_前缀的局部变量.
        if "|" in expr:
            pipes = expr.split("|")
            code = self._expr_code(pipes[0])
            for func in pipes[1:]:
                self._variable(func, self.all_vars)
                code = "c_%s(%s)" % (func, code)
        elif "." in expr:
            dots = expr.split(".")
            code = self._expr_code(dots[0])
            args = ", ".join(repr(d) for d in dots[1:])
            code = "do_dots(%s, %s)" % (code, args)
        else: 
            # the case that there was no pipe or dot in the 
            # input expression. In that case, it's just a name. 
            # We record it in all_vars, and access the variable using its prefixed Python name:
            self._variable(expr, self.all_vars)
            code = "c_%s" % expr
        return code

    def _syntax_error(self, msg, thing):
        """ Raise a syntax error using 'msg', and showing 'thing'. """
        raise TempliteSyntaxError("%s: %r" % (msg, thing))

    def _variable(self, name, vars_set):
        """ 往vars列表中添加一个name. 同时确保name是合法有效的."""
        if not re.match(r"[_a-zA-Z][_a-zA-Z0-9]*$", name):
            self._syntax_error("Not a valid name", name)
        vars_set.add(name)

    def render(self, context=None):
        """ Render this template by applying it to `context`.
            `context` is a dictionary of values to use in this rendering.
        """
        # Make the complete context we'll use.
        render_context = dict(self.context)
        if context:
            render_context.update(context)
        return self._render_function(render_context, self._do_dots)

    def _do_dots(self, value, *dots):
        """ Eval dotted exps at runtime.
        """
        for dot in dots:
            try:
                value = getattr(value, dot)
            except AttributeError:
                value = value[dot]
            if callable(value):
                value = value()
        return value


# Make a Templite obj.
# 初始化的时候, 把template的内容和 context放进去就好.
templite = Templite('''
    <html>
    <h1>Hello {{name|upper}}! </h1>
    {% for topic in topics %}
        <p>You are interested in {{topic}}.</p>
    {% endfor %}
    </html>
    ''',
    {'upper': str.upper},
    )

# 渲染的时候, 再把name和topics的具体内容也传入. 这里name 和 topics变量都是在模板文件以外指定的.
text = templite.render({
    'name': "Ned",
    'topics': ['Python', 'Geometry', 'Juggling'],
    })

# 生成HTML文件
f = open("output.html", "w")
f.write(text)
f.close()