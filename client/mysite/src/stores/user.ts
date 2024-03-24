import { defineStore } from 'pinia';
import CryptoJS from 'crypto-js';

export const userStore = defineStore(
  'user',
  () => {
    const id = ref('');
    const username = ref('');
    const email = ref('');
    function resetStore() {
      id.value = '';
      username.value = '';
      email.value = '';
    }
    return {
      id,
      username,
      email,
      resetStore,
    };
  },
  {
    persist: {
      storage: localStorage,
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
