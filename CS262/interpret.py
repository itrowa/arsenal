def interpret(trees):
    for tree in trees:
        treetype = tree[0]  # 取得tree的类型
        if treetype == "word-element":
            graphics.word(node[1])
        elif treetype == "javascript-element":
            jstext = tree[1]
            jslexer = lex.lex(module=jstokens) # 调用lex建立lexer
            jsparser = yacc.yacc(module=jsgrammar)

            # 调用jsparser的parse方法, 得到得到jstext的AST
            jstree = jsparser.parse(jstext, lexer=jslexer)

            # 对AST的解释结果
            result = jsinterp.interpret(jstree)
            graphics.word(result)

