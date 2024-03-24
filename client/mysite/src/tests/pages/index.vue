<template>
  <div>
    <ProfileCard :initial-data="profile" />
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue';
import Profile from '@/pages/tests/domain/Profile';
import ProfileCard from '../components/ProfileCard.vue';

const profile = reactive<Profile>({
  id: 1,
  firstName: '太郎',
  lastName: '山田',
  contact: {
    phoneNumber: '08011112222',
    mail: 'xxx@example.com',
  },
  addresses: [
    {
      id: 1,
      prefacture: '東京都',
      municpality: '新宿区',
      blockNumber: '新宿1-1-1',
      building: '新宿ビル1階',
    },
    {
      id: 2,
      prefacture: '東京都',
      municpality: '渋谷区',
      blockNumber: '渋谷2-2-2',
      building: '渋谷ビル2階',
    },
  ],
});
</script>
