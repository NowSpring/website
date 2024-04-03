import { defineStore } from 'pinia';
import EventService from '@/plugins/EventService';

interface ComicMaster {
  id: string;
  title: string;
  author: string;
  era: string;
  publisher: string;
  target: string;
  genre: string;
  cover: string;
  review: Review;
  representation: string;
}

interface ComicClicked {
  id: string;
  review: Review;
  representation: string;
}

interface Review {
  id: string;
  scoreAlpha: number;
  scoreBeta: number;
  scoreCamma: number;
  scoreDelta: number;
  scoreEpsilon: number;
  comment: string | null;
  member: string;
  comicID: string;
}

export const comicMasterStore = defineStore('comicMaster', {
  state: (): { comics: ComicMaster[] } => ({
    comics: [],
  }),
  actions: {
    async fetchComics(member_id: string) {
      try {
        const response = await EventService.getComicMasters(member_id);
        this.comics = response.data as ComicMaster[];
        console.log('Comics fetched successfully:', this.comics);
      } catch (error) {
        console.error('Failed to fetch comics:', error);
      }
    },
  },
});

// export const comicClickedStore = defineStore('comicClicked', {
//   state: (): { comics: ComicClicked[] } => ({
//     comics: [],
//   }),
//   actions: {
//     async fetchComics() {
//       try {
//         const response = await EventService.getComicMasters();
//         this.comics = response.data as ComicMaster[];
//         console.log('Comics fetched successfully:', this.comics);
//       } catch (error) {
//         console.error('Failed to fetch comics:', error);
//       }
//     },
//   },
// });
