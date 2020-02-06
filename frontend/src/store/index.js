import Vuex from 'vuex'
import Vue from 'vue'
import currentSong from './modules/currentSong.js'
import playlist from './modules/playlist.js'
import bookmarks from './modules/bookmarks.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    currentSong,
    playlist,
    bookmarks
  }
})
