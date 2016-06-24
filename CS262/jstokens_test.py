import ply.lex as lex
import jstokens             # 导入js 的lex定义

data = """
var x = 32; /* start comment */
// this is a comment
if (x > 5) {
    return x;
}
"""

# 初始化一个lexer
lexer = lex.lex(module=jstokens)

# 输入一些字符串.
lexer.input(data)

# lex.token() 返回下一个LexToken类型的token实例. 如果遇到字符串末尾则返回None
while 1:
    tok = lex.token()
    if not tok: break
    print (tok)