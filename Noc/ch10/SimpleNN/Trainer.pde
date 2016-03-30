// a trainer obj stores a training data, consists of input and 
// desired answer.
class Trainer {
  float[] inputs;
  int answer;
  

  // constructor
  Trainer(float x, float y, int a) {
    inputs = new float[3];
    inputs[0] = x;
    inputs[1] = y;
    inputs[2] = 1;
    answer = a;
  }
}