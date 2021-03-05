<template>
  <div>
    <p>still working.</p>
    <GChart
        type="LineChart"
        :data="chartData"
        :options="chartOptions"
    />
    <GChart
        type="ChartRangeFilter"
        :options="controlOptions"

    />

  </div>

</template>

<script>
import { GChart } from 'vue-google-charts'

import Vue from "vue";
import VueFusionCharts from "vue-fusioncharts";
import FusionCharts from "fusioncharts";
import TimeSeries from "fusioncharts/fusioncharts.timeseries";

// register VueFusionCharts component
Vue.use(VueFusionCharts, FusionCharts, TimeSeries);

var jsonify = res => res.json();
var dataFetch = fetch(
    "https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-multiple-series-on-time-axis-data.json"
).then(jsonify);
var schemaFetch = fetch(
    "https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-multiple-series-on-time-axis-schema.json"
).then(jsonify);

var app = new Vue({
  el: "#app",
  data: {
    width: "100%",
    height: "400",
    type: "timeseries",
    dataFormat: "json",
    dataSource: {
      chart: {},
      caption: {
        text: "Sales Analysis"
      },
      subcaption: {
        text: "Grocery & Footwear"
      },
      series: "Type",
      yaxis: [
        {
          plot: "Sales Value",
          title: "Sale Value",
          format: {
            prefix: "$"
          }
        }
      ]
    }
  },
  mounted: function() {
    Promise.all([dataFetch, schemaFetch]).then(res => {
      const data = res[0];
      const schema = res[1];
      const fusionTable = new FusionCharts.DataStore().createDataTable(
          data,
          schema
      );
      this.dataSource.data = fusionTable;
    });
  }
});

export default {
name: "Fighter",
  components: {
    GChart
  },
  data () {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData:
        // ['Date', 'Value'],
        [
          ['Name', 'Donuts eaten'],
          ['Michael' , 5],
          ['Elisa', 7],
          ['Robert', 3],
          ['John', 2],
          ['Jessica', 6],
          ['Aaron', 1],
          ['Margareth', 8]
        ]
      ,
      chartOptions: {
        chart: {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        },
        vAxis: { viewWindow: { min: 0, max: 9 } },
        hAxis: { slantedText: false },
        chartArea: { height: '80%', width: '90%' },
        legend: { position: 'none' },

      },
      controlOptions: [

      ]
    }
  }
}
</script>

<style scoped>

</style>