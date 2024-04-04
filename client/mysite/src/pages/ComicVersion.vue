<script setup lang="ts">
import { ref, computed, onMounted, provide } from 'vue';
import { useRoute } from 'vue-router';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService.js';

const route = useRoute();
const titleId = computed(() => route.params.id);
const userPinia = userStore();

const currentLink = 'version';
const nextLink = 'episode';

const headers = [
  {
    title: '',
    value: 'cover',
    align: 'start',
    sortable: false,
    width: '100px',
  },
  {
    title: '巻数',
    value: 'version',
    align: 'end',
    sortable: true,
    width: '100px',
  },
  {
    title: '',
    value: 'review',
    width: '100px',
  },
];

const comicVersions = ref([]);

const getComicVersions = async () => {
  try {
    const response = await EventService.getComicReview(currentLink, {
      member_id: userPinia.id,
      title_id: titleId.value,
    });
    comicVersions.value = response.data;
    console.log('comicVersions.value:', comicVersions.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

onMounted(async () => {
  await getComicVersions();
});

provide('datas', comicVersions);
provide('headers', headers);
provide('currentLink', currentLink);
provide('nextLink', nextLink);
</script>

<template>
  <ComicTable> </ComicTable>
</template>
