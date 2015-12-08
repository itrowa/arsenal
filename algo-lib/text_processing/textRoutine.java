public class textRoutine {

    public static void wordFromString(String[] args) {
        String input_str = "she sells sea shells by the sea shore";
        String[] str = input_str.split(" ");

        int i = 0;
        for (String s : str) {
            StdOut.println(s + " " + i);
            i++;
        }
    }

    // 读取文本文件中的内容, 按照指定的分隔符分隔为单词, 并打印出来.
    // java textsep routes.txt " "
    // java textSep tinyTale.txt " "
    public static void wordFromText(String[] args) {
        String filename = args[0];
        String sep = args[1];

        In in = new In(filename);
        while (in.hasNextLine()) {
            String[] a = in.readLine().split(sep); // 读取一行, 分隔后每个单词作为一个数组元素.


            for ( int w = 0; w < a.length; w++)  // 读取数组中存放的所有单词
                StdOut.println(a[w]);
        }
    }

    public static void main(String[] args) {
       String t = "ABABAC" ;
       StdOut.println(t.charAt(0));
    }
}