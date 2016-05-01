Pbox2D box2d;

void setup() {
  box2d = new PBox2D(this);
  box2d = createWorld();
}

void draw(){
  box2d.step();
}