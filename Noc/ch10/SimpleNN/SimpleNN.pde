// a very simple nerv network to identify weather a point is above a line or not.

Perceptron ptron;
Trainer[] training = new Trainer[2000];
int count = 0;

// define a linear function (a line).
float f(float x) {
  return x + 1;
}

void setup() {
  size(800, 800);
  ptron = new Perceptron(3);    // define a perceptron with 3 inputs.
  
  for (int i = 0; i < training.length; i++) {
    // create a random point somewhere on the canvas
    float x = random(-width/2, width/2);
    float y = random(-height/2, height/2);

    // we'll give the correct answer, as training data..
    int answer = 1;
    if (y < f(x)) answer = -1;
    // and store into this array..
    training[i] = new Trainer(x, y, answer);
  }
}

//
void draw() {
  background(255);
  translate(width/2, height/2);
  ptron.train(training[count].inputs, training[count].answer);
  count = (count + 1) % training.length;     // when count exceeds training.length, count come back to zero.
  
  for (int i = 0; i < count; i++) {
    stroke(0);
    int guess = ptron.feedforward(training[i].inputs);
    if (guess > 0) noFill();
    else           fill(0);
    ellipse(training[i].inputs[0], training[i].inputs[1], 8, 8);
  }
}