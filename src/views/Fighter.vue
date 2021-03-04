<template>
  <div>
    <p>still working.</p>
    <GChart
        type="LineChart"
        :data="chartData"
        :options="chartOptions"


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
      chartData: [
        ['Date', 'Value'],
        [new Date(1996, 1, 1), 2000 * Math.random()],
        [new Date(1997, 1, 1), 2000 * Math.random()],
        [new Date(1998, 1, 1), 2000 * Math.random()],
        [new Date(1999, 1, 1), 2000 * Math.random()],
        [new Date(2000, 1, 1), 2000 * Math.random()],
        [new Date(2001, 1, 1), 2000 * Math.random()],
        [new Date(2002, 1, 1), 2000 * Math.random()],
        [new Date(2003, 1, 1), 2000 * Math.random()],
        [new Date(2004, 1, 1), 2000 * Math.random()],
        [new Date(2005, 1, 1), 2000 * Math.random()],
        [new Date(2006, 1, 1), 2000 * Math.random()],
        [new Date(2007, 1, 1), 2000 * Math.random()],
        [new Date(2008, 1, 1), 2000 * Math.random()],
        [new Date(2009, 1, 1), 2000 * Math.random()],
      ],
      chartOptions: {
        chart: {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        },
        vAxis: { viewWindow: { min: 0, max: 2000 } },
        hAxis: { slantedText: false },
        chartArea: { height: '80%', width: '90%' },
        legend: { position: 'none' }
      }
    }
  }
}
</script>

<style scoped>

</style>