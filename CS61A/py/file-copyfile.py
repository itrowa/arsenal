import os.path
import sys

def main():
    # 提示用户输入文件名
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()

    # 确认文件存在
    if os.path.isfile(f2):
        print(f2 + " already exists")
        sys.exit()

    # 打开文件来作为输入和输出
    infile = open(f1, "r")
    outfile = open(f2, "w")

    # 把input file的内容复制到outfile去
    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines, "line and", countChars, "chars copied")

    # 关闭文件对象:
    infile.close()
    outfile.close()

main()
