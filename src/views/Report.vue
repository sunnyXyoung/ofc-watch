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
  mounted: function () {
    var jsonify = res => res.json();
    var dataFetch = fetch(
        "./"+this.$store.state.round+"/Report2.json"
    ).then(jsonify);

    var schemaFetch = fetch(
        "./"+this.$store.state.round+"/Report3.json"
    ).then(jsonify);
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

    fetch(
        "./"+this.$store.state.round+"/Report1.json"
    ).then(jsonify).then(data => {
      this.series3 = data
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