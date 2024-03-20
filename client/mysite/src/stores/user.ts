import { defineStore } from 'pinia';

export const userStore = defineStore('user', () => {
  const username = ref('');
  const email = ref('');
});
