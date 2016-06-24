import ply.lex as lex
import htmltokens             # 导入html 的lex定义

data = """
<html>
    <head>
        <title> this is a title.</title>
    </head>
    <body class="wrapper">
        <p>This is a <i>sample</i> <a href="#" title="haha">text</a>.</p>
        <script type="text/javascript">
            var x = 32; /* start comment */
            // this is a comment
            if (x > 5) {
                return x;
            }
        </script>
    </body>
</html>
"""

# 初始化一个lexer
lexer = lex.lex(module=htmltokens)

# 输入一些字符串.
lexer.input(data)

# lex.token() 返回下一个LexToken类型的token实例. 如果遇到字符串末尾则返回None
while 1:
    tok = lex.token()
    if not tok: break
    print (tok)