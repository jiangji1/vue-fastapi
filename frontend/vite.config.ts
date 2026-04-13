import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  build: {
    // 构建前清空 dist 目录
    emptyOutDir: true,
    // 代码分割
    rollupOptions: {
      output: {
        // 手动分割 chunk
        manualChunks(id: string) {
          if (id.includes('node_modules')) {
            // Element Plus (必须在 vue 之前匹配)
            if (id.includes('element-plus') || id.includes('@element-plus')) {
              return 'element-plus'
            }
            // Vue 生态
            if (id.includes('vue') || id.includes('pinia')) {
              return 'vue-vendor'
            }
            // Axios
            if (id.includes('axios')) {
              return 'axios'
            }
          }
        },
      },
    },
    // chunk 大小警告限制
    chunkSizeWarningLimit: 1000,
  },
})
