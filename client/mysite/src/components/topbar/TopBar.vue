<script setup>
import { useRouter } from 'vue-router';
import { userStore } from '@/stores/user';

const router = useRouter();
const userPinia = userStore();

const logOut = () => {
  window.localStorage.removeItem('token');
  router.push({ name: 'login' });
};
</script>
<template>
  <v-app-bar app clippedLeft :height="60" color="primary">
    <v-btn icon @click="() => $router.push({ name: 'home' })">
      <v-icon x-large> mdi-home </v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn text @click="() => $router.push({ name: 'home' })">
      <span>{{ userPinia.username }}</span>
      <v-icon>mdi-account</v-icon>
    </v-btn>

    <v-btn text @click="logOut">
      <span class="mr-2"> Logout </span>
      <v-icon> mdi-open-in-new </v-icon>
    </v-btn>
  </v-app-bar>
</template>
