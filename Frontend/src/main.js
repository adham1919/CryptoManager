import { createApp } from 'vue'
import App from './App.vue'
import  'bootstrap/dist/css/bootstrap.min.css'
import  'bootstrap'
import router from  './router'
import VueChartkick from 'vue-chartkick' 
import 'chartkick/chart.js'
const app = createApp(App)
app.use(VueChartkick)
app.use(router)
app.mount('#app')
