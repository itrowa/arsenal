# Earley parser for construct AST for a list of tokens and a Context-Free Grmmar set.

def addtochart(theset, index, elt):
    """ theset 是一个dict. 如果element没在index中, 则追加到the set [index]处.
    """

    if not(elt in theset[index]):
        theset[index] = [elt] + theset[index]
        return True
    else:
        return False

def closure (grammar, i, x, ab, cd, j):
    """ 对给定的grammar集和rewrite rule的状态 (x -> ab . cd), 将chart[i]处
        可能满足的state填入chart[i]
    """
    # 输入的state中 cd部分不能为空; 如果cd部分的第一个token在grammar的LHS中能找到, 则生成一条新的state:
    next_states = [(rule[0], [], rule[1], i) for rule in grammar if cd != [] and rule[0] == cd[0]]
    return next_states


def shift (tokens, i, x, ab, cd, j):
    """ tokens: a list of tokens
        state: x=> ab . cd from j.
        函数会返回一条新的state.
    """
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
            # 现在的state: x -> ab.cd, j
            # 对于c是满足的
            # 创建一条新的state: c-> .pqr, i
            # English: We're about to start parsing a "c", but 
            # "c" is a non-terminal, We'll bring those production rulse in.
            next_states = closure(grammar, i, x, ab, cd, j)
            for next_state in next_states:
                changes = addtochart(chart, i, next_state) or changes

            # apply rule 2
            # 对于state: x -> ab.cd, j 而言
            # 如果tokens[i] == c,
            # 则创建一条新的state: x -> abc.d, j 于chart[i+1].
            # English: We're looking for to parse token c next and the current
            # token is exact c! so we can parse over it and move to j+1

            next_state = shift(tokens, i, x, ab, cd, j)
            if next_state != None:
                changes = addtochart(chart, i+1, next_state) or changes

            # apply rule 3
            # 对于state: x -> a b . c d, j而言
            # 如果cd是[], 那么状态就是 x -> a b . , j
            # 对于在chart[j]中的每个 p -> q . x r, l而言
            # 创造一条新state:   p -> q x . r, l 于chart[i]
            # English: We just finished parsing an "x" with this token,
            # but that may have been a sub-step(like matching "exp -> 2"
            # in "2+3"). We should update the higher-level rules as well.
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

    # 如果chart填充完毕, 且能在读取所有的token后达到accepting state, 那么parsing成功.
    accepting_state = (start_rule[0], start_rule[1], [], 0)
    return accepting_state in chart[len(tokens) - 1]

result = parse(tokens, grammar)
print(result)
