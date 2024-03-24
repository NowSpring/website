<script setup lang="ts">
import { useRouter } from 'vue-router';
import EventService from '@/plugins/EventService';

const router = useRouter();

const showPassword = ref(false);
const formReference = ref(null);
const isValid = ref(false);

const formState = reactive({
  username: '',
  email: '',
  password: '',
});

const fieldRules = reactive({
  required: (value: string) => !!value || 'This field is required.',
  email: (value: string) => {
    const pattern =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return pattern.test(value) || 'Invalid email address.';
  },
});

const canSubmit = computed(() => {
  return isValid.value;
});

const formReset = () => {
  if (formReference.value) {
    formReference.value.reset();
  }
};

const submitSignup = () => {
  EventService.submitSignup(toRaw(formState))
    .then((response) => {
      router.push({ name: 'login' });
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};
</script>

<template>
  <Popup>
    <template v-slot:title>
      <h3 class="title font-weight-bold">Sign Up</h3>
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
          type="email"
          label="Email"
          prepend-icon="mdi-email"
          v-model="formState.email"
          :rules="[fieldRules.required, fieldRules.email]"
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
          color="primary"
          :disabled="!canSubmit"
          @click.prevent="submitSignup"
        >
          登録
        </v-btn>
        <v-btn color="outline" class="ml-4" @click="formReset()">
          リセット
        </v-btn>
      </v-form>
    </template>
  </Popup>
</template>
