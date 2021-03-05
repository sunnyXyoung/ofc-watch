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