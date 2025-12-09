<template>
  <div class="auth-container">
    <h1>Register</h1>
    <form @submit.prevent>
      <div class="form-group">
        <label>Full Name</label>
        <input type="text" placeholder="John Doe" />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input type="email" placeholder="email@example.com" />
      </div>
      <div class="form-group">
        <label>Password</label>
        <input type="password" placeholder="********" />
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

p {
  text-align: center;
  margin-top: 1rem;
  font-size: 0.9rem;
}
</style>
