<script setup lang="ts">
import { inject, Ref } from 'vue';
import { useRouter } from 'vue-router';
import { userStore } from '@/stores/user';

const router = useRouter();
const userPinia = userStore();

const isSideBar = inject<Ref<boolean>>('isSideBar');

const logOut = () => {
  window.localStorage.removeItem('token');
  window.localStorage.removeItem('user');
  userPinia.resetStore();
  router.push({ name: 'login' });
};
</script>
<template>
  <v-app-bar app clippedLeft :height="60" color="primary">
    <v-app-bar-nav-icon @click="isSideBar = !isSideBar" class="custom-nav-icon">
    </v-app-bar-nav-icon>
    <v-spacer></v-spacer>

    <ProfileDialog></ProfileDialog>

    <v-btn text @click="logOut">
      <span class="mr-2"> Logout </span>
      <v-icon> mdi-open-in-new </v-icon>
    </v-btn>
  </v-app-bar>
</template>

<style scoped>
.custom-nav-icon {
  position: relative;
  left: 15px;
}
</style>
