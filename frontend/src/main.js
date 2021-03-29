import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

// Kolla om .js på slutet
import router from './router.js'
import store from './store.js'

const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')

