<script setup lang="ts">
import { inject, Ref } from 'vue';

const isSideBar = inject<Ref<boolean>>('isSideBar');
</script>
<template>
  <v-navigation-drawer v-model="isSideBar" app dark clipped :width="100">
    <v-list nav dense>
      <v-list-item>
        <v-btn
          icon="mdi-book-open-variant"
          size="x-large"
          elevation="0"
          @click="() => $router.push({ name: 'master' })"
        >
        </v-btn>
      </v-list-item>

      <v-list-item>
        <v-btn
          icon="mdi-magnify"
          size="x-large"
          elevation="0"
          @click="() => $router.push({ name: 'master' })"
        ></v-btn>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
