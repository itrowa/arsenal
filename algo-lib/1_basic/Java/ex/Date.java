// 以一个Date 抽象数据类型(ADT)为例，说明class的写法。
public class Date implements Comparable<Date>{
    // announce instance variables
    private final int month;
    private final int day;
    private final int year;

    // constructor: init instance vars.
    public Date(int m, int d, int y) {
        month = m; day = d; year = y;
    }

    // implement by API requirements.
    public int day() {
        return day;
    }
    public int month() {
        return month;
    }
    public int year() {
        return year;
    }

    // overload parent class methods.
    public String toString() {
        return month() + "/" + day() + "/" + year();
    }

    public boolean equals(Date x) {
        if (this == x) return true;
        if (x == null) return false;
        if (this.getClass() != x.getClass()) return false;
        Date that = Date x;
        if (this.day != that.day) return false;
        if (this.month != that.month) return false;
        if (this.year != that.year) return false;
        return true;
    }
}