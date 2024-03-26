<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps({
  modelValue: Boolean,
  title: String, // タイトルを渡すためのプロパティ
});

const location = 'end';
</script>
<template>
  <div class="text-center">
    <v-menu :location="location">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" dark v-bind="props"> Dropdown </v-btn>
      </template>

      <v-card max-width="300px">
        <v-card-title>Hello</v-card-title>
        <v-card-text>ここに詳細情報を表示します。</v-card-text>
      </v-card>
    </v-menu>
  </div>
</template>
