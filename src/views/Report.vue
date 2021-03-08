<template>
  <div>
    <div class="row-div2">
    <div class="row-div">
      <VueApexCharts
          width="500" type="donut"
          :options="options2" :series="series3"
      >
      </VueApexCharts>
    </div>

  </div>
    <div class="row-div2">
      <fusioncharts
          :type="type1"
          :width="width"
          :height="height"
          :dataFormat="dataFormat"
          :dataSource="dataSource"
      ></fusioncharts>
    </div>



  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import FusionCharts from "fusioncharts";

var jsonify = res => res.json();
var dataFetch = fetch(
    "/data/time1.json"
).then(jsonify);

var schemaFetch = fetch(
    "https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-multiple-series-on-time-axis-schema.json"
).then(jsonify);


// new Vue({
//   el: '#app',
//   components: {
//     apexchart: VueApexCharts,
//   },
//   data: {
//
//     series: [25, 15, 44, 55, 41, 17],
//     chartOptions
//
//
//   },
//
// })



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
      // chartOptions: {
      //   chart: {
      //     type: 'donut',
      //   },
      //   responsive: [{
      //     breakpoint: 480,
      //     options: {
      //       chart: {
      //         width: 200
      //       },
      //       legend: {
      //         position: 'bottom'
      //       }
      //     }
      //   }]
      // },
      series3: [44, 55, 41, 17],
      options2: {
        chart: {
          width: '100%',
          type: 'pie',
        },
        labels: ["大麻神教", "吳", "海外勢力", "艾基爾"],
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
      series2: [{
        name: 'series-1',
        data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
      }],

    }
  },
  mounted: function () {
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

  }
}

</script>

<style scoped>

#app {
  width: 100%;
  padding: 50px;
}


</style>