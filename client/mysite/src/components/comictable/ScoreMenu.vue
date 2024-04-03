<script setup lang="ts">
import { onMounted, inject } from 'vue';

const props = defineProps({
  rawLabel: String,
  title: String, // タイトルを渡すためのプロパティ
});

const datas = inject('datas');

const location = 'end';
const { rawLabel } = props;

onMounted(() => {
  console.log('datas.value:', datas.value);
  // console.log(headers.value); // headersの中身をコンソールに出力
});
</script>

<template>
  <div class="text-center">
    <v-menu :location="location">
      <template v-slot:activator="{ props }">
        <v-btn icon="mdi-information" elevation="0" dark v-bind="props">
        </v-btn>
      </template>

      <v-card max-width="300px">
        <v-card-title>{{ rawLabel }}</v-card-title>
        <div v-for="data in datas">
          <v-row>
            <v-col cols="6">
              {{ data.title }}
            </v-col>
            <v-col cols="6">
              {{ data.era }}
            </v-col>
          </v-row>
        </div>
      </v-card>
    </v-menu>
  </div>
</template>
