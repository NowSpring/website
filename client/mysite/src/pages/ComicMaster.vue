<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService.js';

const userPinia = userStore();

const headers = ref([
  {
    title: '',
    align: 'start',
    sortable: false,
    value: 'cover',
    width: 100,
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
    width: 100,
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

const meta = 'master';
const nextLink = 'comicversion';

const comicMasters = ref([]);

const getComic = async (meta: string) => {
  try {
    const response = await EventService.getComic(meta);
    comicMasters.value = response.data;
    console.log('comicMasters.value:', comicMasters.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

const reviewMasters = ref([]);

const getReviewMaster = async (id: string) => {
  try {
    const response = await EventService.getReviewMaster(id);
    reviewMasters.value = response.data;
    // console.log('reviewMaster.value:', reviewMasters.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

const comicsWithReviews = computed(() =>
  comicMasters.value.map((comic) => {
    const review = reviewMasters.value.find(
      (review) => review.comicMaster === comic.id,
    );
    return { ...comic, hasReview: review !== undefined };
  }),
);

onMounted(async () => {
  const token = localStorage.getItem('token');
  if (token !== null) {
    await getComic(meta);
    await getReviewMaster(userPinia.id);
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
</template>
