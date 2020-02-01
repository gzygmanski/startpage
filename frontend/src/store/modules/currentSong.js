const state = {
  song: {},
  isConnected: false
}

const getters = {
  currentSong: (state) => state.song,
  connection: (state) => state.isConnected
}

const actions = {
}

const mutations = {
  SOCKET_CONNECT: (state) => {
    state.isConnected = true
    console.log('Client connected')
  },
  SOCKET_DISCONNECT: (state) => {
    state.isConnected = false
    console.log('Client disconnected')
  },
  SOCKET_CURRENTSONG: (state, data) => {
    state.song = data
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
