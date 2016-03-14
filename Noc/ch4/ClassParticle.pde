// a Particle class.
// has: location, velocity, accelaration, and external force will add to acceleration.
// has life span.
class Particle {
  PVector location;
  PVector velocity;
  PVector acceleration;
  float lifespan;
  
  float mass = 1;
  
  // constructor.
  // @param l: location vector.
  Particle(PVector l) {
    location = l.get();
    acceleration = new PVector(0, 0);
    velocity = new PVector(random(-1,1), random(-2,0));
    lifespan = 255;
  }

  // resolve an external force into acceleration.
  void applyForce(PVector force) {
    PVector f = force.get();
    f.div(mass);
    acceleration.add(f);
  }
  
  void run() {
    update();
    display();
  }
  
  // test if this particle is dead.
  boolean isDead() {
    if (lifespan < 0.0) {
      return true;
    }
    else {
      return false;
    }
  }
  
  // update it's status
  void update() {
    velocity.add(acceleration);
    location.add(velocity);
    acceleration.mult(0);
    lifespan -= 2.0;
  }
  
  // display into the screen
  void display() {
    stroke(0, lifespan); // 他俩都可以接收2个参数的。
    fill(175, lifespan);
    ellipse(location.x, location.y, 8, 8);
  }
}