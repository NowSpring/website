import { createRouter, createWebHistory, createWebHashHistory } from "vue-router";
import Login from "./pages/Login.vue";
import Home from "./pages/Home.vue";


const routes = [
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/",
    name: "home",
    component: Home,
  },
];

const useRouter = createRouter({
  history: process.env.IS_ELECTRON
    ? createWebHashHistory()
    : createWebHistory(),
  routes,
});

useRouter.beforeEach((to) => {
  if (to.meta.requiresAuth && window.localStorage.getItem("token") === null) {
    return { name: "login" };
  }
});

export default useRouter;