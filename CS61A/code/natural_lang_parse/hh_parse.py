# -*- coding:utf-8 -*-
# 按照教材写的natural language syntactic tree generator & parser.

##########################################
# 定义英语句子的树形结构.
##########################################

# Tree由tag和放在list中的branches组成。
class Tree:
    def __init__(self, tag, branches):
        assert len(branches) >= 1
        for b in branches:
            assert isinstance(b, (Tree, Leaf)) # 确保b要么是Tree，要么是Leaf 这两个class的实例.

# Leaf由tag和句子中的word本身组成.
class Leaf:
    def __init__(self, tag, word):
        self.tag = tag
        self.word = word

##########################################

# 对上面定义的结构的简单应用.
beasts = Leaf('N', 'buffalo')
intimidate =  Leaf('V', 'buffalo')
S, NP, VP = 'S', 'NP', 'VP'

# 构建一个句子的结构：
# buffalo buffalo buffalo.
#    N     -----VP------
#           V       N
# 这个实例化的对象的结构就表达了上面的句子.
s = Tree(S, [Tree(NP, [beasts]), 
             Tree(VP, [intimidate, 
                       Tree(NP, [beasts])
                      ])
            ])


##########################################
# 句子的生成
##########################################

# 一个dict, 存放Leaf.
lexicon = {
    Leaf('N', 'buffalo'), # beasts
    Leaf('V', 'buffalo'), # intimidate
}

# 一个dict, 存放语法规则.
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['N']],
    'VP': [['V', 'VP']],
}
# note: 这个dict的value都是双重括号.list里面套list

def expand(tag):
    """ Yield all trees rooted by tag. 
    比如，从'S' 展开为['NP', VP']; 从NP展开为N,...
    """
    # tag可以来自于两个地方
    # 在lexicon中找是否有符合的tag,有的话就yield它.
    for leaf in lexicon:   # leaf是新建的临时变量
        if tag == leaf.tag:
            yield leaf
    # 如果在grammar这个dict中能找到tag:
    if tag in grammar:
        for tags in grammar[tag]:  # 查找grammar[tag]下的value (那个value是列表)
            for branches in expand_all(tags):
                yield Tree(tag, branches)


def expand_all(tags):
    """ Yield all sequences of branches for a sequence of tags. 
    tags 可以是一个，也可以是多个元素的list. 
    """
    if len(tags) == 1:
        for branch in expand(tags[0]):
            yield [branch]    # yield的结果放进list里.

    else:
        # split these tags into 2 parts
        first, rest = tags[0], tags[1:]
        for first_branch in expand(first):
            for rest_branches in expand_all(rest):
                yield [first_branch] + rest_branches

#for tree in expand('S'):
#    print_tree(tree)