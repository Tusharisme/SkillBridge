<template>
  <div class="about">
    <div class="hero">
      <h1>About SkillBridge</h1>
      <p>Empowering the world to share knowledge, one skill at a time.</p>
    </div>
    
    <div class="content">
      <section>
        <h2>Our Mission</h2>
        <p>SkillBridge is a community-driven platform designed to connect passionate teachers with eager learners. We believe everyone has a skill worth sharing and something new to learn.</p>
      </section>

      <section>
        <h2>How It Works</h2>
        <div class="steps">
          <div class="step">
            <h3>1. Teach</h3>
            <p>Create a listing for your skill. Set your own terms and share your expertise.</p>
          </div>
          <div class="step">
            <h3>2. Learn</h3>
            <p>Browse a diverse catalog of skills. Connect with instructors directly.</p>
          </div>
          <div class="step">
            <h3>3. Grow</h3>
            <p>Expand your horizons, meet new people, and master new crafts.</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.about {
  max-width: 800px;
  margin: 0 auto;
}

.hero {
  text-align: center;
  padding: 4rem 1rem;
  background: linear-gradient(135deg, #6e8efb, #a777e3);
  color: white;
  border-radius: 0 0 16px 16px;
  margin-bottom: 3rem;
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.content {
  padding: 0 2rem 4rem;
}

section {
  margin-bottom: 3rem;
}

h2 {
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  color: var(--color-heading);
}

.steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}

.step {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.step h3 {
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}
</style>
