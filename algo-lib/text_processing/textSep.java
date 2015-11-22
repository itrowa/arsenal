// 读取文本文件中的内容, 按照指定的分隔符分隔为单词, 并打印出来.
// java textsep routes.txt " "
// java textSep tinyTale.txt " "
public class textSep {
    
    public static void main(String[] args) {
        String filename = args[0];
        String sep = args[1];
        //String[] words;

        In in = new In(filename);
        while (in.hasNextLine()) {
            String[] a = in.readLine().split(sep); // 读取一行, 分隔后每个单词作为一个数组元素.


            for ( int w = 0; w < a.length; w++)  // 读取数组中存放的所有单词
                StdOut.println(a[w]);
        }
    }
}