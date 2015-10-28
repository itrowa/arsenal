# 截断所有的单词成为一个一个的字母列表.
words = ['cat','dog','rabbit']
letters = [ ]
for word in words:
    for letter in word:
        letters.append(letter)
print(letters)