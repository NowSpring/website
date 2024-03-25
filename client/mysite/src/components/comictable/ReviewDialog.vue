<script setup lang="ts">
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService';
import { ref, reactive, computed, toRaw, provide } from 'vue';

const props = defineProps({
  hasReview: Boolean,
});

const width = '1000px';
provide('width', width);

const isDialog = ref(false);
const isEdit = ref(false);
const isValid = ref(false);
const isLoading = ref(false);
const formReference = ref(null);

const userPinia = userStore();
const formState = reactive({ ...userPinia.$state });

const fieldRules = reactive({
  required: (value: string) => !!value || 'This field is required.',
  email: (value: string) => {
    const pattern =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return pattern.test(value) || 'Invalid email address.';
  },
});

const canSubmit = computed(() => {
  return (
    isValid.value &&
    !(
      formState.username === userPinia.username &&
      formState.email === userPinia.email
    )
  );
});

const formReset = () => {
  Object.assign(formState, { ...userPinia.$state });
  isEdit.value = false;
};

const updateProfile = () => {
  const id = ref(userPinia.id);
  isLoading.value = true;
  EventService.updateProfile(id.value, toRaw(formState))
    .then((response) => {
      userPinia.username = response.data.username;
      userPinia.email = response.data.email;
      isLoading.value = !isLoading.value;
      isDialog.value = !isDialog.value;
      isEdit.value = !isEdit.value;
    })
    .catch((error) => {
      console.log('Error' + error);
    });
};
</script>

<template>
  <div class="pa-4 text-center">
    <v-dialog v-model="isDialog" max-width="100000">
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn depressed v-bind="activatorProps">
          <v-icon x-large :color="hasReview ? 'red' : 'grey'"
            >mdi-pencil</v-icon
          >
        </v-btn>
      </template>

      <Popup>
        <template v-slot:title>
          <h3 class="title font-weight-bold">Review</h3>
        </template>
        <template v-slot:content>
          <v-form ref="formReference" v-model="isValid">
            <v-row>
              <v-col col="8"></v-col>
              <v-col col="4">
                <v-text-field
                  label="UserName"
                  prepend-icon="mdi-account-circle"
                  v-model="formState.username"
                  :disabled="!isEdit"
                  :rules="[fieldRules.required]"
                />
                <v-text-field
                  type="email"
                  label="Email"
                  prepend-icon="mdi-email"
                  v-model="formState.email"
                  :disabled="!isEdit"
                  :rules="[fieldRules.required, fieldRules.email]"
                />
              </v-col>
            </v-row>
            <v-row></v-row>
            <v-row>
              <v-col>
                <v-btn
                  class="info"
                  color="primary"
                  :disabled="isEdit"
                  @click="isEdit = !isEdit"
                >
                  編集
                </v-btn>
                <v-btn
                  class="ml-4"
                  color="green"
                  :loading="isLoading"
                  :disabled="!canSubmit"
                  @click="updateProfile"
                >
                  登録
                </v-btn>
                <v-btn
                  class="ml-4"
                  color="red"
                  :disabled="!isEdit"
                  @click="formReset"
                >
                  編集破棄
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </template>
      </Popup>
    </v-dialog>
  </div>
</template>
