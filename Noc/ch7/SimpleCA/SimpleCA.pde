// most simple CA. Rule 90.
CA ca;

void setup(){
  size(800, 400);
  background(255);
  ca = new CA();
}

void draw() {
  ca.display(); // draw CA;
  if (ca.generation < height / ca.w) {
    ca.generate();
  }
}

class CA {
  int[] cells;
  int[] ruleset = {0, 1, 0, 1, 1, 0, 1, 0}; // 1 stands for alive. 0 for dead.
  int w = 10;
  int generation = 0;
  
  CA() {
    cells = new int[width/w];
    
    for (int i=0; i<cells.length; i++) {
      cells[i] = 0;
    }
    cells[cells.length/2] = 1;
  }
  
  void generate() {
    int[] nextgen = new int[cells.length];   // a temp cell store next gen state.
    for (int i=1; i<cells.length-1; i++) {    // we do not iterate cells on boundary.
      int left = cells[i-1];
      int me = cells[i];
      int right = cells[i+1];
      
      nextgen[i] = rules(left, me, right);
    }
    cells = nextgen;
    generation++;
  }
  
  int rules (int a, int b, int c) {
    String s = "" + a + b + c;
    int index = Integer.parseInt(s, 2);
    return ruleset[index];
  }
  
  void display() {
    for (int i = 0; i < cells.length; i++) {
      //do sth? 
      if (cells[i] == 0) 
        fill(255);
      else 
        fill(0);
      stroke(0);
      rect(i*w, generation*w, w, w);
    }
  }
    
}