<template>
  <div>
    <div class="row-div2">
      <div class="row-div">
        <VueApexCharts class="charts"
            :options="options2" :series="series3"
            type="donut"
        >
        </VueApexCharts>
      </div>

    </div>
    <div class="row-div2">
      <fusioncharts
          :dataFormat="dataFormat"
          :dataSource="dataSource"
          :height="height"
          :type="type1"
          :width="width"
      ></fusioncharts>
    </div>


  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import FusionCharts from "fusioncharts";
import api from "../api";


export default {
  name: "Report",
  components: {
    VueApexCharts
  },
  data() {
    return {
      width: "80%",
      height: "400",
      type1: "timeseries",
      dataFormat: "json",
      dataSource: {
        data: {},
        chart: {},
        caption: {
          text: "戰報時間分布"
        },
        subcaption: {
          text: "時間解析度：1小時"
        },
        series: "Type",
        yaxis: [
          {
            plot: "Sales Value",
            title: "每小時戰報數",
            format: {
              prefix: ""
            }
          }
        ]
      },
      series3: [44, 55, 41, 17, 44, 55, 41, 17, 44, 55, 41, 17, 44, 55, 41, 17, 44, 55, 41, 17, 44, 55, 41, 17],
      options2: {
        chart: {
          width: '100%',
          type: 'pie',
        },
        labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        theme: {
          monochrome: {
            enabled: true
          }
        },
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5
            }
          }
        },
        title: {
          text: "戰報時間統計"
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
  mounted: async function () {
    var dataFetch = await api.getData("Report2.json")
    var schemaFetch = await api.getData("Report3.json")
    Promise.all([dataFetch, schemaFetch]).then(res => {
      const data = res[0];
      const schema = res[1];
      console.log(schema);
      this.dataSource.data = new FusionCharts.DataStore().createDataTable(
          data,
          schema
      );
      // this.dataSource.data = fusionTable;
    });
    this.series3 = await api.getData("Report1.json")


  }
}

</script>

<style scoped>



</style>
