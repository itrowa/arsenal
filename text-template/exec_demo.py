# test

python_source = """
SEVENTEEN = 17

def three():
    return 3
"""
global_namespace = {}

exec(python_source, global_namespace)