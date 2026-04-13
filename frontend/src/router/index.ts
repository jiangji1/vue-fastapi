import { createRouter, createWebHistory } from 'vue-router'

import { useAuthStore } from '../stores/auth'

// 路由懒加载 - 只在需要时才加载对应的组件
const LoginView = () => import('../views/LoginView.vue')
const HomeView = () => import('../views/HomeView.vue')

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

