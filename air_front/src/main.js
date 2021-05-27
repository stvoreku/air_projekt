import Vue from 'vue'
import App from './App.vue'
import './assets/base.css';

Vue.config.productionTip = false

new Vue({
  data: {'PlaceID':0, 'QueueID': 0, 'plotX': [0,1,2,4,3,2], 'plotY': [1,1,2,3,3,1]},
  render: h => h(App),
}).$mount('#app')

console.log(Vue)
