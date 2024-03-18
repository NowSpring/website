<script setup lang="ts">
import { useForm, FieldBinding, FormActions } from 'vee-validate';
import * as yup from 'yup';

import Popup from '@/components/Popup.vue';

// スキーマ定義には変更なし
const schema = yup.object({
  user_name: yup.string().required().label('UserName'),
  email: yup.string().email().required().label('E-mail'),
  password: yup.string().min(6).required(),
});

const { defineField, handleSubmit, resetForm }: FormActions = useForm({
  validationSchema: schema,
});

const vuetifyConfig = (state): Record<string, any> => ({
  props: {
    'error-messages': state.errors,
  },
});

const [user_name, nameProps]: [ref: string, binding: FieldBinding] =
  defineField('user_name', vuetifyConfig);
const [email, emailProps]: [ref: string, binding: FieldBinding] = defineField(
  'email',
  vuetifyConfig,
);
const [password, passwordProps]: [ref: string, binding: FieldBinding] =
  defineField('password', vuetifyConfig);

const onSubmit = handleSubmit((values) => {
  console.log('Submitted with', values);
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
        v-model="user_name"
        v-bind="nameProps"
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
        prepend-icon="mdi-lock"
        v-model="password"
        v-bind="passwordProps"
        label="Password"
        type="password"
      />
      <v-btn
        color="primary"
        :disabled="formState.username === '' || formState.password === ''"
        @click.prevent="onSubmit"
      >
        登録
      </v-btn>
      <v-btn color="outline" class="ml-4" @click="resetForm()">
        リセット
      </v-btn>
    </template>
  </Popup>
</template>
