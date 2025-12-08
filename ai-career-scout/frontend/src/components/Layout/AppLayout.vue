<template>
  <div class="min-h-screen bg-dark-bg">
    <!-- Навигация -->
    <nav class="sticky top-0 z-50 border-b border-dark-card/50 bg-dark-bg/95 backdrop-blur">
      <div class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          <!-- Лого -->
          <router-link to="/" class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-primary rounded-lg flex items-center justify-center">
              <span class="text-dark-bg font-bold text-xl">AI</span>
            </div>
            <span class="text-xl font-bold text-dark-text">Career Scout</span>
          </router-link>
          
          <!-- Навигационные ссылки -->
          <div class="hidden md:flex items-center space-x-8">
            <router-link 
              v-for="item in navItems" 
              :key="item.to"
              :to="item.to"
              class="text-dark-text-secondary hover:text-primary transition-colors"
              active-class="text-primary"
            >
              {{ item.label }}
            </router-link>
          </div>
          
          <!-- Кнопки действий -->
          <div class="flex items-center space-x-4">
            <button @click="toggleLanguage" class="text-dark-text-secondary hover:text-primary">
              {{ currentLanguage === 'ru' ? 'EN' : 'RU' }}
            </button>
            <template v-if="isAuthenticated">
              <router-link to="/dashboard" class="btn-secondary">
                Кабинет
              </router-link>
            </template>
            <template v-else>
              <router-link to="/login" class="btn-secondary">
                Войти
              </router-link>
              <router-link to="/register" class="btn-primary">
                Начать
              </router-link>
            </template>
          </div>
        </div>
      </div>
    </nav>
    
    <!-- Основной контент -->
    <main class="min-h-[calc(100vh-80px)]">
      <slot />
    </main>
    
    <!-- Футер -->
    <footer class="border-t border-dark-card/50 py-8">
      <div class="container mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="mb-6 md:mb-0">
            <div class="flex items-center space-x-3 mb-4">
              <div class="w-8 h-8 bg-primary rounded-lg"></div>
              <span class="text-lg font-bold">AI Career Scout</span>
            </div>
            <p class="text-dark-text-secondary text-sm">
              Умный поиск работы с искусственным интеллектом
            </p>
          </div>
          
          <div class="flex space-x-6">
            <a href="#" class="text-dark-text-secondary hover:text-primary">Политика конфиденциальности</a>
            <a href="#" class="text-dark-text-secondary hover:text-primary">Условия использования</a>
            <a href="#" class="text-dark-text-secondary hover:text-primary">Контакты</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const currentLanguage = ref('ru')
const isAuthenticated = computed(() => authStore.isAuthenticated)

const navItems = [
  { to: '/', label: 'Главная' },
  { to: '/vacancies', label: 'Вакансии' },
  { to: '/tests', label: 'Тесты' },
  { to: '/resume', label: 'Резюме' },
  { to: '/faq', label: 'FAQ' },
  { to: '/pricing', label: 'Тарифы' }
]

const toggleLanguage = () => {
  currentLanguage.value = currentLanguage.value === 'ru' ? 'en' : 'ru'
}
</script>