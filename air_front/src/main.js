import Vue from 'vue'
import App from './App.vue'
import './assets/base.css';

Vue.config.productionTip = false

new Vue({
  data: {'PlaceID':0, 'QueueID': 0, 'plotX': [], 'plotY': []},
  render: h => h(App),
}).$mount('#app')

console.log(Vue)
