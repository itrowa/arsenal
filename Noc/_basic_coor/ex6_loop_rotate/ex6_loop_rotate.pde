// 清单 6. 更有意思的转换和旋转
size(200, 200);
rectMode(CENTER);
noFill();
translate(100, 100);

for (int i = 1 ; i < 16 ; i++) {
  rotate( (PI/16)*i );
  rect(0, 0, 100, 100);
}