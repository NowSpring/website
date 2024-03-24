<template>
  <div v-if="form">
    <v-card-title>Profile</v-card-title>
    <v-card-text>
      <v-form>
        <v-container>
          <div class="mb-2 text-subtitle-1 font-weight-bold">名前</div>
          <v-row no-gutters>
            <v-col class="mr-3">
              <v-text-field label="姓" v-model="form.lastName"></v-text-field>
            </v-col>
            <v-col class="ml-3">
              <v-text-field label="名" v-model="form.firstName"></v-text-field>
            </v-col>
          </v-row>
          <div class="mb-2 text-subtitle-1 font-weight-bold">連絡先</div>
          <v-text-field
            label="電話番号"
            v-model="form.contact.phoneNumber"
          ></v-text-field>
          <v-text-field
            label="メールアドレス"
            v-model="form.contact.mail"
          ></v-text-field>
          <div v-for="(address, index) in form.addresses" :key="address.id">
            <div class="mb-2 text-subtitle-1 font-weight-bold">
              住所 {{ index + 1 }}
            </div>
            <v-row no-gutters>
              <v-col class="mr-3">
                <v-text-field
                  label="都道府県"
                  v-model="address.prefecture"
                ></v-text-field>
              </v-col>
              <v-col class="ml-3">
                <v-text-field
                  label="市区町村"
                  v-model="address.municipality"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row no-gutters>
              <v-col class="mr-3">
                <v-text-field
                  label="番地"
                  v-model="address.blockNumber"
                ></v-text-field>
              </v-col>
              <v-col class="ml-3">
                <v-text-field
                  label="建物"
                  v-model="address.building"
                ></v-text-field>
              </v-col>
            </v-row>
          </div>
        </v-container>
      </v-form>
    </v-card-text>
  </div>
</template>

<script setup lang="ts">
import { reactive, toRefs } from 'vue';
import Profile from '@/tests/domain/Profile';

// definePropsを使ってpropsを定義
const props = defineProps({
  value: {
    type: Object as PropType<Profile>,
    required: true,
  },
});

// reactiveを使ってformをリアクティブなデータとして定義
const form = reactive({ ...props.value });

// toRefsを使用してリアクティブなプロパティを分解して、テンプレート内での使用を可能にします。
// このステップは、このケースでは特に必要ではありませんが、リアクティブなオブジェクトのプロパティをテンプレートで直接参照する際に便利です。
const { value } = toRefs(props);
</script>

<style scoped>
/* スタイルがあればここに追加 */
</style>
