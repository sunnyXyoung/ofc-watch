<template>
  <div class="row-div row-div2">
    <div class="row-div chart-p">

      <VueApexCharts
          width="500" type="donut"
          :options="options1" :series="series1"
      >
      </VueApexCharts>
    </div>
    <div class="row-div chart-p">

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
        chart: {
          width: '100%',
          type: 'pie',
        },
        labels: ["大麻神教", "吳", "海外勢力", "艾基爾"],
        theme: {

        },
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5
            }
          }
        },
        title: {
          text: "陣營輸出"
        },
        dataLabels: {
          formatter(val, opts) {
            const name = opts.w.globals.labels[opts.seriesIndex]
            return [name, val.toFixed(1) + '%']
          }
        },
        legend: {
          show: false
        }
      },
      options2: {
        chart: {
          width: '100%',
          type: 'pie',
        },
        labels: ["大麻神教", "吳", "海外勢力", "艾基爾"],
        theme: {

        },
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5
            }
          }
        },
        title: {
          text: "戰鬥熟練總和（有出戰過的）"
        },
        dataLabels: {
          formatter(val, opts) {
            const name = opts.w.globals.labels[opts.seriesIndex]
            return [name, val.toFixed(1) + '%']
          }
        },
        legend: {
          show: false
        }
      },
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