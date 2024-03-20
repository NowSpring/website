<template>
  <div class="overlay">
    <v-card width="400px" class="mx-auto mt-5">
      <v-card-title class="d-flex justify-center">
        <slot name="title"> </slot>
      </v-card-title>
      <v-card-text>
        <v-form>
          <slot name="content"></slot>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup lang="ts"></script>
