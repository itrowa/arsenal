
class Mover {
  PVector location;    //r
  PVector velocity;    //r'
  PVector acceleration; //r''
  float topspeed;
  
  // constructor
  Mover() {
    location = new PVector(random(width), random(height));
    velocity = new PVector(random(-2, 2), random(-2, 2));
    acceleration = new PVector(0, 0);
    topspeed = 10;
  }
  
  void update() {
    velocity.add(acceleration);
    velocity.limit(topspeed);
    location.add(velocity);
  }
  
  void display() {
   stroke(0);
   fill(175);
   ellipse(location.x, location.y, 16, 16);
  }
  
  void checkEdges() {
    if (location.x > width) {
      location.x = 0;
      } 
    else if (location.x < 0) {
      location.x = width;
      }
    
    if (location.y > height) {
      location.y = 0;
      } 
    else if (location.y < 0) {
      location.y = height;
      }
  }
}


Mover mover;

void setup() {
  size(200, 200);
  smooth();
  
  mover = new Mover();
}

void draw() {
  background(255);
  
  mover.update();
  mover.checkEdges();
  mover.display();
}