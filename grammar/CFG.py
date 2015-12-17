# define a context-free-grammar object and randomly generate some sentences from this cfg.
# 
# original post here:
# http://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar/

import collections, random

class CFG(object):
    def __init__(self):
        self.prod = collections.defaultdict(list)
        # create a dict, in which every value is a list.

    def add_prod(self, lhs, rhs):
        """ Add production to the grammar. 'rhs' can
            be several productions separated by '|'.
            Each production is a sequence of symbols
            separated by whitespace.

            Usage:
                grammar.add_prod('NT', 'VP PP')
                grammar.add_prod('Digit', '1|2|3|4')
        """
        prods = rhs.split('|')
        for prod in prods:
            self.prod[lhs].append(tuple(prod.split()))

    def gen_random(self, symbol):
        """ Generate a random sentence from the
            grammar, starting with the given
            symbol.
        """
        sentence = ''

        # select one production of this symbol randomly
        rand_prod = random.choice(self.prod[symbol])

        for sym in rand_prod:
            # for non-terminals, recurse
            if sym in self.prod:
                sentence += self.gen_random(sym)
            else:
                sentence += sym + ' '

        return sentence

cfg1 = CFG()
cfg1.add_prod('S', 'NP VP')
cfg1.add_prod('NP', 'Det N | Det N')
cfg1.add_prod('NP', 'I | he | she | Joe')
cfg1.add_prod('VP', 'V NP | VP')
cfg1.add_prod('Det', 'a | the | my | his')
cfg1.add_prod('N', 'elephant | cat | jeans | suit')
cfg1.add_prod('V', 'kicked | followed | shot')

ex1 = CFG()
ex1.add_prod('U', '0 | 1 | 0 U | 1 U')
