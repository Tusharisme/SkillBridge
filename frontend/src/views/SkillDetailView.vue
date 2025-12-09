<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useSkillStore } from '../stores/skills'
import { useAuthStore } from '../stores/auth'

const route = useRoute()
const skillStore = useSkillStore()
const authStore = useAuthStore()

onMounted(() => {
  skillStore.fetchSkill(route.params.id)
})

const handleBooking = () => {
  if (!authStore.isAuthenticated) {
    alert('Please login to book a session')
    return
  }
  if (confirm('Are you sure you want to book this session?')) {
    skillStore.bookSkill(skillStore.currentSkill.id)
  }
}
</script>

<template>
  <div class="skill-detail">
    <div v-if="skillStore.loading" class="loading">Loading details...</div>
    <div v-else-if="skillStore.currentSkill" class="content">
      <div class="skill-header">
        <div class="header-content">
          <span class="badge">Course</span>
          <h1>{{ skillStore.currentSkill.name }}</h1>
          <p class="instructor">Taught by <strong>{{ skillStore.currentSkill.instructor }}</strong></p>
        </div>
      </div>
      
      <div class="skill-body">
        <div class="main-info">
          <h2>About this Skill</h2>
          <p class="description">{{ skillStore.currentSkill.description }}</p>
          
          <div class="meta">
            <p><strong>Created:</strong> {{ new Date(skillStore.currentSkill.created_at).toLocaleDateString() }}</p>
          </div>
        </div>
        
        <div class="sidebar">
          <div class="action-card">
            <h3>Interested?</h3>
            <p>Book a session with the instructor to start learning.</p>
            <button @click="handleBooking" class="btn-book">Book Session</button>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="error">
      <p>Skill not found.</p>
      <router-link to="/">Back to Home</router-link>
    </div>
  </div>
</template>

<style scoped>
.skill-detail {
  max-width: 1200px;
  margin: 0 auto;
  min-height: 80vh;
}

.skill-header {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 4rem 2rem;
  margin-bottom: 2rem;
}

.badge {
  background: var(--color-primary);
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
}

.skill-header h1 {
  font-size: 2.5rem;
  margin: 1rem 0;
}

.skill-body {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 3rem;
  padding: 0 2rem;
}

.description {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #4a5568;
  white-space: pre-line;
}

.sidebar .action-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  text-align: center;
}

.btn-book {
  display: block;
  width: 100%;
  margin-top: 1.5rem;
  padding: 1rem;
  background-color: var(--color-primary);
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  font-size: 1rem;
}

.btn-book:hover {
  background-color: var(--color-primary-dark);
}

@media (max-width: 768px) {
  .skill-body {
    grid-template-columns: 1fr;
  }
}
</style>
