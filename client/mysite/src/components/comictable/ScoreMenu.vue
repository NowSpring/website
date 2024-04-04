<script setup lang="ts">
import { ref, computed, onMounted, inject } from 'vue';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService.js';

const userPinia = userStore();

const props = defineProps({
  rawLabel: String,
  title: String, // タイトルを渡すためのプロパティ
});

// const datas = inject('datas');
const location = 'end';
const { rawLabel } = props;
const comic = ref([]);
const currentLink = inject('currentLink');

const getComic = async () => {
  try {
    const response = await EventService.getComicReview(currentLink, {
      member_id: userPinia.id,
    });
    comic.value = response.data;
  } catch (error) {
    console.log('error:' + error);
  }
};
const filteredDatas = computed(() => {
  return comic.value.filter((data) => data.review !== null);
});

const hover = ref(false);

onMounted(async () => {
  await getComic();
  // console.log('datas.value:', datas.value);
  // console.log(headers.value); // headersの中身をコンソールに出力
});
</script>

<template>
  <div class="text-center">
    <v-menu :location="location">
      <template v-slot:activator="{ props }">
        <v-btn icon="mdi-information" elevation="0" dark v-bind="props">
        </v-btn>
      </template>

      <v-card width="200px">
        <v-card-title>{{ '他作品の評価' }}</v-card-title>
        <div v-for="data in filteredDatas">
          <v-row>
            <v-col cols="6">
              <!-- {{ data.representation }} -->
              <div class="representation-container">
                <span @mouseover="hover = true" @mouseleave="hover = false">
                  {{ data.representation }}
                </span>
                <div v-if="hover" class="image-preview">
                  <img
                    :src="data.cover"
                    :alt="`Cover for ${data.representation}`"
                  />
                </div>
              </div>
            </v-col>
            <v-col cols="6">
              {{ data.review[rawLabel] }}
            </v-col>
          </v-row>
        </div>
      </v-card>
    </v-menu>
  </div>
</template>
<style scoped>
.representation-container {
  /* ここにスタイリングを追加 */
  position: relative;
}

.image-preview {
  display: block;
  position: fixed; /* 画像を画面の特定の位置に固定する */
  top: 100%; /* 画像を垂直方向の中央に配置 */
  left: 50%; /* 画像を水平方向の中央に配置 */
  transform: translate(-50%, -50%); /* 画像を正確に中央に配置するための調整 */
  z-index: 100; /* 他の要素より前面に表示 */
  border: 1px solid #ccc; /* 枠線を追加 (オプション) */
  background-color: white; /* 背景色を白に設定 (オプション) */
  padding: 10px; /* 内側の余白を設定 (オプション) */
}

.image-preview img {
  max-width: 50vw; /* ビューポート幅の90%を最大幅とする */
  max-height: 50vh; /* ビューポート高の90%を最大高さとする */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* 影を追加 (オプション) */
}
</style>
