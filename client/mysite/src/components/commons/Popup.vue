<template>
  <div class="overlay">
    <v-card :width="width">
      <v-row align-content="center">
        <v-col align="center">
          <v-card-title>
            <slot name="title"></slot>
          </v-card-title>

          <v-card-text>
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
