class Rect {
  // Rect的智能体.
  PVector location;
  int w;
  
  Rect() {
    location = new PVector(random(width), random(height));
    w = int(random(0, 20));  
  }
  
  void update(){
  }
  
  
  
  void display(){
    stroke(180);
    fill(175);
    rect(location.x - w/2, location.y - w/2, w, w);
  }
}