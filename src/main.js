import Vue from 'vue';
import 'bootstrap/dist/css/bootstrap.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App.vue';
import router from './router';
import store from './store';
// import axios from "axios";

Vue.use(BootstrapVue);
// Vue.use(axios)
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
