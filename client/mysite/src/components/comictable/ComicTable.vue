<script setup lang="ts">
import { toRefs, onMounted, inject } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps({
  datas: Array,
  headers: Array,
  nextLink: String,
});

const { datas, headers, nextLink } = toRefs(props);

const clickRow = (item) => {
  if (nextLink.value !== 'pdf') {
    router.push({ name: nextLink.value, params: { id: item.id } });
  } else {
    window.open(item.pdf, '_blank');
  }
};

onMounted(() => {
  // console.log(datas.value)
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
                min-width="160px"
                class="ma-0 pa-0"
              ></v-img>
            </div>
          </span>
          <span v-if="header.value === 'title'">
            <div align="left">{{ item.title }}</div>
          </span>
          <span v-if="header.value === 'author'">
            <div align="left">{{ item.author }}</div>
          </span>
          <span v-if="header.value === 'era'">
            <div align="left">{{ item.era }}</div>
          </span>
          <span v-if="header.value === 'publisher'">
            <div align="left">{{ item.publisher }}</div>
          </span>
          <span v-if="header.value === 'target'">
            <div align="left">{{ item.target }}</div>
          </span>
          <span v-if="header.value === 'genre'">
            <div align="left">{{ item.genre }}</div>
          </span>
          <span v-if="header.value === 'version_number'">
            <div align="right">{{ item.version_number }}</div>
          </span>
          <span v-if="header.value === 'episode_number'">
            <div align="right">{{ item.episode_number }}</div>
          </span>
          <span v-if="header.value === 'review'">
            <ReviewDialog :hasReview="item.hasReview"></ReviewDialog>
          </span>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>
