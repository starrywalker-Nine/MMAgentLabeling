import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/',
  plugins: [react()],
  reactStrictMode: true,
  transpileDependencies: true,
  lintOnSave: false,
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "./src/styles/sassConfig.scss";`
      }
    }
  }
})

