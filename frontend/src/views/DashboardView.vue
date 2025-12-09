<script setup>
import { onMounted, ref } from 'vue'
import { useSkillStore } from '../stores/skills'
import { useAuthStore } from '../stores/auth'

const skillStore = useSkillStore()
const authStore = useAuthStore()
const bookings = ref({ as_student: [], as_instructor: [] })

onMounted(async () => {
  await skillStore.fetchDashboard()
  bookings.value = await skillStore.fetchBookings()
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
      <section class="section-block">
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

      <section class="section-block">
        <h2>My Bookings (As Student)</h2>
        <div v-if="bookings.as_student.length === 0" class="empty-state">
          <p>No active bookings.</p>
        </div>
        <ul v-else class="booking-list">
          <li v-for="booking in bookings.as_student" :key="booking.id">
            <strong>{{ booking.skill_name }}</strong> - {{ booking.status }} ({{ new Date(booking.created_at).toLocaleDateString() }})
          </li>
        </ul>
      </section>

      <section class="section-block">
        <h2>Booking Requests (As Instructor)</h2>
        <div v-if="bookings.as_instructor.length === 0" class="empty-state">
          <p>No booking requests received.</p>
        </div>
        <ul v-else class="booking-list">
          <li v-for="booking in bookings.as_instructor" :key="booking.id">
            Request from <strong>{{ booking.student_name }}</strong> for <strong>{{ booking.skill_name }}</strong> - {{ booking.status }}
          </li>
        </ul>
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

.section-block {
  margin-bottom: 2rem;
}

.section-block h2 {
  margin-bottom: 1rem;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 0.5rem;
}

.booking-list {
  list-style: none;
  padding: 0;
}

.booking-list li {
  padding: 1rem;
  background: white;
  border-radius: 6px;
  margin-bottom: 0.5rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  display: flex;
  justify-content: space-between;
}
</style>
