<template>
  <div>
    <v-dialog v-model="editDialog" max-width="500">
      <!-- `v-slot:activator`のスロットを使用して、アクティベーターのイベントと属性を設定 -->
      <template v-slot:activator="{ on, attrs }">
        <!-- `v-bind="attrs"`で自動的に属性を適用し、`v-on="on"`でイベントリスナーを適用 -->
        <v-btn text rounded v-bind="attrs" v-on="on">
          <v-icon>mdi-pencil</v-icon>
          編集
        </v-btn>
      </template>
      <v-card class="ma-auto pa-4">
        <ProfileEditForm v-model="state.profile" />
        <v-card-actions>
          <v-btn color="primary" @click="submit">変更する</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import type { Profile } from '@/tests/domain/Profile';
import clone from 'just-clone';
import ProfileEditForm from './ProfileEditForm.vue';

const props = defineProps<{
  initialData: Profile;
}>();

const emit = defineEmits(['submitted']);

const editDialog = ref(false);
const close = () => (editDialog.value = false);
const state = reactive({
  profile: clone(props.initialData),
});

const submit = () => {
  emit('submitted', clone(state.profile));
  close();
};
</script>
