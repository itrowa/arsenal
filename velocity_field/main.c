// add source into velocity field.
// s[]: 当前帧中, 每个格子上的密度源!
// x[]: 当前帧中, 棋盘的密度场.
void add_source(int N, float *x, float *s, float dt) {
    int i, size = (N+2) * (N+2);
    for (i = 0; i < size; i++)
        x[i] += dt*s[i];
}

void diffuse_bad (int N, int b, float *x, float *x0, float diff, float dt) {
   int i, j;
   float a = dt * diff * N * N;

   for ( i = 1; i <= N; i++)  {
        for (j = 1; j <= N; j++) {
            x[IX(i, j)] = x0[IX(i, j)  ] + a * (x0[IX(i-1, j)]) +
                          x0[IX(i, j-1)] +      x0[IX(i, j+1)]  -
                          4 * x0[IX(i, j)];
        }
   }
   set_bnd(N, b, x);
}

void diffuse (int N, int b, float *x, float *x0, float diff, float dt) {
    
}