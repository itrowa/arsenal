def scheme_eval(expr, env):
	"""Eval scheme expression expr inn environment env."""
	if scheme_symbolp(expr):
		return env[expr]
	elif scheme_atomp(expr):
		return expr
	first, rest = expr.first, expr.second
	if first == "lambda":
		return do_lambda_form(rest, env)
	elif first == "define":
		# deine special form:
		do_define_form(rest, env)
		return None
	else:
		procedure = scheme_eval(first, env)
		args = rest.map(lambda operand: scheme_eval(operand, env))
		return scheme_apply(procedure, args, env)