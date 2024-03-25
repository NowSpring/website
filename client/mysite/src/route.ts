import { createRouter, createWebHistory } from 'vue-router';
import Test01 from '@/tests/pages/Test01.vue';
import Test02 from '@/tests/pages/Test02.vue';
import Dialog from '@/tests/pages/index.vue';
import Login from '@/pages/Login.vue';
import Signup from '@/pages/Signup.vue';
import Home from '@/pages/Home.vue';
import ComicMaster from '@/pages/ComicMaster.vue';

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
      {
        path: 'dialog',
        name: 'dialog',
        component: Dialog,
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
  {
    path: '/comicmaster',
    name: 'comicmaster',
    component: ComicMaster,
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
