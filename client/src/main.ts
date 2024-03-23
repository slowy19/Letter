// src/main.js or src/main.ts
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axiosInstance from './utils/axios'; 

const app = createApp(App);

app.use(store);
app.use(router);
app.provide('axios', axiosInstance); 
app.mount('#app');
