class Mover {
  // linear kinetics
  PVector location;
  PVector velocity;
  PVector acceleration;
  
  float mass;                    // now object has mass
  
  // angluar kinetics
  float angle = 0;
  float aVelocity = 0;
  float aAcceleration = 0;


  void update() {
    // linear movement
    velocity.add(acceleration);
    location.add(velocity);
    
    // angle movement
    aAcceleration = acceleration.x / 10.0;     // determine the a accel
    aVelocity += aAcceleration;
    aVelocity = constrain(aVelocity, -0.1, 0.1);
    angle += aVelocity;
    
    acceleration.mult(0);
  }

  void display() {
    stroke(0);
    fill(175, 120);
    rectMode(CENTER);
    pushMatrix();
    translate(location.x, location.y);
    rotate(angle);
    rect(0, 0, mass*16, mass*16);
    popMatrix();
  }
}