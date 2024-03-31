<script setup lang="ts">
import { ref, watchEffect } from 'vue';
// @types/chart.jsの型付けを使用するためにimportしてます。
import type { ChartData, ChartOptions } from 'chart.js';

// それぞれの部品をインポートしていきます。
// まだ種類があると思いますが、とりあえず手当たり次第importしておきます。
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  RadialLinearScale,
  Filler,
  LineElement,
} from 'chart.js';

// 今回はRadar-chartを作成するので、import。
// 他にも{ Bar }など、種類があります。
import { Radar } from 'vue-chartjs';

// ここでChartJSでこれらを使います〜と登録してあげます。
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  RadialLinearScale,
  LineElement,
  Filler,
  Title,
  Tooltip,
  Legend,
);

const props = defineProps({
  labels: Array,
  scores: Array,
});

// ここではchartに使うdataを登録していきます。
// ChartData<'radar'>でRadar-Chartの型付けを使ってます。
// 他にも<"bar">などがあります。
const chartData = ref({
  labels: props.labels,
  datasets: [
    {
      label: 'My Second dataset',
      backgroundColor: 'rgba(255,99,132,0.2)',
      borderColor: 'rgba(255,99,132,1)',
      pointBackgroundColor: 'rgba(255,99,132,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(255,99,132,1)',
      data: props.scores,
    },
  ],
});

// ここではchartに使うoptionsを登録していきます。
// ChartOptions<'radar'>でRadar-Chartの型付けを使ってます。
// 他にも<"bar">などがあります。
const options: ChartOptions<'radar'> = {
  responsive: true,
  maintainAspectRatio: false,
};

watchEffect(() => {
  chartData.value.datasets[0].data = props.scores;
});
</script>

<template>
  <!-- 定義したdataとoptionsを渡してあげます。 -->
  <Radar :data="chartData" :options="options" />
</template>
