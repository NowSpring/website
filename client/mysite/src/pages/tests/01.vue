<!-- https://zenn.dev/iandcinc/articles/5d4a4b4b3297c1 -->
<script setup lang="ts">
// import { useRoute } from 'vue-router/auto'
import { Field, Form, defineRule, type GenericObject } from 'vee-validate';
import { required } from '@vee-validate/rules';

// const route = useRoute('/tests/Test')

defineRule('required', (value: string, params: string): boolean | string => {
  if (required(value)) {
    return true;
  } else {
    return `${params} can not be empty`;
  }
});

defineRule('email', (value: string): boolean | string => {
  if (/^[a-z.-]+@[a-z.-]+\.[a-z]+$/i.test(value)) {
    return true;
  } else {
    return 'Email must be valid';
  }
});

const emailValue = ref('');

const onSubmit = (values: GenericObject) => {
  alert(JSON.stringify(values, null, 2));
};
</script>

<template>
  <v-app>
    <v-sheet class="pa-4" width="540" location="top left">
      <Form v-slot="{ meta, handleReset }" @submit="onSubmit">
        <Field
          v-slot="{ errors, handleChange }"
          name="email"
          v-model="emailValue"
          rules="required:Email|email"
        >
          <v-text-field
            label="E-mail"
            :model-value="emailValue"
            @update:model-value="
              (e: string) => handleChange(e, errors.length > 0)
            "
            @blur="handleChange"
            :error-messages="errors"
          ></v-text-field>
        </Field>

        <v-btn class="me-4" type="submit" :disabled="!meta.valid">
          submit
        </v-btn>

        <v-btn @click="handleReset"> clear </v-btn>
      </Form>
    </v-sheet>
  </v-app>
</template>
