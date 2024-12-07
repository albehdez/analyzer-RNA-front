import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'
import Dialog from 'primevue/dialog'
import Dropdown from 'primevue/dropdown'

import 'primeicons/primeicons.css'

const app = createApp(App)
app.use(PrimeVue)
app.use(createPinia())
app.use(router)
app.component('Dialog', Dialog)
app.component('Dropdown', Dropdown)

app.mount('#app')
