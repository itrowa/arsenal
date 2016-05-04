// a cell object. 
class Cell {
  float x, y;
  float w;
  
  int state;    // current state
  int previous; // previous state
  
  Cell(float x_, float y_, float w_) {
    x = x_;
    y = y_;
    w = w_;
    
    state = int(random(2));
    previous = state;
  }
  
  // save current state.
  void savePrevious() {
    previous = state;
  }
  
  // apply new state s to the cell.
  void newState(int s) {
    state = s;
  }


  void display() {
    if (previous == 0 && state == 1) 
      fill(0, 0, 255); // if respawn, fill with blue! 
    else if (state == 1) 
      fill(0);
    else if (previous == 1 && state == 0) 
      fill(255, 0, 0);
    else 
      fill(255);
    stroke(0);
    rect(x, y, w, w);   
  }

}