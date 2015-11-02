class Walker{
    int x;
    int y;

    // constructor
    Walker(){
        x = width / 2;
        y = height / 2;
    }

    void display() {
        stroke(0);
        point(x, y);
    }

    void step(){
        int choice = int(random(4)); //0,2,2,or 3
        if(choice == 0) {
            x++;
        } else if (choice == 1) {
            x--;
        } else if (choice == 2) {
            y++;
        } else {
            y--;
        }
    }
}

Walker w;

void setup(){
  size(640,360);
  w = new Walker();
  background(255);
}

void draw() {
  w.step();
  w.display();
}