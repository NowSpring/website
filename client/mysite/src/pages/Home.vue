<script setup lang="ts">
import { provide, ref } from 'vue';

const isSideBar = ref(true);
provide('isSideBar', isSideBar);
</script>

<template>
  <TopBar></TopBar>
  <SideBar></SideBar>
  <v-main>
    <v-container>
      <router-view />
    </v-container>
  </v-main>
</template>
