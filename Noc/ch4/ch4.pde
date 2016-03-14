// a particle system with a repeller obj.
ParticleSystem ps;
Repeller repeller;

void setup() {
  size(200, 200);
  smooth();
  ps = new ParticleSystem(new PVector(width/2, 50));
  repeller = new Repeller(width/2 - 20, height/2);
}

void draw() {
  background(100);
  ps.addParticle();
  
  // global gravity
  PVector gravity = new PVector(0, 0.1);
  ps.applyForce(gravity);
  ps.applyRepeller(repeller);
  
  ps.run();
  repeller.display();
}