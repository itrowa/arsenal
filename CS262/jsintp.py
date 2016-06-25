# javascript interpreter

# environment
global_env = []

global_frame = {
    "javascript output: ": "",
    "x": 3,
    "y": 4,
    "z": 5,
}

f1 = {
    "x": 100,
    "y": 101,
    "z": 102,
}

global_env.append(global_frame)
global_env.append(f1)
print (global_env)

def env_lookup(name, env):
    """ 查找变量的值.
    """
    for frame in env:
        if name in frame:
            return frame[name]
    return None

def env_update(name, value, env):
    """ 若变量已存在, 则更新其值
        若变量不存在, 添加一个变量绑定到global frame.
    """
    for frame in env:
        if name in frame:
            frame[name] = value
            return
    env[0][name] = value
    # @todo: 如果不能正确赋值, 应该返回什么信息?



# 在我们的javascript实现中, js的解释结果是一系列字符串, 
# 储存在env的第一帧的"javascript output: "键下.
def interpret(ast):
    global_env = (None, {"javascript output: ": ""})

    for elt in ast:
        eval_elt(elt, global_env)
    return (global_env[1])["javascript output"]

def eval_elt(elt, env):
    # help def
    elttype = elt[0]
    eltcontent = elt[1]

    if elttype == 'function':           # function definition?
        pass
    elif tlttype == 'stmt':             # statement
        eval_stmt(eltcontent, env)      # stmt@?
    else:
        print ("ERROR - Unknown element " + elt) 

def eval_stmts(stmts, env):
    for stmt in stmts:
        eval_stmt(stmt, env)

def eval_stmt(stmt, env):
    stype = stmt[0]

    # if-then
    # if (<exp>) {...}
    if stype == "if-then":
        predicate = stmt[1]
        consequent = stmt[2] 
        if eval_exp(predicate ,env):
            eval_stmts(consequent, env) 

    # while (<exp>) {}
    elif stype == "while":
        predicate = stmt[1]
        consequent = stmt[2]
        if eval_exp(predicate, env):
            eval_stmts(consequent, env)

    # if (exp) {<stmts>} else {<stmts>}
    elif stype == "if-then-else":
        predicate = stmt[1]           
        consequent = stmt[2]
        alternative = stmt[3]
        if eval_exp(predicate, env):
            eval_stmts(consequent, env)
        else:
            eval_stmts(consequent, env)

    # var 变量声明. 
    elif stype == "var":
        varname = stmt[1]
        rhs = stmt[2]
        #@? 求值rhs的值, 然后在环境中更新
        pass

    # x = <exp>
    elif stype == "assign":
        varname = stmt[1]
        rhs = stmt[2]
        # 在环境中更新varname的值. @?@
        pass

    elif stype == "return":
        returned = eval_exp(stmt[1], env)
        return returned   # 难道不能这样搞吗

    elif stype == "exp":
        eval_exp(stmt[1], env)

    else:
        print( "ERROR: unknown statement type", stype)

# 求值表达式.
def eval_exp(exp, env):
    etype = exp[0]

    if etype == "identifier":
        varname = exp[1]
        # @todo: 在环境中查找变量.
        value = env_lookup(varname, env)
        if value == None:
            print("ERROR: unbound variable: " + varname)
        else: 
            return value

    elif etype == "number":
        return float(exp[1])

    elif etype == "string":
        return exp[1]

    elif etype == "true":
        return True

    elif etype == "false":
        return False

    elif etype == "not":
        return not(eval_exp(exp[1], env))

    # @?@ 又是closure?
    elif etype == "function":
        fparams = exp[1]
        fbody = exp[2]
        return ("closure", fparams, fbody, env)

    # 二元运算
    elif etype == "binop":
        a = eval_exp(exp[1],env)
        op = exp[2]
        b = eval_exp(exp[3],env)
        if op == "+":
                return a+b
        elif op == "-":
                return a-b
        elif op == "/":
                return a/b
        elif op == "*":
                return a*b
        elif op == "%":
                return a%b
        elif op == "==":
                return a==b
        elif op == "<=":
                return a<=b
        elif op == "<":
                return a<b
        elif op == ">=":
                return a>=b
        elif op == ">":
                return a>b
        elif op == "&&":
                return a and b
        elif op == "||":
                return a or b
        else:
                print ("ERROR: unknown binary operator ", op)
                exit(1)

    # call expression
    elif etype == "call":
        fname == exp[1]
        args = exp[2]

        fvalue = env_lookup(fname, env)

        if fname == "write":
            pass

        # fname在环境中应该绑定到一个闭包上.
        # 如果是闭包, 则求值args,  然后在扩展了的环境中将参数值求值function的body.
        else:
            print ("ERROR: call to non-function ", fname)

    else:
        print ("ERROR: unknown expression type ", etype)











