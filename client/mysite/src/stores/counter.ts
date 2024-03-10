import { defineStore } from 'pinia';

export const useStore = defineStore('counter', {
  state: (): { count: number } => ({
    count: 0,
  }),
  getters: {
    tenfold(): number {
      return this.count * 10;
    },
  },
  actions: {
    increment() {
      this.count++;
    },
  },
});
