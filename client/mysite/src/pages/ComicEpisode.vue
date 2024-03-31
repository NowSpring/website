<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService.js';

const route = useRoute();
const userPinia = userStore();
const includeId = computed(() => route.params.id);
console.log('includeID:', includeId);

const headers = ref([
  {
    title: '',
    value: 'cover',
    align: 'start',
    sortable: false,
    width: '100px',
  },
  {
    title: '話数',
    value: 'episode',
    align: 'end',
    sortable: true,
    width: '100px',
  },
  {
    title: '',
    value: 'review',
    width: '100px',
  },
]);

const nextLink = 'pdf';

const comicEpisodes = ref([]);

const getComicEpisodes = async () => {
  try {
    const response = await EventService.getComicEpisodes(includeId.value);
    comicEpisodes.value = response.data;
    console.log('comicEpisodes.value:', comicEpisodes.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

onMounted(async () => {
  const token = localStorage.getItem('token');
  if (token !== null) {
    await getComicEpisodes();
  }
});
</script>
<template>
  <ComicTable :datas="comicEpisodes" :headers="headers" :nextLink="nextLink">
  </ComicTable>
</template>
