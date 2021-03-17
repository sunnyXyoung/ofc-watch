<template>
  <div>
    <div class="row-div chart-p row-div2">
      <VueApexCharts
          width="500" type="donut"
          :options="options1" :series="series1"
      >
      </VueApexCharts>
    </div>
    <div class="row-div2">

    </div>
  </div>

</template>

<script>
import VueApexCharts from "vue-apexcharts";


export default {
  name: "Weapon",
  components: {
    VueApexCharts
  },
  data() {
    return {
      series1: [5],

      options1: {
        chart: {
          width: '100%',
          type: 'pie',
        },
        labels: ["單手劍"],
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
          text: "裝備出場分布"
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
    var jsonify = res => res.json();
    fetch(
        "./"+this.$store.state.round+"/Weapon1.json"
    ).then(jsonify).then(data=>{this.series1=data});
    fetch(
        "./"+this.$store.state.round+"/Weapon2.json"
    ).then(jsonify).then(data=>{this.options1.labels=data});
  }
}
</script>

<style scoped>
.chart-p {
  margin: 40px;
}
</style>