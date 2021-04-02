import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueFusionCharts from "vue-fusioncharts";
import FusionCharts from "fusioncharts";
import TimeSeries from "fusioncharts/fusioncharts.timeseries";
import store from './store';

Vue.use(VueFusionCharts, FusionCharts, TimeSeries,);
Vue.config.productionTip = false

new Vue({
    router, store,
    render: h => h(App)
}).$mount('#app')