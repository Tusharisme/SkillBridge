<script setup>
import { ref } from 'vue'

const featuredSkills = ref([
  { id: 1, title: 'Learn Python', instructor: 'Alice', image: 'https://via.placeholder.com/300x200?text=Python' },
  { id: 2, title: 'Master Vue.js', instructor: 'Bob', image: 'https://via.placeholder.com/300x200?text=Vue.js' },
  { id: 3, title: 'Digital Marketing', instructor: 'Charlie', image: 'https://via.placeholder.com/300x200?text=Marketing' },
])
</script>

<template>
  <div class="home">
    <section class="hero">
      <h1>Unlock Your Potential with <span class="highlight">SkillBridge</span></h1>
      <p>Connect with experts and master new skills today.</p>
      <router-link to="/register" class="cta-button">Get Started</router-link>
    </section>

    <section class="featured">
      <h2>Featured Skills</h2>
      <div class="skills-grid">
        <div v-for="skill in featuredSkills" :key="skill.id" class="skill-card">
          <img :src="skill.image" :alt="skill.title" />
          <div class="card-content">
            <h3>{{ skill.title }}</h3>
            <p>by {{ skill.instructor }}</p>
            <button>View Details</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.hero {
  text-align: center;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 0 0 50% 50% / 4%;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  font-weight: 800;
}

.highlight {
  color: var(--color-primary);
}

.cta-button {
  display: inline-block;
  margin-top: 1.5rem;
  padding: 0.8rem 2rem;
  background-color: var(--color-primary);
  color: white;
  text-decoration: none;
  border-radius: 30px;
  font-weight: 600;
  transition: transform 0.2s;
}

.cta-button:hover {
  transform: translateY(-2px);
  background-color: var(--color-primary-dark);
}

.featured {
  padding: 4rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.featured h2 {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.skill-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  transition: transform 0.3s;
}

.skill-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 15px rgba(0,0,0,0.1);
}

.skill-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-content {
  padding: 1.5rem;
}

.card-content h3 {
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.card-content button {
  margin-top: 1rem;
  width: 100%;
  padding: 0.5rem;
  border: 1px solid var(--color-primary);
  color: var(--color-primary);
  background: transparent;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}

.card-content button:hover {
  background: var(--color-primary);
  color: white;
}
</style>
