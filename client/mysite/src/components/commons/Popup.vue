<template>
  <div class="overlay">
    <v-card :width="width">
      <v-row align-content="center">
        <v-col align="center">
          <v-card-title>
            <slot name="title"></slot>
          </v-card-title>

          <v-card-text class="scrollable">
            <slot name="content"></slot>
          </v-card-text>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script setup lang="ts">
const width = inject('width', '400px');
</script>

<style>
/* スクロールバー用のスタイル */
.scrollable {
  max-height: 650px; /* ここでは300pxに設定していますが、必要に応じて調整してください */
  overflow-y: auto; /* 縦スクロールを有効にし、必要に応じてスクロールバーを表示 */
}
</style>
