def eval_exp(tree, env):
    exptype = tree[0]
    if exptype == "call":
        fname = tree[1]
        fargs = tree[2]
        fvalue = env_lookup(fname, env)

        if fname == "write":
            argval = eval_exp_fargs[0], env)
            output_sofar = env_lookup("javascript output", env)
            env_update("javascript output", output_sofar + str(argval), env)
            return None