<script setup lang="ts">
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

// ここではchartに使うdataを登録していきます。
// ChartData<'radar'>でRadar-Chartの型付けを使ってます。
// 他にも<"bar">などがあります。
const data: ChartData<'radar'> = {
  labels: [
    'Eating',
    'Drinking',
    'Sleeping',
    'Designing',
    'Coding',
    'Cycling',
    'Running',
  ],
  datasets: [
    {
      label: 'My First dataset',
      backgroundColor: 'rgba(179,181,198,0.2)',
      borderColor: 'rgba(179,181,198,1)',
      pointBackgroundColor: 'rgba(179,181,198,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(179,181,198,1)',
      data: [65, 59, 90, 81, 56, 55, 40],
    },
    {
      label: 'My Second dataset',
      backgroundColor: 'rgba(255,99,132,0.2)',
      borderColor: 'rgba(255,99,132,1)',
      pointBackgroundColor: 'rgba(255,99,132,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(255,99,132,1)',
      data: [28, 48, 40, 19, 96, 27, 100],
    },
  ],
};

// ここではchartに使うoptionsを登録していきます。
// ChartOptions<'radar'>でRadar-Chartの型付けを使ってます。
// 他にも<"bar">などがあります。
const options: ChartOptions<'radar'> = {
  responsive: true,
  maintainAspectRatio: false,
};

const props = defineProps({
  scoreAlpha: Float64Array,
  headers: Array,
  linkname: String,
});
</script>

<template>
  <!-- 定義したdataとoptionsを渡してあげます。 -->
  <Radar :data="data" :options="options" />
</template>
