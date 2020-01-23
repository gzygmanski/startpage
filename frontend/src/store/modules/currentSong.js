import axios from 'axios'

const apiURI = 'http://localhost:5000/api/v1/resources/currentsong'

const state = {
  song: []
}

const getters = {
  currentSong: (state) => state.song
}

const actions = {
  async fetch ({commit}) {
    const response = await axios.get(apiURI)
    commit('getSong', response.data)
  }
}

const mutations = {
  getSong: (state, song) => (state.song.push(song))
}

export default {
  state,
  getters,
  actions,
  mutations
}
