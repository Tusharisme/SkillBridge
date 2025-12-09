<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from './stores/auth'

const authStore = useAuthStore()
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/" class="logo">SkillBridge</RouterLink>
        <div class="nav-links">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">About</RouterLink>
          
          <template v-if="!authStore.isAuthenticated">
            <RouterLink to="/login" class="btn-login">Login</RouterLink>
          </template>
          
          <template v-else>
            <RouterLink to="/dashboard">Dashboard</RouterLink>
            <button @click="authStore.logout()" class="btn-logout">Logout</button>
          </template>
        </div>
      </nav>
    </div>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  padding: 1rem 2rem;
  background-color: var(--color-background-soft);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--color-heading);
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.nav-links a {
  text-decoration: none;
  color: var(--color-text);
  font-weight: 500;
}

.nav-links a:hover {
  color: var(--color-primary);
}

.nav-links a.router-link-active {
  color: var(--color-primary);
}

.btn-login {
  background-color: var(--color-primary);
  color: white !important;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn-login:hover {
  background-color: var(--color-primary-dark);
}

.btn-logout {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--color-text);
  font-weight: 500;
  font-size: 1rem;
}

.btn-logout:hover {
  color: var(--color-primary);
}
</style>
