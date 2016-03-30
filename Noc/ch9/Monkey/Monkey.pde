float mutationRate;
int totalPopulation = 150;

DNA[] population;
ArrayList<DNA> matingPool;                // for sexual intercourse
String target;                            // the target string. the famous one by shakespere

void setup() {
  size(200,200);
  target = "to be or not to be";
  mutationRate = 0.01;
  // step 1: init the population. each DNA has a random sentences. fill
  // these DNAs into population.
  population = new DNA[totalPopulation];
  for (int i = 0; i < population.length; i++) {
    population[i] = new DNA();
  }
}

void draw() {
  for (int i = 0; i < population.length; i++) {
    // step 2a: for each DNA obj, calc its firness.
    population[i].fitness();   // (fitness are measured in percentage.)
  }
    // step 2b: create mating pool
  ArrayList<DNA> matingPool = new ArrayList<DNA>(); 
    
  // step: fill in the mating pool 
  // according to nature selection law, the one who have a higher fitness
  // will have more copies in matingPool. 
  for (int i = 0; i < population.length; i++) {
    int n = int(population[i].fitness * 100);
    for (int j = 0; j < n; j++) {
      matingPool.add(population[i]);
    }
  }
    
  // step: crossover
  // replace everyone in polulation with a child.
  // the child can produce like this: randomly choose two in the mating pool,
  // cut somewhere for the first one, and pill up from the second one. then child
  // is done!
  for (int i = 0; i < population.length; i++) {
    int a = int(random(matingPool.size()));
    int b = int(random(matingPool.size()));
    DNA partnerA = matingPool.get(a);
    DNA partnerB = matingPool.get(b);
    DNA child = partnerA.crossover(partnerB);
    child.mutate(mutationRate);
    population[i] = child;
  }
}