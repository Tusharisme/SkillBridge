<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useSkillStore } from '../stores/skills'

const route = useRoute()
const skillStore = useSkillStore()
const form = ref({
  name: '',
  description: ''
})

onMounted(async () => {
  await skillStore.fetchSkill(route.params.id)
  if (skillStore.currentSkill) {
    form.value.name = skillStore.currentSkill.name
    form.value.description = skillStore.currentSkill.description
  }
})

const handleSubmit = () => {
  skillStore.updateSkill(route.params.id, form.value)
}
</script>

<template>
  <div class="create-skill">
    <h1>Edit Skill</h1>
    <div v-if="skillStore.loading && !form.name" class="loading">Loading...</div>
    <form v-else @submit.prevent="handleSubmit">
      <div class="form-group">
        <label>Skill Name</label>
        <input v-model="form.name" type="text" placeholder="e.g. Advanced Pottery" required />
      </div>
      <div class="form-group">
        <label>Description</label>
        <textarea v-model="form.description" rows="5" placeholder="Describe what you will teach..." required></textarea>
      </div>
      <div class="actions">
        <button type="submit" class="btn-submit" :disabled="skillStore.loading">
          {{ skillStore.loading ? 'Saving...' : 'Save Changes' }}
        </button>
        <router-link to="/dashboard" class="btn-cancel">Cancel</router-link>
      </div>
    </form>
  </div>
</template>

<style scoped>
.create-skill {
  max-width: 600px;
  margin: 3rem auto;
  padding: 2rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

h1 {
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

input, textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
}

.actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.btn-submit {
  padding: 1rem 2rem;
  background-color: var(--color-primary);
  color: white;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}

.btn-submit:disabled {
  opacity: 0.7;
}

.btn-cancel {
  color: #666;
  text-decoration: none;
}
</style>
