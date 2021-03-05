import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueFusionCharts from "vue-fusioncharts";
import FusionCharts from "fusioncharts";
import TimeSeries from "fusioncharts/fusioncharts.timeseries";


Vue.use(VueFusionCharts, FusionCharts, TimeSeries);
Vue.config.productionTip = false
// Vue.prototype.google = google


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
