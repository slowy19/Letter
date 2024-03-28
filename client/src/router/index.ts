import Chats from '@/views/Chats.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import NotFound from '@/views/NotFound.vue'
import Profile from '@/views/profile/Profile.vue'
import Photos from '@/views/profile/components/Photos.vue'
import Documents from '@/views/profile/components/Documents.vue'

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
    component: Profile,
    children: [
      {
        path: '', 
        component: Photos,
      },
      {
        path: 'docs', 
        component: Documents,
      },
    ],
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
