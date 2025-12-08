<template>
  <AppLayout>
    <div class="container mx-auto px-4 py-16">
      <div class="max-w-md mx-auto">
        <div class="card">
          <h1 class="text-2xl font-bold mb-2">Вход в систему</h1>
          <p class="text-dark-text-secondary mb-8">
            Введите ваши учетные данные для входа
          </p>
          
          <form @submit.prevent="handleLogin" class="space-y-6">
            <div>
              <label class="block text-dark-text-secondary mb-2">Email</label>
              <input
                v-model="email"
                type="email"
                required
                placeholder="ваш@email.com"
                class="input-dark w-full"
              />
            </div>
            
            <div>
              <label class="block text-dark-text-secondary mb-2">Пароль</label>
              <input
                v-model="password"
                type="password"
                required
                placeholder="Ваш пароль"
                class="input-dark w-full"
              />
            </div>
            
            <div v-if="authStore.error" class="p-4 bg-red-500/10 border border-red-500/30 rounded-lg">
              <p class="text-red-400">{{ authStore.error }}</p>
            </div>
            
            <button 
              type="submit" 
              class="btn-primary w-full"
              :disabled="authStore.loading"
            >
              <span v-if="authStore.loading">Вход...</span>
              <span v-else>Войти</span>
            </button>
          </form>
          
          <div class="mt-8 pt-6 border-t border-dark-card">
            <p class="text-dark-text-secondary text-center">
              Нет аккаунта? 
              <router-link to="/register" class="text-primary hover:underline">
                Зарегистрироваться
              </router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import AppLayout from '@/components/Layout/AppLayout.vue'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')

async function handleLogin() {
  try {
    await authStore.login(email.value, password.value)
    router.push('/dashboard')
  } catch (error) {
    console.error('Login failed:', error)
  }
}
</script>