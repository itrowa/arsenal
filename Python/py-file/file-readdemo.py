def main():

    # 用read()方法读取一个文件
    infile = open("Presidents.txt", "r")
    print("(1) Using read(): ")
    print(infile.read() + "\n")
    infile.close()

    # 用read(n)方法读取一个文件
    infile = open("Presidents.txt", "r")
    print("(2) Using read(number): ")
    s1 = infile.read(4)
    print(s1)
    s2 = infile.read(10)
    print(s2)
    print(repr(s2))
    infile.close()

    # 用readline()方法读取一个文件
    infile = open("Presidents.txt", "r")
    print("\n(3) Using readline(): ")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    infile.close()

    # 用readlines()方法读取一个文件
    infile = open("Presidents.txt", "r")
    print("\n(4) Using readlines(): ")
    print(infile.readlines())
    infile.close()

main()