// 清单 8. 基于鼠标的简单 3D 旋转示例
void setup() {
  size(200, 200, P3D);
  noFill();
  smooth();
}

void draw() {
  background(0);
  
  translate(width/2, height/2, -(width/2));
  rotateY(map(mouseX, 0, width, -PI, PI));
  stroke(100);
  box(150);
  
  rotateX(map(mouseY, 0, height, -PI, PI));
  stroke(150);
  box(75);
}