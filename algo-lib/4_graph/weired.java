public class weired {
    private static int charAt(String s, int d) {
        if (d < s.length())
            return s.charAt(d);
        else 
            return -1;
        // 当索引d超过了字符串的末尾时, 直接返回-1
    }
        public static void main(String[] args) {
            String ss = "ABCDEFG";
            for (int i = 0; i < ss.length(); i++) {
                
                int t = charAt(ss, i);
                StdOut.println(t);
            }
        }
}
