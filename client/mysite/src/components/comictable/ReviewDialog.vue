<script setup lang="ts">
import {
  ref,
  reactive,
  computed,
  toRefs,
  toRaw,
  watchEffect,
  provide,
  inject,
  nextTick,
} from 'vue';
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService';

interface FormState {
  scoreAlpha: number;
  scoreBeta: number;
  scoreCamma: number;
  scoreDelta: number;
  scoreEpsilon: number;
  comment: string | null;
  comicID: string;
  member: string;
}

const props = defineProps({
  review: Object,
  comicID: String,
});

const width = '1000px';
provide('width', width);

const { review } = toRefs(props);
const { comicID } = props;
const currentLink = inject('currentLink');

const isDialog = ref(false);
const isEdit = ref(true);
const isLoading = ref(false);
const formReference = ref(null);

const userPinia = userStore();

const formState: FormState = reactive({
  scoreAlpha: 0,
  scoreBeta: 0,
  scoreCamma: 0,
  scoreDelta: 0,
  scoreEpsilon: 0,
  comment: null,
  comicID: comicID,
  member: userPinia.id,
});

let initialState: FormState | null = null;

watchEffect(() => {
  if (review.value) {
    formState.scoreAlpha = parseFloat(review.value.scoreAlpha);
    formState.scoreBeta = parseFloat(review.value.scoreBeta);
    formState.scoreCamma = parseFloat(review.value.scoreCamma);
    formState.scoreDelta = parseFloat(review.value.scoreDelta);
    formState.scoreEpsilon = parseFloat(review.value.scoreEpsilon);
    formState.comment = review.value.comment;
    isEdit.value = false;
  }
  nextTick(() => {
    initialState = JSON.parse(JSON.stringify(formState));
    // console.log('initial:', initialState);
  });
});

const shownLabels = {
  scoreAlpha: 'アルファ',
  scoreBeta: 'ベータ',
  scoreCamma: 'ガンマ',
  scoreDelta: 'デルタ',
  scoreEpsilon: 'イプシロン',
};

const canSubmit = computed(() => {
  if (!initialState) return false;
  return Object.keys(formState).some((key) => {
    return (
      formState[key as keyof FormState] !== initialState[key as keyof FormState]
    );
  });
});

const formReset = () => {
  Object.assign(formState, initialState);
  if (review.value) {
    isEdit.value = false;
  }
};

const submitReview = () => {
  console.log('formState:', formState);
  console.log('currentLink:', currentLink);
  isLoading.value = true;
  let promise;
  if (review.value) {
    promise = EventService.patchReview(
      currentLink,
      review.value.id,
      toRaw(formState),
    );
  } else {
    promise = EventService.postReview(currentLink, toRaw(formState));
  }
  promise
    .then(() => {
      isLoading.value = !isLoading.value;
      isDialog.value = !isDialog.value;
      isEdit.value = !isEdit.value;
      initialState = JSON.parse(JSON.stringify(formState));
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
        <v-btn
          icon="mdi-pencil"
          size="x-large"
          elevation="0"
          depressed
          v-bind="activatorProps"
          :color="review ? 'red' : 'grey'"
        >
        </v-btn>
      </template>
      <Popup>
        <template v-slot:title>
          <h3 class="title font-weight-bold">Review</h3>
        </template>
        <template v-slot:content>
          <v-form ref="formReference" v-model="canSubmit">
            <v-row>
              <v-col cols="7">
                <ScoreRadar />
              </v-col>
              <v-col cols="5">
                <div
                  v-for="(label, rawLabel) in shownLabels"
                  :key="rawLabel"
                  class="slider-container"
                >
                  <v-subheader class="slider-label">
                    {{ label }}
                  </v-subheader>
                  <v-slider
                    v-model="formState[rawLabel]"
                    :min="0"
                    :max="5"
                    :step="0.1"
                    thumb-label="always"
                    :disabled="!isEdit"
                  >
                    <template #append>
                      <ScoreMenu :raw-label="rawLabel" />
                    </template>
                  </v-slider>
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="7">
                <v-container fluid>
                  <v-textarea
                    v-model="formState.comment"
                    clear-icon="mdi-close-circle"
                    label="感想"
                    clearable
                    :disabled="!isEdit"
                  ></v-textarea>
                </v-container>
              </v-col>
              <v-col cols="5">
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
                  @click="submitReview"
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

<style>
.slider-container .slider-label {
  text-align: left; /* ラベルを左寄せにする */
  display: block; /* ブロックレベル要素として扱う */
}
</style>
