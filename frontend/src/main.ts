import { createApp } from 'vue'
// Element Plus 已改为按需导入，无需在此引入

import App from './App.vue'
import { router } from './router'
import { pinia } from './stores'

import './style.css'

createApp(App).use(pinia).use(router).mount('#app')
