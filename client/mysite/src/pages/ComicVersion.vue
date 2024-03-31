<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService.js';

const route = useRoute();
const userPinia = userStore();
const titleId = computed(() => route.params.id);
console.log(titleId);

const headers = ref([
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
]);

const nextLink = 'episode';

const comicVersions = ref([]);

const getComicVersions = async () => {
  try {
    const response = await EventService.getComicVersions(titleId.value);
    comicVersions.value = response.data;
    console.log('comicVersions.value:', comicVersions.value);
  } catch (error) {
    console.log('error:' + error);
  }
};

// const reviewVersions = ref([]);

// const getReviewVersions = async (id: string) => {
//   try {
//     const response = await EventService.getReviewVersions(id);
//     reviewVersions.value = response.data;
//     // console.log('reviewVersion.value:', reviewVersions.value);
//   } catch (error) {
//     console.log('error:' + error);
//   }
// };

// const comicsWithReviews = computed(() =>
//   comicVersions.value.map((comic) => {
//     const review = reviewVersions.value.find(
//       (review) => review.comicMaster === comic.id,
//     );
//     return { ...comic, hasReview: review !== undefined };
//   }),
// );

onMounted(async () => {
  const token = localStorage.getItem('token');
  if (token !== null) {
    await getComicVersions();
    // await getReviewVersions(userPinia.id);
  }
});
</script>
<template>
  <ComicTable :datas="comicVersions" :headers="headers" :nextLink="nextLink">
  </ComicTable>
</template>
