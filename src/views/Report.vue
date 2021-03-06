<template>
  <div id="app">
    <fusioncharts
        :type="type1"
        :width="width"
        :height="height"
        :dataFormat="dataFormat"
        :dataSource="dataSource"
    ></fusioncharts>

    <div id="row-div">
      <VueApexCharts
          width="500" type="bar"
          :options="options" :series="series2"
      >
      </VueApexCharts>
      <VueApexCharts
          width="500" type="donut"
          :options="options2" :series="series3"
      >
      </VueApexCharts>

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
      chartOptions: {
        chart: {
          type: 'donut',
        },
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }]
      },
      series3: [44, 55, 41, 17, 15],
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec"
          ]
        }
      },
      series2: [{
        name: 'series-1',
        data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
      }],
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

#row-div {
  display: flex;
  flex-flow: row;
}
</style>