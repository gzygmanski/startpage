import axios from 'axios'
const apiURI = 'http://localhost:5000/api/v1/resources'

const state = {
  playlist: null,
  playlistList: null,
  pos: 1,
  playlistName: ''
}

const getters = {
  playlist: (state) => state.playlist,
  playlistList: (state) => state.playlistList
}

const actions = {
  async getCurrentPlaylist ({commit}) {
    const res = await axios.get(`${apiURI}/playlists/currentplaylist`)
    commit('savePlaylist', res.data)
  },
  async getPlaylistList ({commit}) {
    const res = await axios.get(`${apiURI}/playlists`)
    commit('savePlaylistList', res.data)
  },
  playPos ({commit}, pos) {
    commit('getPos', pos)
    this._vm.$socket.client.emit('play_pos', state.pos)
  },
  removePos ({commit}, pos) {
    commit('getPos', pos)
    this._vm.$socket.client.emit('remove_pos', state.pos)
  },
  loadPlaylist ({commit}, name) {
    commit('getPlaylistName', name)
    this._vm.$socket.client.emit('load_playlist', state.playlistName)
  }
}

const mutations = {
  savePlaylist: (state, playlist) => (state.playlist = playlist),
  savePlaylistList: (state, playlistList) => (state.playlistList = playlistList),
  getPos: (state, pos) => (state.pos = pos),
  getPlaylistName: (state, name) => (state.playlistName = name)
}

export default {
  state,
  getters,
  actions,
  mutations
}
