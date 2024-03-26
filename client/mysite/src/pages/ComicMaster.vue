<script setup lang="ts">
import { useRoute } from 'vue-router';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService.js';
import TopBar from '@/components/topbar/TopBar.vue';
import ComicTable from '@/components/comictable/ComicTable.vue';

const route = useRoute();
const userPinia = userStore();
const isParentRoute = computed(() => route.name === 'comicmaster');

const comic_masters = ref([]);
const review_masters = ref([]);

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

const linkname = 'comicversion';

const getComicMaster = async () => {
  try {
    const response = await EventService.getComicMaster();
    comic_masters.value = response.data;
    console.log('comic_masters.value:', comic_masters.value);
  } catch (error) {
    console.log('Error_home' + error);
  }
};

const getReviewMaster = async (id: string) => {
  try {
    const response = await EventService.getReviewMaster(id);
    review_masters.value = response.data;
    // console.log('review_master.value:', review_masters.value);
  } catch (error) {
    console.log('Error_home' + error);
  }
};

const comicsWithReviews = computed(() =>
  comic_masters.value.map((comic) => {
    const review = review_masters.value.find(
      (review) => review.comic_master === comic.id,
    );
    return { ...comic, hasReview: review !== undefined };
  }),
);

onMounted(async () => {
  const token = localStorage.getItem('token');
  if (token !== null) {
    await getComicMaster();
    await getReviewMaster(userPinia.id);
  }
});
</script>
<template>
  <TopBar v-if="isParentRoute"></TopBar>
  <v-container v-if="isParentRoute">
    <ComicTable
      :datas="comicsWithReviews"
      :headers="headers"
      :linkname="linkname"
    >
    </ComicTable>
  </v-container>
  <router-view></router-view>
</template>
