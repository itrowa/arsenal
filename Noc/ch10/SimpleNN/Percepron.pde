// a Perception nerual cell(unit).

class Perceptron {
  float[] weights;
  float c = 0.01;
  
  // constructor.
  // n: num of inputs.
  Perceptron (int n) {
    weights = new float[n];
    for (int i = 0; i < weights.length; i++) {
      weights[i] = random(-1, 1);
    }
  }
  
  // adopt some inputs and gen output.
  int feedforward(float[] inputs) {
    float sum = 0;
    for (int i = 0; i < weights.length; i++) {
      sum += inputs[i]*weights[i];
    }
    return activate(sum);
  }
  
  int activate(float sum) {
    if (sum > 0) return 1;
    else         return 0;
  }
  
  // a training function. using known inputs and
  // answer to train a Perception's weight.
  void train(float[] inputs, int desired) {
    int guess = feedforward(inputs);
    float error = desired - guess;
    for (int i = 0; i < weights.length; i++) {
      weights[i] += c * error * inputs[i];
    }
  }
}