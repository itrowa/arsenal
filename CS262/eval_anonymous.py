def eval_exp(tree, env):
    exptype = tree[0]
    # eg: function(x, y) {return x + y;}
    if exptype == "function":
        # ("function", ["x", "y"], [("return", ("binop", ...)])
        fparams = tree[1]
        fbody = tree[2]
        return ("function", fparams, fbody, env)