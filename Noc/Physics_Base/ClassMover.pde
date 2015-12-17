class Mover {
  PVector location;
  PVector velocity;
  PVector acceleration;
  float mass;                    // now object has mass
  
  Mover(float m, float x, float y) {
    mass = m;
    location = new PVector(x, y);
    velocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
  }
  
  // newton's second law
  void applyForce(PVector force) {
    // F/M, and add to acceleration.
    PVector f = PVector.div(force, mass);
    acceleration.add(f);
  }
  
  void update() {
    velocity.add(acceleration);
    location.add(velocity);
    
    acceleration.mult(0);        // reset accel to 0
  }
  
  void display() {
    stroke(0);
    fill(175);
    ellipse(location.x, location.y, mass*16, mass*16);
  }
  
  void checkEdges() {
    if (location.x > width) {
      location.x = width;
      velocity.x *= -1;
    }
    else if (location.y > height) {
      velocity.y *= -1;
      location.y = height;
    }
  }
  
  boolean isInside(Liquid l) {
    if (location.x > l.x && 
        location.x < l.x + l.w &&
        location.y > l.y &&
        location.y < l.y + l.h) {
          return true;
        }
     else {
        return false;
     }
  }
  
  void drag(Liquid l) {
    float speed = velocity.mag();
    float dragMagnitude = l.c * speed * speed;
    PVector drag = velocity.get();
    drag.mult(-1);
    drag.normalize();
    drag.mult(dragMagnitude);
    applyForce(drag);
  }
}