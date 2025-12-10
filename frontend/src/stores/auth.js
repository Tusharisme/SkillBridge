import { defineStore } from 'pinia'
import axios from 'axios'
import router from '../router'

const API_URL = (import.meta.env.VITE_API_URL || 'http://localhost:5000').replace(/\/+$/, '')

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
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
        const response = await axios.post(`${API_URL}/api/login`, {
          email,
          password
        }, {
          headers: { 'Content-Type': 'application/json' }
        })
        
        // Custom API returns response.user.authentication_token
        const data = response.data.response
        const token = data.user.authentication_token
        const user = data.user
        
        if (!token || token === 'undefined' || token === 'null') {
             throw new Error("Invalid token received from server")
        }
        
        this.token = token
        this.user = user
        localStorage.setItem('token', token)
        localStorage.setItem('user', JSON.stringify(user))
        
        // Set default axios header
        axios.defaults.headers.common['Authentication-Token'] = token
        
        router.push('/')
      } catch (error) {
        this.authError = error.response?.data?.response?.errors?.[0] || error.message || 'Login failed'
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
      localStorage.removeItem('user')
      delete axios.defaults.headers.common['Authentication-Token']
      router.push('/login')
    }
  }
})
