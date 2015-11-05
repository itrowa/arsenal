import sys
# sys.stdin is a file-like object on which you can call functions read or readlines if you want to read everything or you want to read everything and split it by newline automatically.
# l = sys.stdin.readlines()

# python -i readstdin.py < tinyG.txt
# print(l)
# ['13\n', '13\n', '0 5\n', '4 3\n', '0 1\n', '9 12\n', '6 4\n', '5 4\n', '0 2\n', '11 12\n', '9 10\n', '0 6\n', '7 8\n', '9 11\n', '5 3\n']

la = sys.stdin.readlines()
print(la)

result = [ ]
for items in la:
    for i in items:
        result.append(i)

print(result)