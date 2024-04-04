<script setup lang="ts">
import { ref, onMounted, provide, inject } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const datas = inject('datas');
const headers = inject('headers');
const nextLink = inject('nextLink');

const clickRow = (item) => {
  if (nextLink !== 'pdf') {
    router.push({ name: nextLink, params: { id: item.id } });
  } else {
    console.log('item.pdf:', item.pdf);
    window.open(item.pdf, '_blank');
  }
};

onMounted(() => {
  // console.log('datas.value:', datas.value);
  // console.log(headers.value); // headersの中身をコンソールに出力
});
</script>

<template>
  <v-data-table
    v-if="headers && datas"
    :headers="headers"
    :items="datas"
    :items-per-page="5"
    class="elevation-1 my-3 mx-auto"
    style="width: 100%"
  >
    <template v-slot:item="{ item }">
      <tr :key="item.key" @click="clickRow(item)">
        <td v-for="header in headers" :key="header.value">
          <span v-if="header.value === 'cover'">
            <div align="center">
              <v-img
                :src="item.cover"
                :aspect-ratio="16 / 9"
                height="9vw"
                min-height="100px"
                width="16vw"
                min-width="100px"
                class="ma-0 pa-0"
              ></v-img>
            </div>
          </span>
          <span v-if="header.value === 'title'">
            <div align="left" class="text-truncate" style="max-width: 100px">
              {{ item.title }}
            </div>
          </span>
          <span v-if="header.value === 'author'">
            <div align="left" class="text-truncate" style="max-width: 100px">
              {{ item.author }}
            </div>
          </span>
          <span v-if="header.value === 'era'">
            <div align="left" class="text-truncate" style="max-width: 50px">
              {{ item.era }}
            </div>
          </span>
          <span v-if="header.value === 'publisher'">
            <div align="left" class="text-truncate" style="max-width: 100px">
              {{ item.publisher }}
            </div>
          </span>
          <span v-if="header.value === 'target'">
            <div align="left" class="text-truncate" style="max-width: 50px">
              {{ item.target }}
            </div>
          </span>
          <span v-if="header.value === 'genre'">
            <div align="left">{{ item.genre }}</div>
          </span>
          <span v-if="header.value === 'version'">
            <div align="right">{{ item.version }}</div>
          </span>
          <span v-if="header.value === 'episode'">
            <div align="right">{{ item.episode }}</div>
          </span>
          <span v-if="header.value === 'review'">
            <ReviewDialog
              :review="item.review"
              :comicID="item.id"
              @review-updated="$emit('review-updated')"
            ></ReviewDialog>
          </span>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>
