<template>
  <div>
    <div class="row-div chart-p row-div2">
      <p>裝備出場分布</p>
      <VueApexCharts
          width="500" type="donut"
          :options="options1" :series="series1"
      >
      </VueApexCharts>
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
    var jsonify = res => res.json();
    fetch(
        "http://localhost:3000/time1.json"
    ).then(jsonify).then(data=>{this.series1=data});
    console.log(this.series1);
  }
}
</script>

<style scoped>
.chart-p {
  margin: 40px;
}
</style>