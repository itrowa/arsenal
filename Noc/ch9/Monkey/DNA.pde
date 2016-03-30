class DNA {
  char[] genes = new char[18];
  float fitness;
  
  // constructor: make a random sentence.
  DNA() {
    for (int i = 0; i < genes.length; i++) {
      genes[i] = (char) random(32, 128); // the ascii encodings of chars
    }
  }
  
  // cals fitness value.
  void fitness() {
    int score = 0;
    for (int i = 0; i < genes.length; i++) {
      if (genes[i] == target.charAt(i)) {
        score++;
      }
    }
    // fitness are measured in percentage! 
    fitness = float(score) / target.length();
  }
  
  // crossover myself's DNA to my partners'.
  DNA crossover(DNA partner) {
    DNA child = new DNA();
    int midpoint = int(random(genes.length));
    for (int i = 0; i < genes.length; i++) {
      if (i > midpoint) child.genes[i] = genes[i];
      else              child.genes[i] = partner.genes[i];
    }
    return child;
  }
  
  void mutate(float mutationRate) {
    for (int i = 0; i < genes.length; i++) {
      if (random(1) < mutationRate) {
        genes[i] = (char)random(32, 128);
      }
    }
  }
  
  String getPhrase() {
    return new String(genes); // convert from char[] to string type.
  }
}