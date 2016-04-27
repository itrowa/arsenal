// java CollisonSystem 5

public class CollisionSystem {
    private class Event implements Comparable<Event> {
        private final double time;
        private final Particle a, b;
        private final int countA, countB;

        public Event(double t, Particle a, Particle b) {
            // 事件是和两个粒子a, b相关的，并且约定当b为空时，事件是a撞墙
            this.time = t;
            this.a = a;
            this.b = b;
            // countA和countB分别记录着a和b粒子发生过的碰撞的次数.记录这个变量
            // 的目的是为了排除掉无效碰撞.
            if (a != null) countA = a.count();
            else countA = -1;
            if (b != null) countB = b.count();
            else countB = -1;
        }

        public int compareTo(Event that) {
            if (this.time < that.time) return -1;
            else if (this.time > that.time) return +1;
            else return 0;
        }

        /* 判断这个事件是否合法.
        */
        public boolean isValid() {
            if (a != null && a.count() != countA)
                return false;
            if (b != null && b.count() != countB)
                return false;
            return true;
        }
    }

    private MinPQ<Event> pq;    // 优先队列
    private double t = 0.0;
    private Particle[] particles;

    public CollisionSystem(Particle[] particles) {
        this.particles = particles;
    }

    /* 预测粒子a在一段时间内所有的碰撞。并写入到pq中
    */
    private void predictCollisions(Particle a, double limit) {
        if (a == null) return;
        for (int i = 0; i < particles.length; i++) {
            // 将与particle[i]发生碰撞的事件插入pq中
            double dt = a.timeToHit(particles[i]);
            if (t + dt <= limit)
                pq.insert(new Event(t + dt, a, particles[i]));
        }
        double dtX = a.timeToHitVerticalWall();
        if (t + dtX <= limit)
            pq.insert(new Event(t + dtX, a, null));
        double dtY = a.timeToHitHorizontalWall();
        if (t + dtY <= limit)
            pq.insert(new Event(t + dtY, null, a));
    }

    /* 重绘事件：重新画出所有粒子
    */
    public void redraw(double limit, double Hz) {
        StdDraw.clear();
        for (int i = 0; i < particles.length; i++)
            particles[i].draw();
        StdDraw.show(20);
        if (t < limit)
            pq.insert(new Event(t + 1.0 / Hz, null, null));
    }

    /* 主循环
    */
    public void simulate(double limit, double Hz) {
        pq = new MinPQ<Event>();
        for (int i = 0; i < particles.length; i++)
            predictCollisions(particles[i], limit);
        pq.insert(new Event(0, null, null));

        while(!pq.isEmpty()) {
            // 处理一个事件?
            Event event = pq.delMin();
            if (!event.isValid())
                continue;
            for (int i = 0; i < particles.length; i++)
                particles[i].move(event.time - t);   // 更新粒子的位置
            t = event.time;                          // 和时间
            Particle a = event.a, 
                     b = event.b;

            if      (a != null && b != null) a.bounceOff(b);
            else if (a != null && b == null) a.bounceOffVerticalWall();
            else if (a == null && b != null) b.bounceOffHorizontalWall();
            else if (a == null && b == null) redraw(limit, Hz);
            predictCollisions(a, limit);
            predictCollisions(b, limit);
        }
    }

    public static void main(String[] args) {
        StdDraw.show(0);
        int N = Integer.parseInt(args[0]);
        Particle[] particles = new Particle[N];

        for (int i = 0; i < N; i++)
            particles[i] = new Particle();
        CollisionSystem system = new CollisionSystem(particles);
        system.simulate(10000, 0.5);
    }
}