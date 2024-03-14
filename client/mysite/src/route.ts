import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/pages/Login/main.vue';
import Home from '@/pages/Home/main.vue';

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: { requiresAuth: true },
  },
];

const useRouter = createRouter({
  history: createWebHistory(),
  routes,
});

useRouter.beforeEach((to) => {
  if (to.meta.requiresAuth && window.localStorage.getItem('token') === null) {
    return { name: 'login' };
  }
});

export default useRouter;
