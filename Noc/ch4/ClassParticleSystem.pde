import java.util.Iterator;

class ParticleSystem {
  ArrayList<Particle> particles;
  PVector origin;
  
  ParticleSystem(PVector location) {
    origin = location.get();
    particles = new ArrayList<Particle>();
  }

  void addParticle() {
    particles.add(new Particle(origin));
  }

  // apply force to the system, result is apply the 
  // same force to every particle in the sys.
  void applyForce(PVector f) {
    for (Particle p: particles) {
        p.applyForce(f);
    }
  }
  
  void applyRepeller(Repeller r) {
    for (Particle p: particles) {
      PVector force = r.repel(p);   // call r.repel(p) to calc force
      p.applyForce(force);
    }
  }
  
  void run() {
    Iterator<Particle> it = particles.iterator();
    while (it.hasNext()) {
      Particle p = (Particle)it.next();
      p.run();
      if (p.isDead()) {
        it.remove();
      }
    }
  }
}