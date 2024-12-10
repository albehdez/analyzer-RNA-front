import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/analysis',
      name: 'analysis',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/help',
      name: 'help',
      component: () => import('../views/HelpView.vue'),
    },
    {
      path: '/advertise',
      name: 'advertise',
      component: () => import('../views/AddView.vue'),
    },
    {
      path: '/tendency',
      name: 'tendency',
      component: () => import('../views/TendencyView.vue'),
    },
  ],
})

export default router
