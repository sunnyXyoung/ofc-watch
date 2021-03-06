<template>
  <div class="row-div row-div2">
    <div class="row-div chart-p">
      <p>陣營輸出</p>
      <VueApexCharts
          width="500" type="donut"
          :options="options1" :series="series1"
      >
      </VueApexCharts>
    </div>
    <div class="row-div chart-p">
      <p>戰鬥熟練總和</p>
      <VueApexCharts
          width="500" type="donut"
          :options="options2" :series="series2"
      >
      </VueApexCharts>
    </div>
  </div>

</template>

<script>

import VueApexCharts from 'vue-apexcharts'



export default {
  name: "Faction",
  components: {
    VueApexCharts
  },
  data() {
    return {
      series1: [44, 55, 41, 17, 15],
      series2: [44, 55, 41, 17, 15],
      options1: {
        dataLabels: {
          enabled: true,
          formatter: function (val) {
            return val + "%"
          },
          dropShadow: {

          }
        }
      },
      options2: {
        dataLabels: {
          enabled: true,
          formatter: function (val) {
            return val + "%"
          },
          dropShadow: {

          }
        }
      }
    }
  },
  mounted: function () {
  }
}

</script>

<style scoped>
.chart-p {
  margin: 20px  ;
}
</style>