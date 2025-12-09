<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const fullName = ref('')
const email = ref('')
const password = ref('')

const handleRegister = () => {
  authStore.register(email.value, password.value, fullName.value)
}
</script>

<template>
  <div class="auth-container">
    <h1>Register</h1>
    <form @submit.prevent="handleRegister">
      <div v-if="authStore.authError" class="error-msg">{{ authStore.authError }}</div>
      <div class="form-group">
        <label>Full Name</label>
        <input v-model="fullName" type="text" placeholder="John Doe" required />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input v-model="email" type="email" placeholder="email@example.com" required />
      </div>
      <div class="form-group">
        <label>Password</label>
        <input v-model="password" type="password" placeholder="********" required />
      </div>
      <button type="submit">Sign Up</button>
    </form>
    <p>Already have an account? <router-link to="/login">Login</router-link></p>
  </div>
</template>

<style scoped>
/* Reuse styles from Login (or move to global component later) */
.auth-container {
  max-width: 400px;
  margin: 4rem auto;
  padding: 2rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

h1 {
  text-align: center;
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

.form-group input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 1rem;
  background-color: var(--color-primary);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  font-weight: 600;
}

button:hover {
  background-color: var(--color-primary-dark);
}

.error-msg {
  color: #721c24;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
  margin-bottom: 1rem;
}
</style>
