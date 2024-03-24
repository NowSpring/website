<template>
  <div>
    <v-card class="ma-auto pa-4" max-width="400" tile>
      <v-card-title>
        Profile
        <ProfileEditDialog :initial-data="profile" @submitted="submitted" />
      </v-card-title>
      <v-divider></v-divider>
      <v-card-subtitle class="pb-1 font-weight-bold">名前</v-card-subtitle>
      <v-card-text class="pt-0 pb-1">
        {{ profile.lastName + ' ' + profile.firstName }}
      </v-card-text>
      <v-card-subtitle class="pt-0 pb-1 font-weight-bold"
        >電話番号</v-card-subtitle
      >
      <v-card-text class="pt-0 pb-1">
        {{ profile.contact.phoneNumber }}
      </v-card-text>
      <v-card-subtitle class="pt-0 pb-1 font-weight-bold"
        >メールアドレス</v-card-subtitle
      >
      <v-card-text class="pt-0 pb-1">
        {{ profile.contact.mail }}
      </v-card-text>
      <template
        v-for="(address, index) in profile.addresses"
        :key="`address-${index}`"
      >
        <v-card-subtitle class="pt-0 pb-1 font-weight-bold">
          住所{{ index + 1 }}
        </v-card-subtitle>
        <v-card-text class="pt-0 pb-1">
          {{
            address.prefacture +
            address.municpality +
            address.blockNumber +
            address.building
          }}
        </v-card-text>
      </template>
    </v-card>
  </div>
</template>

<script setup lang="ts">
import { reactive, toRefs } from 'vue';
import Profile from '@/tests/domain/Profile';
import ProfileEditDialog from './ProfileEditDialog.vue';
import type { PropType } from 'vue';

// props を定義します
const props = defineProps({
  initialData: {
    type: Object as PropType<Profile>,
    required: true,
  },
});

// state を reactive オブジェクトとして定義します
const state = reactive({
  profile: props.initialData,
});

// submitted イベントハンドラーを定義します
const submitted = (updatedProfile: Profile) => {
  state.profile = updatedProfile;
};

// state をテンプレートで使用するために展開します
const { profile } = toRefs(state);
</script>
