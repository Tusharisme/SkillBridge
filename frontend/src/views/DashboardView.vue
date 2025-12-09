<script setup>
import { onMounted } from 'vue'
import { useSkillStore } from '../stores/skills'
import { useAuthStore } from '../stores/auth'

const skillStore = useSkillStore()
const authStore = useAuthStore()

onMounted(() => {
  skillStore.fetchDashboard()
})
</script>

<template>
  <div class="dashboard">
    <header class="dashboard-header">
      <h1>Welcome, {{ skillStore.dashboardData?.user?.full_name || 'User' }}</h1>
      <router-link to="/skills/create" class="btn-create">+ Create New Skill</router-link>
    </header>

    <div v-if="skillStore.loading" class="loading">Loading dashboard...</div>

    <div v-else class="dashboard-content">
      <section class="my-skills">
        <h2>My Skills</h2>
        <div v-if="skillStore.dashboardData?.my_skills?.length === 0" class="empty-state">
          <p>You haven't listed any skills yet.</p>
        </div>
        <div v-else class="skills-list">
          <div v-for="skill in skillStore.dashboardData?.my_skills" :key="skill.id" class="skill-item">
            <div class="skill-info">
              <h3>{{ skill.name }}</h3>
              <p>{{ skill.description }}</p>
            </div>
            <div class="skill-actions">
              <button>Edit</button>
              <button class="delete">Delete</button>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 3rem;
}

.btn-create {
  background-color: var(--color-primary);
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
}

.skills-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.skill-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.skill-info h3 {
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.skill-actions {
  display: flex;
  gap: 0.5rem;
}

button {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
}

button.delete {
  color: red;
  border-color: #ffdce0;
  background: #fff5f5;
}
</style>
