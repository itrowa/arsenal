// Game of Life: a chess board-like object. 
class GOL {
  int w = 8;
  int columns, rows;
  Cell[][] board;
  
  GOL() {
    columns = width/w;
    rows = height/w;
    board =  new Cell [columns][rows];
    
    for (int x = 0; x < columns; x++) {
      for (int y = 0; y < rows; y++) {
      board[x][y] = new Cell(x*w, y*w, w); //<>//
      }
    }
  }
  
  void generate() {
    //Cell [][] next = new Cell [columns][rows];   // the next board. //<>//
    for (int i=0; i<columns; i++){
      for (int j=0; j<rows; j++){
        board[i][j].savePrevious();
      }
    }
    
    for (int x = 1; x < columns-1; x++) {
      for (int y = 1; y < rows-1; y++) {
        
        // calc total num of neighbors
        int neighbors = 0;
        
        if (board[x-1][y-1].state == 1) neighbors++;
        if (board[x  ][y-1].state == 1) neighbors++;
        if (board[x+1][y-1].state == 1) neighbors++;
        
        if (board[x-1][y  ].state == 1) neighbors++;
        if (board[x+1][y  ].state == 1) neighbors++;
        
        if (board[x-1][y+1].state == 1) neighbors++;
        if (board[x  ][y+1].state == 1) neighbors++;
        if (board[x+1][y+1].state == 1) neighbors++; //<>//
            
        // calc next[x][y]
        if ((board[x][y].state == 1) && (neighbors < 2))        board[x][y].newState(0);
        else if ((board[x][y].state == 1) && (neighbors > 3))   board[x][y].newState(0);
        else if ((board[x][y].state == 0) && (neighbors == 3))  board[x][y].newState(1);
      }
    } 
  }
  
  void display() {
    for (int i = 0; i < columns; i++) {
      for (int j = 0; j < rows; j++) {
        board[i][j].display();
      }
    }
  }
}
  
  