import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import VueGoogleCharts from 'vue-google-charts'

Vue.use(VueGoogleCharts)
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
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/fighter',
    name: 'Fighter',
    component: () => import('../views/Fighter.vue')
  },
  {
    path: '/faction',
    name: 'Faction',
    component: () => import('../views/Faction.vue')
  },
  {
    path: '/weapon',
    name: 'Weapon',
    component: () => import('../views/Weapon.vue')
  },
  {
    path: '/report',
    name: 'Report',
    component: () => import('../views/Report.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
