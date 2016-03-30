class Liquid {
  // definition for liquid area
  float x, y, w, h;
  float c;                    // drag coefficient
  
  Liquid(float x_, float y_, float w_, float h_, float c_) {
    x = x_;
    y = y_;
    w = w_;
    h = h_;
    c = c_;
  }
  
  void display() {
    noStroke();
    fill(175);
    rect(x, y, w, h);
  }
}