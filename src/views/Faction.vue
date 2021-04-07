<template>
  <div v-if="loading">
    <div class="row-div row-div2 chart-p">
      <VueApexCharts
          class="charts" type="donut"
          :options="options1" :series="series1"
      >
      </VueApexCharts>
      <VueApexCharts
          class="charts" type="donut"
          :options="options2" :series="series2"
      >
      </VueApexCharts>
    </div>
    <div class="row-div row-div2 chart-p">
      <VueApexCharts
          class="charts" type="donut"
          :options="options3" :series="series3"
      >
      </VueApexCharts>
      <VueApexCharts
          class="charts" type="donut"
          :options="options4" :series="series4"
      >
      </VueApexCharts>
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
import api from "../api";
import FusionCharts from "fusioncharts";


export default {
  name: "Faction",
  components: {
    VueApexCharts
  },
  data() {
    return {
      loading: false,
      width: "80%",
      height: "400",
      type1: "timeseries",
      dataFormat: "json",
      dataSource: {
        data: {},
        chart: {},
        caption: {
          text: "樓層推進進度"
        },
        subcaption: {
          text: "還原歷史戰況"
        },
        series: "Type",
        yaxis: [
          {
            plot: [
              {
                value: "樓層數",
                plottype: "Step Line",
                connectnulldata: true,
                style: {
                  "plot.null": {
                    "stroke-dasharray": "none",
                  }
                }
              }
            ],
            title: "樓層推進進度",
            format: {
              prefix: ""
            }
          }
        ]
      },
      series1: [44, 55, 41, 17],
      series2: [44, 55, 41, 17],
      series3: [44, 55, 41, 17],
      series4: [44, 55, 41, 17],
      options1: {
        chart: {
          type: 'pie',
        },
        labels: ["大麻神教", "吳", "海外勢力", "艾基爾"],
        theme: {},
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
          type: 'pie',
        },
        labels: ["大麻神教", "吳", "海外勢力", "艾基爾"],
        theme: {},
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
          type: 'pie',
        },
        labels: ["大麻神教", "吳", "海外勢力", "艾基爾"],
        theme: {},
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
      options4: {
        chart: {
          type: 'pie',
        },
        labels: ["大麻神教", "吳", "海外勢力", "艾基爾"],
        theme: {},
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5
            }
          }
        },
        title: {
          text: "獲得樓層獎勵數"
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
  watch: {
    "$store.state.round": async function () {
      this.loading = false
      var dataFetch = await api.getData("Faction5.json")
      var schemaFetch = await api.getData("Faction6.json")
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
      this.series1 = await api.getData("Faction1.json")
      this.options1.labels = await api.getData("Faction12.json")
      this.series2 = await api.getData("Faction2.json")
      this.options2.labels = await api.getData("Faction12.json")
      this.series3 = await api.getData("Faction3.json")
      this.options3.labels = await api.getData("Faction12.json")
      this.series4 = await api.getData("Faction4.json")
      this.options4.labels = await api.getData("Faction12.json")
      this.loading = true
    },
  },
  mounted: async function () {
    var dataFetch = await api.getData("Faction5.json")
    var schemaFetch = await api.getData("Faction6.json")
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
    this.series1 = await api.getData("Faction1.json")
    this.options1.labels = await api.getData("Faction12.json")
    this.series2 = await api.getData("Faction2.json")
    this.options2.labels = await api.getData("Faction12.json")
    this.series3 = await api.getData("Faction3.json")
    this.options3.labels = await api.getData("Faction12.json")
    this.series4 = await api.getData("Faction4.json")
    this.options4.labels = await api.getData("Faction12.json")
    this.loading = true
  }
}

</script>

<style scoped>
.chart-p {
  margin: 20px;
}
</style>
