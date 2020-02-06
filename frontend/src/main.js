// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/index.js'
import vuesocketioext from 'vue-socket.io-extended'
import io from 'socket.io-client'

const socket = io('http://localhost:5000/api')

Vue.config.productiontip = false

Vue.use(vuesocketioext, socket, { store })

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
