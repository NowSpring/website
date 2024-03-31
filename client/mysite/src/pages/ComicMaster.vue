<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService.js';
import { provide } from 'vue';

const userPinia = userStore();

const headers = ref([
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
]);

const nextLink = 'version';

const comicMasters = ref([]);

const getComicMasters = async () => {
  try {
    const response = await EventService.getComicMasters();
    comicMasters.value = response.data;
    // console.log('comicMasters.value:', comicMasters.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

const reviewMasters = ref([]);

const getReviewMasters = async () => {
  try {
    const response = await EventService.getReviewMasters(userPinia.id);
    reviewMasters.value = response.data;
    // console.log('reviewMaster.value:', reviewMasters.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

const comicsWithReviews = computed(() =>
  comicMasters.value.map((comic) => {
    const review = reviewMasters.value.find(
      (review) => review.comicID === comic.id,
    );
    return { ...comic, review: review || null };
  }),
);

onMounted(async () => {
  const token = localStorage.getItem('token');
  if (token !== null) {
    await getComicMasters();
    await getReviewMasters();
  }
});
</script>
<template>
  <ComicTable
    :datas="comicsWithReviews"
    :headers="headers"
    :nextLink="nextLink"
  >
  </ComicTable>
  <router-view></router-view>
</template>
