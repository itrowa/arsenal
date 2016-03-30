# CodeBuilder只是在字面意义上地一行一行堆砌"代码", 而完全不关心代码里面的实际内容是什么.

class CodeBuilder(object):
    """ Build source code conveniently.
    """
    INDENT_STEP = 4

    def __init__(self, indent=0):
        self.code = []
        self.indent_level = indent

    def add_line(self, line):
        """ 给code新添加一行, 开始是一些空格, 然后是line的内容.
        """
        self.code.extend([" " * self.indent_level, line, "\n"])

    def indent(self):
        """ Increase the current indent for following lines.
        """
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """ Decrease the current indent for following lines.
        """
        self.indent_level -= self.INDENT_STEP

    def add_section(self):
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def get_globals(self):
        """ Exec the code and return a dict of globals it defines.

        """
        assert self.indent_level == 0
        python_source = str(self)
        global_namespace = {}

        exec(python_source, global_namespace)
        # 注意, 一开始global_namespace是空的, 但是这句函数执行完以后, 它就会存储着刚才运行的
        # python代码中定义的name对应的value.
        # EG:
        # ------------
        # python_source = """\
        # SEVENTEEN = 17

        # def three():
        #     return 3
        # """
        # global_namespace = {}
        # exec(python_source, global_namespace)
        # ------------
        # then global_namespace['SEVENTEEN'] is 17, and global_namespace['three'] is an actual function named three.

        return global_namespace

    def __str__(self):
        return "".join(str(c) for c in self.code)


# usage:
code = CodeBuilder()

code.add_line("def render_function(context, do_dots):")
code.indent()

vars_code = code.add_section()
# 一个区域 以后可以在函数中添加更多的信息..

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
        这是一个闭包函数, 引用了code和buffered.
    """
    if len(buffered) == 1:
        code.add_line("append_result(%s)" % buffered[0])
    elif len(buffered) > 1:
        code.add_line("extend_result([%s])" % ", ".join(buffered))
    del buffered[:]


