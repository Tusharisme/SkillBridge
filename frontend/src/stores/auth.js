import { defineStore } from 'pinia'
import axios from 'axios'
import router from '../router'

const API_URL = 'http://localhost:5000'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
    authError: null
  }),
  getters: {
    isAuthenticated: (state) => !!state.token
  },
  actions: {
    async login(email, password) {
      this.authError = null
      try {
        const response = await axios.post(`${API_URL}/login`, {
          email,
          password
        }, {
          headers: { 'Content-Type': 'application/json' }
        })
        
        // Flask-Security returns proper JSON with auth_token
        const token = response.data.response.user.authentication_token
        const user = response.data.response.user
        
        this.token = token
        this.user = user
        localStorage.setItem('token', token)
        
        // Set default axios header
        axios.defaults.headers.common['Authentication-Token'] = token
        
        router.push('/')
      } catch (error) {
        this.authError = error.response?.data?.response?.errors?.[0] || 'Login failed'
        console.error("Login Error:", error)
      }
    },
    
    async register(email, password, fullName) {
      this.authError = null
      try {
        await axios.post(`${API_URL}/register`, {
          email,
          password,
          full_name: fullName
        })
        // Auto login or redirect to login
        router.push('/login')
      } catch (error) {
         this.authError = error.response?.data?.response?.errors?.[0] || 'Registration failed'
      }
    },

    logout() {
      this.token = null
      this.user = null
      localStorage.removeItem('token')
      delete axios.defaults.headers.common['Authentication-Token']
      router.push('/login')
    }
  }
})
