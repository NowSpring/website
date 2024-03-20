import { defineStore } from 'pinia';
import CryptoJS from 'crypto-js';

export const userStore = defineStore(
  'user',
  () => {
    const username = ref('');
    const email = ref('');
    return {
      username,
      email,
    };
  },
  {
    persist: {
      storage: sessionStorage,
      serializer: {
        deserialize: (str) => {
          const decrypted = CryptoJS.AES.decrypt(str, 'user');
          const decryptedData = decrypted.toString(CryptoJS.enc.Utf8);
          return JSON.parse(decryptedData);
        },
        serialize: (state) => {
          return CryptoJS.AES.encrypt(JSON.stringify(state), 'user').toString();
        },
      },
    },
  },
);
