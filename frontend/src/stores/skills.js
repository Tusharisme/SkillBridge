import { defineStore } from 'pinia'
import axios from 'axios'
import router from '../router'

const API_URL = (import.meta.env.VITE_API_URL || 'http://localhost:5000') + '/api'

export const useSkillStore = defineStore('skills', {
  state: () => ({
    skills: [],
    currentSkill: null,
    dashboardData: null,
    loading: false,
    error: null
  }),
  actions: {
    async fetchSkills() {
      this.loading = true
      try {
        const response = await axios.get(`${API_URL}/skills`)
        this.skills = response.data
      } catch (err) {
        this.error = 'Failed to fetch skills'
      } finally {
        this.loading = false
      }
    },
    
    async fetchSkill(id) {
      this.loading = true
      try {
        const response = await axios.get(`${API_URL}/skills/${id}`)
        this.currentSkill = response.data
      } catch (err) {
        this.error = 'Failed to fetch skill details'
      } finally {
        this.loading = false
      }
    },

    async createSkill(skillData) {
      this.loading = true
      try {
        await axios.post(`${API_URL}/skills`, skillData)
        router.push('/dashboard')
      } catch (err) {
        this.error = 'Failed to create skill'
      } finally {
        this.loading = false
      }
    },
    
    async updateSkill(id, skillData) {
      this.loading = true
      try {
        await axios.put(`${API_URL}/skills/${id}`, skillData)
        router.push('/dashboard')
      } catch (err) {
        this.error = 'Failed to update skill'
      } finally {
        this.loading = false
      }
    },

    async deleteSkill(id) {
      if (!confirm('Are you sure you want to delete this skill?')) return
      
      this.loading = true
      try {
        await axios.delete(`${API_URL}/skills/${id}`)
        // Refresh dashboard
        await this.fetchDashboard()
      } catch (err) {
        alert('Failed to delete skill')
      } finally {
        this.loading = false
      }
    },

    async fetchDashboard() {
      this.loading = true
      try {
        const response = await axios.get(`${API_URL}/dashboard`)
        this.dashboardData = response.data
      } catch (err) {
        this.error = 'Failed to load dashboard'
      } finally {
        this.loading = false
      }
    },

    async bookSkill(skillId) {
      try {
        await axios.post(`${API_URL}/bookings`, { skill_id: skillId })
        alert('Booking request sent successfully!')
        router.push('/dashboard')
      } catch (err) {
        alert(err.response?.data?.error || 'Failed to book session')
      }
    },

    async fetchBookings() {
      try {
        const response = await axios.get(`${API_URL}/my-bookings`)
        return response.data
      } catch (err) {
        console.error('Failed to fetch bookings')
        return { as_student: [], as_instructor: [] }
      }
    }
  }
})
