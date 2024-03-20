<script setup lang="ts">
import { ref, reactive, toRaw } from 'vue';
import { useRouter } from 'vue-router';
import EventService from '@/plugins/EventService';

const router = useRouter();

const formState = reactive({
  username: '',
  password: '',
});

const showPassword = ref(false);

const submitLogin = () => {
  EventService.submitLogin(toRaw(formState))
    .then((response) => {
      window.localStorage.setItem('token', response.data.token);
      window.localStorage.setItem('id', response.data.id);
      window.localStorage.setItem('username', response.data.username);
      router.push({ name: 'home' });
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
      <v-text-field
        prepend-icon="mdi-account-circle"
        label="UserName"
        v-model="formState.username"
      />
      <v-text-field
        :type="showPassword ? 'text' : 'password'"
        @click:append="showPassword = !showPassword"
        prepend-icon="mdi-lock"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        label="Password"
        v-model="formState.password"
      />

      <v-btn
        class="info"
        color="primary"
        :disabled="formState.username === '' || formState.password === ''"
        @click.prevent="submitLogin"
      >
        ログイン
      </v-btn>
      <v-btn
        color="outline"
        class="ml-4"
        @click="() => $router.push({ path: '/signup' })"
      >
        新規作成
      </v-btn>
    </template>
  </Popup>
</template>
