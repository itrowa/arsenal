# Earley parser for construct AST for a list of tokens and a Context-Free Grmmar set.

def addtochart(theset, index, elt):
    if not(elt in theset[index]):
        theset[index] = [elt] + theset[index]
        return True
    else:
        return False

def closure (grammar, i, x, ab, cd, j):
    next_states = [(rule[0], [], rule[1], i) for rule in grammar if cd != [] and rule[0] == cd[0]]
    return next_states


def shift (tokens, i, x, ab, cd, j):
    if cd != [] and tokens[i] == cd[0]:
        return (x, ab+[cd[0]], cd[1:], j)
    else:
        return None

def reductions(chart, i, x, ab, cd, j):
    return [ (jstate[0], jstate[1] + [x], (jstate[2])[1:], jstate[3])
            for jstate in chart[j]
            if cd == [] and jstate[2] != [] and (jstate[2])[0] == x]

grammar = [
    ("S", ["P"]),
    ("P", ["(", "P", ")"]),
    ("P", []),
]

tokens = ["(", "(", ")", ")"]

def parse(tokens, grammar):
    tokens = tokens + ["end_of_input_marker"] # arbitrarily add end marker.
    start_rule = grammar[0]

    # init the chart
    chart = {} 
    for i in range(len(tokens) + 1):
        chart[i] = []

    start_state = (start_rule[0], [], start_rule[1], 0)
    chart[0] = [start_state]

    # use 3 rules for parsing!
    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart[i]:
                # State === x -> a b . c d, j
                x = state[0]
                ab = state[1]
                cd = state[2]
                j = state[3]

            # apply rule 1
            next_states = closure(grammar, i, x, ab, cd, j)
            for next_state in next_states:
                changes = addtochart(chart, i, next_state) or changes

            # apply rule 2
            next_state = shift(tokens, i, x, ab, cd, j)
            if next_state != None:
                changes = addtochart(chart, i+1, next_state) or changes

            # apply rule 3
            next_states = reductions(chart, i, x, ab, cd, j)
            for next_state in next_states:
                changes = addtochart(chart, i, next_state) or changes

            if not changes: # if no changes!
                break

    # print out the chart
    for i in range(len(tokens)):
        print ("== chart" + str(i))
        for state in chart[i]:
            x = state[0]
            ab = state[1]
            cd = state[2]
            j = state[3]

            print ("    " + x + " ->", end="")
            for sym in ab:
                print (" " + sym, end="")
            print( " .", end="")
            for sym in cd:
                print (" " + sym, end="")
            print (" from " + str(j))

    accepting_state = (start_rule[0], start_rule[1], [], 0)
    return accepting_state in chart[len(tokens) - 1]

result = parse(tokens, grammar)
print(result)
