# CodeBuilder只是在字面意义上地一行一行堆砌"代码", 而完全不关心代码里面的实际内容是什么.

class CodeBuilder(object):
    """ 仅仅是一个类, 让我们更方便创建python代码, 尤其是按行进行处理; 以及
        处理缩进.
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
        """ 一个递归的自己, 被添加到code中
        """
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
        # 执行完毕后, global_namespace['SEVENTEEN'] = 17, 
        #            global_namespace['three'] is an actual function named three.

        return global_namespace

    def __str__(self):
        return "".join(str(c) for c in self.code)

# test
if __name__ == "__main__":

    python_source = """
    SEVENTEEN = 17

    def three():
        return 3
    """
    global_namespace = {}

    exec(python_source, global_namespace)