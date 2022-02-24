import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/search/:search_text',
    name: 'Search',
    component: () => import('../views/Search.vue')
  },
  {
    path: '/message-wall',
    name: 'Message-wall',
    component: () => import('../views/Message-wall.vue')
  },
  {
    path: '/:orderId(\\d+)',
    name: 'round_home',
    component: Home
  },
  {
    path: '/:orderId(\\d+)/player',
    name: 'Leaderboard',
    component: () => import('../views/leaderboard.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
