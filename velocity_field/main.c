// a prototype of real-time N-S solver.
// ref: http://www.dgp.toronto.edu/people/stam/reality/Research/pub.html

// 二维点阵用一维数组表示.
size = (N + 2) * (N + 2);

// 声明这些个2维格点
// u, v: 速度场的x和y分量. 带prev的是表示前一个时刻的对应速度场的分量.
static u[size], v[size], u_prev[size], v_prev[size];

// 选择某个座标所代表的格点
#define IX(i, j) ((i) + (N+2)*(j))
// eg: 选择u上的(i,j)点:
// u[IX(i,j)]


// add source into velocity field.
// s[]: 当前帧中, 每个格子上的密度源!
// x[]: 当前帧中, 棋盘的密度场.
void add_source(int N, float *x, float *s, float dt) {
    int i, size = (N+2) * (N+2);
    for (i = 0; i < size; i++)
        x[i] += dt*s[i];
}

// this not gonna work!
// *x0: 老的密度场
// *x : 新的密度场
// diff > 0 表示当前格子的密度会发散到邻居去
void diffuse_bad (int N, int b, float *x, float *x0, float diff, float dt) {
    int i, j;
    float a = dt * diff * N * N;

    for ( i = 1; i <= N; i++)  {
        for (j = 1; j <= N; j++) {
            x[IX(i, j)] =       x0[IX(i, j)  ] + a * (x0[IX(i-1, j)])
                          +     x0[IX(i, j-1)] +      x0[IX(i, j+1)]
                          - 4 * x0[IX(i, j)];
        }
    }
    set_bnd(N, b, x);
}

// 计算密度的发散项.
// *x0: 老的密度场
// *x : 新的密度场
// diff > 0 表示当前格子的密度会发散到邻居去
void diffuse (int N, int b, float *x, float *x0, float diff, float dt) {
    int i, j, k;
    float a = dt * diff * N * N;

    for (k=0; k<20; k++) {
        for(i=1; i<=N; i++) {
            // Gauss-Seidel Relaxiation
            for(j=1; j<=N; j++) {
                x[IX(i,j)] = (x0[IX(i,j)]) + a*(x[IX(i-1,j)] + x[IX(i+1,j)]
                                            + x[IX(i,j-1)] + x[IX(i,j+1)]) / (1+4*a);
            }
        }
    set_bnd(N, b, x);
    }
}

// *d: 当前的密度场   *d0: dt前的密度场
//
void advect(int N, int b, float *d, float *d0, float *u, float *v, float dt){
    int i, j, i0, j0, i1, j1;
    float x, y, s0, s1, t1, dt0;

    dt0 = dt*N;
    for (i=1; i<=N; i++) {
        for (j=1; j<=N; j++) {
            // 计算前一个时刻, 一个粒子在速度场作用下运动的距离(x, y).
            x = i - dt0 * u[IX(i,j)];
            y = j - dt0 * v[IX(i,j)];

            // 计算前一个时刻粒子坐标x, y所对应的格点下标

            if (x < 0.5) x = 0.5;
            if (x> N+0.5) x = N+0.5;
            j0 = (int)x;              // 把座标转换为数组下标..
            j1 = j0 + 1;

            if (y < 0.5) y = 0.5;
            if (y > N+0.5) y = N+0.5;
            j0 = (int)y;
            j1 = j0 + 1;

            s1 = x-i0;
            s0 = 1-s1;
            t1 = y-j0;
            t0 = 1-t1;

            d[IX(i,j)] =   s0 * (t0 * d0[IX(i0,j0)] + t1 * d0[IX(i0, j1)])
                         + s1 * (t0 * d0[IX(i1, j0)] + t1 * d0[IX(i1, j1)])
        }
    }
    set_bnd(N, b, d);
  }

void dens_step(int N, float *x, float *x0, float *u, float *v, float diff, float dt) {
    add_source(N, x, x0, dt);
    SWAP(x0, x); diffuse(N, 0, x, x0, diff, dt);
    SWAP(x0, x); advect(N, 0, x, x0, u, v, dt);
}

#define SWAP(x0 , x) {float *tmp = x0; x0 = x; x = tmp;}

void project (int N, float *u, float *v, float *p, float *div) {
    int i, j, k
    float h;

    h = 1.0/N;
    for (i = 1; i <= N; i++) {
        for (j = 1; j <=N; j++) {
            // Gauss-Seidel Relaxiation
            div[IX(i,j)] = -0.5 * h * (u[IX(i+1,j)] - u[IX(i-1,j)]
                                       +v[IX(i,j+1)] - v[IX(i,j-1)]);
            p[IX(i,j)] = 0;
        }
    }
    set_bnd(N, 0, div);
    set_bnd(N, 0, p);

    for (k=0; k<20; k++) {
        for (i=1; i<=N; i++) {
            for (j=1; j<=N; j++) {
                p[IX(i,j)] = (div[IX(i,j)] + p[IX(i-1,j)] + p[IX(i+1,j)]
                                           + p[IX(i,j-1)] + p[IX(i,j+1)]) / 4;
            }
        }
        set_bnd(N, 0, p);
    }

    for (i=1; i<=N; i++) {
        for(j=1; j<=N; j++) {
            u[IX(i,j)] -= 0.5 * (p[IX(i+1,j)] - p[IX(i-1,j)]) / h;
            v[IX(i,j)] -= 0.5 * (p[IX(i,j+1)] - p[IX(i,j-1)]) / h;
        }
    }
    set_bnd(N, 1, u);
    set_bnd(N, 2, v);
}

// 设置场*x在边界上的格点的值.
void set_bnd(int N, int b, float *x) {
    int i;
    // 设置4个边线上的*x场的值.
    for (i = 1; i <= N; i++) {
        x[IX(0, i)]    = b == 1 ? -x[IX(1,i)] : x[IX(1,i)];
        x[IX(N+1,i)]   = b == 1 ? -x[IX(N,i)] : x[IX(N,i)];
        x[IX(i,0)]     = b == 2 ? -x[IX(i,1)] : x[IX(i,1)];
        x[IX(i,N+1)]   = b == 2 ? -x[IX(i,N)] : x[IX(i,N)];
    }
    // 手动设置4个角点
    x[IX(0,0)] = 0.5 * (x[IX(1,0)] + x[IX(0,1)]);
    x[IX(0,N+1)] = 0.5 * (x[IX(1,N+1)] + x[IX(0,N)]);
    x[IX(N+1,0)] = 0.5 * (x[IX(N,0)] + x[IX(N+1,1)]);
    x[IX(N+1,N+1)] = 0.5 (x[IX(N,N+1)] + x[IX(N+1,N)]);
}

while(simulating){
    get_from_UI(den_prev, u_prev, v_prev);
    vel_step(N, u, v, u_prev, v_prev, visc, dt);
    dens_step(N, dens, dens_prev, u, v, diff, dt);
    draw_dens(N, dens);
}
