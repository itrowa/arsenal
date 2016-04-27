Rect[] agents = new Rect[15];

void setup() {
  size(600, 600);
  smooth();
  for (int i = 0; i < 15; i++)
    agents[i] = new Rect();
}

void draw() {
  background(255);
  for (int i = 0; i < 15; i++)
    agents[i].display();
}