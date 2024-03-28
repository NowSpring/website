<script setup lang="ts">
import { ref, reactive, computed, toRaw } from 'vue';
import { useRouter } from 'vue-router';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService';

const router = useRouter();
const userPinia = userStore();

const formState = reactive({ ...userPinia.$state });
const showPassword = ref(false);
const formReference = ref(null);
const isValid = ref(false);

const fieldRules = reactive({
  required: (value: string) => !!value || 'This field is required.',
});

const canSubmit = computed(() => {
  return isValid.value;
});

const submitLogin = () => {
  EventService.submitLogin(toRaw(formState))
    .then((response) => {
      window.localStorage.setItem('token', response.data.token);
      userPinia.id = response.data.user.id;
      userPinia.username = response.data.user.username;
      userPinia.email = response.data.user.email;
      router.push({ name: 'master' });
    })
    .catch((error) => {
      console.log('Error' + error);
    });
};
</script>

<template>
  <Popup>
    <template v-slot:title>
      <h3 class="title font-weight-bold">Login</h3>
    </template>
    <template v-slot:content>
      <v-form ref="formReference" v-model="isValid">
        <v-text-field
          label="UserName"
          prepend-icon="mdi-account-circle"
          v-model="formState.username"
          :rules="[fieldRules.required]"
        />
        <v-text-field
          label="Password"
          prepend-icon="mdi-lock"
          autocomplete="off"
          v-model="formState.password"
          :rules="[fieldRules.required]"
          :type="showPassword ? 'text' : 'password'"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="showPassword = !showPassword"
        />
        <v-btn
          class="info"
          color="primary"
          :disabled="!canSubmit"
          @click.prevent="submitLogin"
        >
          ログイン
        </v-btn>
        <v-btn
          class="ml-4"
          color="outline"
          @click="() => $router.push({ name: '/signup' })"
        >
          新規作成
        </v-btn>
      </v-form>
    </template>
  </Popup>
</template>
