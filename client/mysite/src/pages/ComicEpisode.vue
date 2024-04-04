<script setup lang="ts">
import { ref, computed, onMounted, provide } from 'vue';
import { useRoute } from 'vue-router';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService.js';

const route = useRoute();
const includeId = computed(() => route.params.id);
const userPinia = userStore();

const currentLink = 'episode';
const nextLink = 'pdf';

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

const comicEpisodes = ref([]);

const getComicEpisodes = async () => {
  try {
    const response = await EventService.getComicReview(currentLink, {
      member_id: userPinia.id,
      include_id: includeId.value,
    });
    comicEpisodes.value = response.data;
    console.log('comicEpisodes.value:', comicEpisodes.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

onMounted(async () => {
  await getComicEpisodes();
});

provide('datas', comicEpisodes);
provide('headers', headers);
provide('currentLink', currentLink);
provide('nextLink', nextLink);
</script>
<template>
  <ComicTable> </ComicTable>
</template>
