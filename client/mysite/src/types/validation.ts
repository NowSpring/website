import { defineRule, type GenericObject } from 'vee-validate';
import { required } from '@vee-validate/rules';

defineRule('required', (value: string, params: string): boolean | string => {
  if (required(value)) {
    return true;
  } else {
    return `${params} can not be empty`;
  }
});
