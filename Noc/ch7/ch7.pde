class CA {
  int[] ceslls;
  int[] ruleset;
  
  CA() {
    cells = new int[width];
    ruleset = {0, 1, 0, 1, 1, 0, 1, 0};
    
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
  }
  
  int rules (int a, int b, int c) {
    String s = "" + a + b + c;
    int index = Integer.parseInt(s, 2);
    return ruleset[index];
  }
  
  
  
}

int[] cells = [];

for (int i = 0; i < cells.length(); i++) {
  //do sth? 
  if (cells[i] == 0) fill(255);
  else fill(0);
  stroke(0);
  rect(i*50, 0, 50, 50);
}




//int[] ruleset = {0, 1, 0, 1, 1, 0, 1, 0};

//int rules (int a, int b, int c) {
//  if      (a == 1 && b == 1 && c == 1) return ruleset[0];
//  else if (a == 1 && b == 1 && c == 0) return ruleset[1];
//  else if (a == 1 && b == 0 && c == 1) return ruleset[2];
//  else if (a == 1 && b == 0 && c == 0) return ruleset[3];
//  else if (a == 0 && b == 1 && c == 1) return ruleset[4];
//  else if (a == 0 && b == 1 && c == 0) return ruleset[5];
//  else if (a == 0 && b == 0 && c == 1) return ruleset[6];
//  else if (a == 0 && b == 0 && c == 0) return ruleset[7];
//  return 0;
//}