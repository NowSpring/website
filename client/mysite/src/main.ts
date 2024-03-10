import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useRouter } from './route'

import './style.css'
import App from './App.vue'

createApp(App)
  .use(createPinia())
  .use(useRouter)
  .mount('#app')
