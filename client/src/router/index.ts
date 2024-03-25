import Chats from '@/views/Chats.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import Profile from '@/views/Profile.vue'
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import NotFound from '@/views/NotFound.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'chats',
    component: Chats
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/404', 
    name: 'NotFound',
    component: NotFound
  },
  {
    path: '/:catchAll(.*)', redirect:'404'
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
