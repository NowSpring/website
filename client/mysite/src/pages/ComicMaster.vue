<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { userStore } from '@/stores/user';
import { comicMasterStore } from '@/stores/comic.ts';
import EventService from '@/plugins/EventService.js';
import { provide } from 'vue';

const userPinia = userStore();
const comicMasterPinia = comicMasterStore();

const currentLink = 'master';
const nextLink = 'version';

const headers = [
  {
    title: '',
    align: 'start',
    sortable: false,
    value: 'cover',
    width: '100px',
  },
  {
    title: 'タイトル',
    value: 'title',
    sortable: true,
    width: 100,
  },
  {
    title: '作者',
    value: 'author',
    sortable: true,
    width: 100,
  },
  {
    title: '年代',
    value: 'era',
    sortable: true,
    width: '100px',
  },
  {
    title: '出版社',
    value: 'publisher',
    sortable: true,
    width: 100,
  },
  {
    title: '対象',
    value: 'target',
    sortable: true,
    width: 100,
  },
  {
    title: 'ジャンル',
    value: 'genre',
    sortable: true,
    width: 100,
  },
  {
    title: '',
    value: 'review',
    width: 100,
  },
];

const comicMasters = ref([]);

const getComicMasters = async () => {
  try {
    const response = await EventService.getComicMasters({
      member_id: userPinia.id,
    });
    comicMasters.value = response.data;
    console.log('comicMasters.value:', comicMasters.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

onMounted(async () => {
  comicMasterPinia.fetchComics(userPinia.id);
  await getComicMasters();
});

provide('datas', comicMasters);
provide('headers', headers);
provide('currentLink', currentLink);
provide('nextLink', nextLink);
</script>

<!-- <template>
  <ComicTable
    :datas="comicMasters"
    :headers="headers"
    :currentLink="currentLink"
    :nextLink="nextLink"
  >
  </ComicTable>
  <router-view></router-view>
</template> -->

<template>
  <ComicTable> </ComicTable>
</template>
