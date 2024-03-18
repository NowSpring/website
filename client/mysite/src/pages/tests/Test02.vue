<script setup>
import { useForm } from 'vee-validate';
import * as yup from 'yup';
import EventService from '@/plugins/EventService';

const schema = yup.object({
  username: yup.string().required().label('UserName'),
  email: yup
    .string()
    .email()
    .required()
    .label('E-mail')
    .matches(/^[^\s@]+@[^\s@]+\.[^\s@]+$/, 'E-mail must be a valid email'),
  password: yup.string().min(6).required(),
  passwordConfirm: yup
    .string()
    .oneOf([yup.ref('password')], 'Passwords must match')
    .required()
    .label('Password confirmation'),
});

const { defineField, handleSubmit, resetForm } = useForm({
  validationSchema: schema,
});

// // Refer to the docs for how to make advanced validation behaviors with dynamic configs
// // TODO: Add link
const vuetifyConfig = (state) => ({
  props: {
    'error-messages': state.errors,
  },
});

const [username, usernameProps] = defineField('username', vuetifyConfig);
const [email, emailProps] = defineField('email', vuetifyConfig);
const [password, passwordProps] = defineField('password', vuetifyConfig);
const [passwordConfirm, confirmProps] = defineField(
  'passwordConfirm',
  vuetifyConfig,
);

const onSubmit = handleSubmit((values) => {
  // 必要なプロパティのみを含む新しいオブジェクトを作成
  const { passwordConfirm, ...submissionValues } = values;

  console.log('Submitted with', submissionValues);
  EventService.submitSignup(submissionValues)
    .then((response) => {
      console.log('Submitted with', submissionValues);
    })
    .catch((error) => {
      console.error('Submission error:', error);
    });
});
</script>

<template>
  <v-form @submit="onSubmit" class="px-4">
    <v-text-field v-model="username" v-bind="usernameProps" label="Name" />
    <v-text-field
      v-model="email"
      v-bind="emailProps"
      label="Email"
      type="email"
    />
    <v-text-field
      v-model="password"
      v-bind="passwordProps"
      label="Password"
      type="password"
    />
    <v-text-field
      v-model="passwordConfirm"
      v-bind="confirmProps"
      label="Password confirmation"
      type="password"
    />

    <v-btn color="primary" type="submit"> Submit </v-btn>
    <v-btn color="outline" class="ml-4" @click="resetForm()"> Reset </v-btn>
  </v-form>
</template>
