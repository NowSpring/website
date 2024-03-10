import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useRouter } from './route'

// Vuetify
import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css' 
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import './style.css'
import App from './App.vue'

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi', 
  },
})

createApp(App)
  .use(createPinia())
  .use(useRouter)
  .use(vuetify)
  .mount('#app')
