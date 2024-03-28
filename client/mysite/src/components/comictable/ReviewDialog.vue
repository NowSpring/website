<script setup lang="ts">
import { userStore } from '@/stores/user';
import EventService from '@/plugins/EventService';
import { ref, reactive, computed, toRaw, provide } from 'vue';

const props = defineProps({
  hasReview: Boolean,
});

const width = '1000px';
provide('width', width);

const isReviewDialog = ref(false);
const isEdit = ref(false);
const isValid = ref(false);
const isLoading = ref(false);
const formReference = ref(null);

const userPinia = userStore();
const formState = reactive({ ...userPinia.$state });

const scores = ref({
  scoreAlpha: 0,
  scoreBeta: 0,
  scoreCamma: 0,
  scoreDelta: 0,
  scoreEpsilon: 0,
});

const scoreMin = 0;
const scoreMax = 5;

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
      isReviewDialog.value = !isReviewDialog.value;
      isEdit.value = !isEdit.value;
    })
    .catch((error) => {
      console.log('Error' + error);
    });
};
</script>

<template>
  <div class="pa-4 text-center">
    <v-dialog v-model="isReviewDialog" max-width="100000">
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          icon="mdi-pencil"
          size="x-large"
          elevation="0"
          depressed
          v-bind="activatorProps"
          :color="hasReview ? 'red' : 'grey'"
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
              <v-col col="8">
                <ScoreRadar />
              </v-col>
              <v-col col="4">
                <v-slider
                  v-model="scoreAlpha"
                  :min="scoreMin"
                  :max="scoreMax"
                  step="0.1"
                  thumb-label
                  ticks
                  label="スライダーラベル"
                >
                  <template #append>
                    <ScoreMenu title="スライダーラベル" />
                  </template>
                </v-slider>
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
