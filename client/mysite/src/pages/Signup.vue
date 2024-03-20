<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useForm } from 'vee-validate';
import * as yup from 'yup';
import EventService from '@/plugins/EventService';

const router = useRouter();

const schema = yup.object({
  username: yup.string().required().label('UserName'),
  email: yup
    .string()
    .email()
    .required()
    .label('E-mail')
    .matches(/^[^\s@]+@[^\s@]+\.[^\s@]+$/, 'E-mail must be a valid email'),
  password: yup.string().min(6).required(),
});

const { defineField, handleSubmit, resetForm } = useForm({
  validationSchema: schema,
});

const vuetifyConfig = (state): Record<string, any> => ({
  props: {
    'error-messages': state.errors,
  },
});

const [username, usernameProps] = defineField('username', vuetifyConfig);
const [email, emailProps] = defineField('email', vuetifyConfig);
const [password, passwordProps] = defineField('password', vuetifyConfig);

const showPassword = ref(false);

const onSubmit = handleSubmit((values) => {
  EventService.submitSignup(values)
    .then((response) => {
      router.push({ name: 'login' });
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
</script>

<template>
  <Popup>
    <template v-slot:title>
      <h3 class="title font-weight-bold">Sign Up</h3>
    </template>
    <template v-slot:content>
      <v-text-field
        prepend-icon="mdi-account-circle"
        v-model="username"
        v-bind="usernameProps"
        label="UserName"
      />
      <v-text-field
        prepend-icon="mdi-email"
        v-model="email"
        v-bind="emailProps"
        label="Email"
        type="email"
      />
      <v-text-field
        :type="showPassword ? 'text' : 'password'"
        @click:append="showPassword = !showPassword"
        prepend-icon="mdi-lock"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        v-model="password"
        v-bind="passwordProps"
        label="Password"
      />
      <v-btn color="primary" @click.prevent="onSubmit"> 登録 </v-btn>
      <v-btn color="outline" class="ml-4" @click="resetForm()">
        リセット
      </v-btn>
    </template>
  </Popup>
</template>
