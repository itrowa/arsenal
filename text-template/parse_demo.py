# just a parser demo for demostrating templite class.

import re

e1 = "abc.edf.ghi"
print(e1.split("."))



buffered = ["haha", "hehe"]
if len(buffered) == 1:
    print("append_result(%s)" % buffered[0])
elif len(buffered) > 1: 
    print("extend_result([%s])" % ", ".join(buffered))

# re对templite的解析
text = '''
    <h1>Hello {{name|upper}}! </h1>
    {% for topic in topics %}
        <p>You are interested in {{topic}}.</p>
        {% if name = "huang" %}
            <p>This apperas!! </p>
    {% endfor %}
    '''
ops_stack = []
code = ""

tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)
for t in tokens:
    print(t)

print("----------------------")
for token in tokens:
    # 对expression的处理
    if token.startswith('{{'):
        expr = token[2:-2].strip()
        print("to_str(%s)" % expr)

    elif token.startswith('{%'):
        # Control Structrures.
        words = token[2:-2].strip().split()

        if words[0] == 'if':
            # if statement
            if len(words) != 2:
                # self._syntax_error("Don't understand if", token)    # helper?
                print("Don't understand if, ", token)

            ops_stack.append('if')
            print ("if %s:" % words[1])

# 关于expr_code()
def _expr_code(self, expr):
    """ generate a Python exp for 'expr'. 
    """
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

def _variable(self, name, vars_set):
    """ 往vars_set列表中添加一个name. 同时确保name是合法有效的."""
    if not re.match(r"[_a-zA-Z][_a-zA-Z0-9]*$", name):
        self._syntax_error("Not a valid name", name)
    vars_set.add(name)

s = """
    name|upper|lower
    """

