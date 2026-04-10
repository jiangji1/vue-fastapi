import { defineStore } from 'pinia'

type TokenPayload = {
  access_token: string
  token_type: string
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('access_token') ?? '',
  }),
  getters: {
    isAuthed: (s) => Boolean(s.token),
  },
  actions: {
    setToken(token: string) {
      this.token = token
      localStorage.setItem('access_token', token)
    },
    clear() {
      this.token = ''
      localStorage.removeItem('access_token')
    },
    async login(username: string, password: string) {
      const body = new URLSearchParams()
      body.set('username', username)
      body.set('password', password)

      const res = await fetch('/api/auth/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body,
      })
      if (!res.ok) {
        throw new Error('登录失败')
      }
      const data = (await res.json()) as TokenPayload
      this.setToken(data.access_token)
    },
  },
})

