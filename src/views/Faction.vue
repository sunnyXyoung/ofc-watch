<template>
  <div>
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
    <div class="row-div2">
      <div class="row-div chart-p">

        <VueApexCharts
            width="500" type="donut"
            :options="options3" :series="series3"
        >
        </VueApexCharts>
      </div>
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
      series1: [44, 55, 41, 17],
      series2: [44, 55, 41, 17],
      series3: [44, 55, 41, 17],
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
      options3: {
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
          text: "進攻次數（衛兵不算）"
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
    var jsonify = res => res.json();
    fetch(
        "http://localhost:3000/Faction1.json"
    ).then(jsonify).then(data=>{this.series1=data});
    fetch(
        "http://localhost:3000/Faction2.json"
    ).then(jsonify).then(data=>{this.series2=data});
    fetch(
        "http://localhost:3000/Faction3.json"
    ).then(jsonify).then(data=>{this.series3=data});
  }
}

</script>

<style scoped>
.chart-p {
  margin: 20px  ;
}
</style>