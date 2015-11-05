def main():
    # open file for output
    outfile = open("Presidents.txt", "w")

    # write data
    outfile.write("Bill Cliton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama")

    # 记得关闭文件！
    outfile.close()

main()