import axios from 'axios'
const apiURI = 'http://localhost:5000/api/v1/resources'

const state = {
  playlist: null
}

const getters = {
  playlist: (state) => state.playlist
}

const actions = {
  async getPlaylist ({commit}) {
    const res = await axios.get(`${apiURI}/playlist`)
    commit('savePlaylist', res.data)
  }
}

const mutations = {
  savePlaylist: (state, playlist) => (state.playlist = playlist)
}

export default {
  state,
  getters,
  actions,
  mutations
}
