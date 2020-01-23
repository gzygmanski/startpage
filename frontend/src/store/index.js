import Vuex from 'vuex'
import Vue from 'vue'
import currentSong from './modules/currentSong.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    currentSong
  }
})
