<template>
  <div>
    <div class="row-div">
      <div id="ranks">
        <router-link class="ranks-link" to="kill">擊殺排行</router-link>
        <router-link class="ranks-link" to="killed">被擊殺排行</router-link>
        <router-link class="ranks-link" to="damage">輸出排行</router-link>
        <router-link class="ranks-link" to="damaged">被輸出排行</router-link>
        <router-link class="ranks-link" to="xp">戰鬥經驗排行</router-link>
        <router-link class="ranks-link" to="loot">樓層獎勵排行</router-link>
      </div>
    </div>
    <div style="display: None">
      <fusioncharts
          :type="type"
          :width="width"
          :height="height"
          :dataFormat="dataFormat"
          :dataSource="dataSource"
      ></fusioncharts>
    </div>
  </div>

</template>

<script>


import FusionCharts from "fusioncharts";

// register VueFusionCharts component


var jsonify = res => res.json();
var dataFetch = fetch(
    "https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-multiple-series-on-time-axis-data.json"
).then(jsonify);
var schemaFetch = fetch(
    "https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-multiple-series-on-time-axis-schema.json"
).then(jsonify);


export default {
name: "Fighter",
  components: {

  },
  data () {
    return {
      width: "100%",
      height: "400",
      type: "timeseries",
      dataFormat: "json",
      dataSource: {
        data:{},
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
    }
  },
  mounted: function() {
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

#ranks {
  text-align: center;
  width: 100%;
}

.ranks-link {
  font-weight: bold;
  color: #2c3e50;

  margin-right: 20px;
  margin-left: 20px;
}

.ranks-link:hover {
  text-decoration: underline;
}

</style>