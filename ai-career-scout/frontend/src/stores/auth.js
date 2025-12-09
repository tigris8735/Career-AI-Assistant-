import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token'))
  const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))
  const loading = ref(false)
  const error = ref(null)

  const isAuthenticated = computed(() => !!token.value)

  // Конфигурация axios
  const api = axios.create({
    baseURL: 'http://localhost:8000/api/v1',
    headers: {
      'Content-Type': 'application/json'
    }
  })

  // Добавляем токен к запросам, если он есть
  if (token.value) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
  }

  async function login(email, password) {
    try {
      loading.value = true
      error.value = null
      
      const response = await api.post('/auth/login', {
        email,
        password
      })

      token.value = response.data.access_token
      localStorage.setItem('token', token.value)
      
      // Получаем информацию о пользователе
      api.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
      await fetchUser()
      
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка авторизации'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function register(userData) {
    try {
      loading.value = true
      error.value = null
      
      const response = await api.post('/auth/register', userData)
      
      // Автоматически логиним после регистрации
      await login(userData.email, userData.password)
      
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка регистрации'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function fetchUser() {
    try {
      const response = await api.get('/auth/me')
      user.value = response.data
      localStorage.setItem('user', JSON.stringify(user.value))
      return user.value
    } catch (err) {
      console.error('Failed to fetch user:', err)
      logout()
    }
  }

  function logout() {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    delete api.defaults.headers.common['Authorization']
  }

  return {
    token,
    user,
    loading,
    error,
    isAuthenticated,
    login,
    register,
    logout,
    fetchUser
  }
})