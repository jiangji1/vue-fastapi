import { createRouter, createWebHistory } from 'vue-router'

import { useAuthStore } from '../stores/auth'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/home' },
    { path: '/login', component: LoginView, meta: { public: true } },
    { path: '/home', component: HomeView },
  ],
})

router.beforeEach((to) => {
  const auth = useAuthStore()
  if (to.meta.public) return true
  if (auth.isAuthed) return true
  return { path: '/login', query: { redirect: to.fullPath } }
})

