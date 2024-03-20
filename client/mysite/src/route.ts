import { createRouter, createWebHistory } from 'vue-router';
import Test01 from '@/pages/tests/Test01.vue';
import Test02 from '@/pages/tests/Test02.vue';
import Login from '@/pages/Login.vue';
import Signup from '@/pages/Signup.vue';
import Home from '@/pages/Home.vue';

const routes = [
  {
    path: '/tests',
    children: [
      {
        path: '01',
        name: 'test01',
        component: Test01,
      },
      {
        path: '02',
        name: 'test02',
        component: Test02,
      },
    ],
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup,
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
