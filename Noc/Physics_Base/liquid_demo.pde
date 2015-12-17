Liquid liquid;
Mover[] movers = new Mover[100];

void setup() {
  size(360, 640);
  smooth();
  for (int i = 0; i < movers.length; i++) {
    movers[i] = new Mover(random(0.1, 5), 0, 0);
  }
  liquid = new Liquid(0, height/2, width, height/2, 0.1);
}

void draw() {
  background(255);
  liquid.display();
  
  for (int i = 0; i < movers.length; i++) {
    if (movers[i].isInside(liquid)) {
      movers[i].drag(liquid);
    }
    float m = 0.1 * movers[i].mass;
    PVector gravity = new PVector(0, m);        // calc gravity by mass
    movers[i].applyForce(gravity);
    movers[i].update();
    movers[i].display();
    movers[i].checkEdges();
  }
}