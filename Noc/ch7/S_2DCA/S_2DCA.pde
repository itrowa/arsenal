GOL gol;

void setup() {
  size(640, 480);
  frameRate(24);
  gol = new GOL();
}

void draw() {
  background(255);
  gol.generate();
  gol.display();
}

void mousePressed() {
  gol.init();
}



int [][] board =  new int [columns][rows];

for (int x = 0; x < columns; x++) {
  for (int y = 0; y < rows; y++) {
    current[x][y] = int(random(2));
  }
}

// calc next state!
int [][] next = new int[columns][rows];
for (int x = 1; x < columns-1; x++) {
  for (int y = 1; y < rows-1; y++) {
    
    // calc total num of neighbors
    int neighbors = 0;
    
    if (board[x-1][y-1] == 1) neighbors++;
    if (board[x  ][y-1] == 1) neighbors++;
    if (board[x+1][y-1] == 1) neighbors++;
    
    if (board[x-1][y  ] == 1) neighbors++;
    if (board[x+1][y  ] == 1) neighbors++;
    
    if (board[x-1][y+1] == 1) neighbors++;
    if (board[x  ][y+1] == 1) neighbors++;
    if (board[x+1][y+1] == 1) neighbors++;
        
    // calc next[x][y]
    if ((board[x][y] == 1) && (neighbors < 2) {
      next[x][y] = 0;
    }
    
    if ((board[x][y] == 1) && (neighbors < 2)) {
      next[x][y] = 0;
    }
    else if ((board[x][y] == 1) && (neighbors > 3)) {
      next[x][y] = 0;
    }
    else if ((board[x][y] == 0) & (neighbors == 3)) {
      next[x][y] = 1;
    }
    else {
      next[x][y] = board[x][y];
    }  
    
  }
}

board = next;


//display
for (int i = 0; i < columns; i++) {
  for (int j = 0; j < rows; j++) {
    if ((board[i][j] == 1)
      fill(0);
    else fill(255);
      stroke(0);
      
      rect(i*w, j*w, w, w);
      
  }
}