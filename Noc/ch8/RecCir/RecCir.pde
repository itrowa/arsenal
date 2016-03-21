void setup() {
  size(1152, 864);
  background(255);
  
}

void draw() {
  drawCircle(width/2, height/2, 1200);
}

void drawCircle(float x, float y, float radius) {
  stroke(0.1);
  noFill();
  ellipse(x, y, radius, radius);
  if (radius > 24) {
    radius *= 0.5;
    drawCircle(x + radius/2, y, radius);
    drawCircle(x - radius/2, y, radius);
    drawCircle(x, y+radius/2, radius);
    drawCircle(x, y-radius/2, radius);
  }
}