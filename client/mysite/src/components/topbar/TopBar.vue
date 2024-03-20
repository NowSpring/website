<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();
const username = ref('');

onMounted(() => {
  username.value = window.localStorage.getItem('username');
});

const logOut = () => {
  window.localStorage.removeItem('token');
  window.localStorage.removeItem('user_id');
  window.localStorage.removeItem('username');
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
      <span>{{ username }}</span>
      <v-icon>mdi-account</v-icon>
    </v-btn>

    <v-btn text @click="logOut">
      <span class="mr-2"> Logout </span>
      <v-icon> mdi-open-in-new </v-icon>
    </v-btn>
  </v-app-bar>
</template>
