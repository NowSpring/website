import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import tsconfigPaths from 'vite-tsconfig-paths';
import Components from 'unplugin-vue-components/vite';
import AutoImport from 'unplugin-auto-import/vite';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    Components(),
    AutoImport({
      imports: ['vue'],
    }),
    // tsconfigPaths(),
  ],
  resolve: {
    alias: {
      '@/': `${__dirname}/src/`,
    },
  },
  server: {
    host: true
  }
});
