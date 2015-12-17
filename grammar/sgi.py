# 上下文无关语法推演:
# 从一个起始符号开始, 按照设立好的语法和规则的序列对符号进行推演 然后返回结果.

class CFG(object):
    def __init__(self):
        """ 语法是一系列规则的列表. 
            每一条规则都是一个dict, 左手边就是Key, 右手边就是
            value, 右手边是一个tuple.

            好处: 每条规则都有下标, 可以通过指定通过一个特定的
            规则序列来导出一个句子了.
        """
        self.prod = []

    def add_prod(self, lhs, rhs):
        """ Add one rule to the grammar. 'rhs' is just
            an symbol or serval symbols seperated by 
            spaces.

            Usage:
                g.add_prod('NT', 'VP PP')
                g.add_prod('Digit', '1')
                g.add_prod('Digit', '2')
                g.add_prod('Digit', '3')
                g.add_prod('Digit', '4')

        """
        rule =  {}
        rule[lhs] = tuple(rhs.split())

        self.prod.append(rule)
            # self.prod[lhs].append(tuple(prod.split()))

    def gen_by_rules(self, indices, I):
        """ generate a sentences by a sequence of rule indices. from 
            initial symbol I.
            rules is a sequence of num seperated by spaces
            which represents the subscriptions for rules  
            in self.prod[]. 

            eg:
            g.gen_by_rules([2, 3, 1], 'U')
        """
        symbols = I

        for i in indices:
            symbols = self.gen(i, symbols)

        return symbols
                
    def gen(self, i, symbols):
        """ 对于一个symbols 列表, 按照规则i指定的规则推演这个列表,然后返回推演结果.
        """
        result = []
        for sym in symbols:
            sym_for_i = list(self.prod[int(i)].keys())[0] 
            if sym_for_i == sym:
                for s in self.prod[int(i)][sym_for_i]:
                    result.append(s)
            else:
                result.append(sym)
        return result



g = CFG()
g.add_prod('U', '0')
g.add_prod('U', '1')
g.add_prod('U', '0 U')
g.add_prod('U', '1 U')
g.gen_by_rules([2, 3, 1], 'U')

# g = CFG()
# g.add_prod('S', 'NP VP')
# g.add_prod('NP', 'I')
# g.add_prod('NP', 'he')
# g.add_prod('NP', 'she')
# g.add_prod('NP', 'Joe')
# g.add_prod('VP', 'V NP')
# g.add_prod('VP', 'NP')
