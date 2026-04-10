<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'

import { http } from '../lib/http'
import { useAuthStore } from '../stores/auth'

const auth = useAuthStore()
const me = ref<{ id: number; username: string; is_active: boolean; is_superuser: boolean } | null>(null)
const loading = ref(false)
const errorMsg = ref('')

const roleText = computed(() => (me.value?.is_superuser ? '管理员' : '普通用户'))

async function loadMe() {
  errorMsg.value = ''
  loading.value = true
  try {
    const res = await http.get('/api/users/me')
    me.value = res.data
  } catch (e) {
    errorMsg.value = '加载当前用户失败（可能 token 失效）'
  } finally {
    loading.value = false
  }
}

onMounted(loadMe)

// token 被清空时，路由守卫会把用户带回登录页
watch(
  () => auth.isAuthed,
  (v) => {
    if (!v) {
      location.href = '/login'
    }
  },
)
</script>

<template>
  <div class="layout">
    <el-header class="header">
      <div class="left">f1 管理后台</div>
      <div class="right">
        <el-button size="small" @click="loadMe" :loading="loading">刷新</el-button>
        <el-button size="small" type="danger" @click="auth.clear()">退出</el-button>
      </div>
    </el-header>

    <el-main class="main">
      <el-card>
        <template #header>当前登录信息</template>
        <el-alert v-if="errorMsg" :title="errorMsg" type="error" show-icon class="mb" />
        <div v-if="me">
          <div><b>用户：</b>{{ me.username }}</div>
          <div><b>角色：</b>{{ roleText }}</div>
          <div><b>ID：</b>{{ me.id }}</div>
        </div>
        <div v-else>暂无数据</div>
      </el-card>
    </el-main>
  </div>
</template>

<style scoped>
.layout {
  min-height: 100vh;
}
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #ebeef5;
  background: #fff;
}
.main {
  padding: 16px;
  background: #f5f7fa;
}
.mb {
  margin-bottom: 12px;
}
</style>

