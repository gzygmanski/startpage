import axios from 'axios'
const apiURI = 'http://localhost:5000/api/v1/resources'

const state = {
  bookmarks: [],
  name: '',
  url: ''
}

const getters = {
  bookmarks: (state) => state.bookmarks
}

const actions = {
  async getBookmarks ({commit}) {
    const res = await axios.get(`${apiURI}/bookmarks`)
    commit('saveBookmarks', res.data)
  },
  postBookmark ({commit}, payload) {
    commit('getBookmark', payload)
    axios.post(`${apiURI}/bookmarks/add/`, {
      name: state.name,
      url: state.url
    })
  }
}

const mutations = {
  saveBookmarks: (state, bookmarks) => (state.bookmarks = bookmarks),
  getBookmark: (state, payload) => {
    state.name = payload.name
    state.url = payload.url
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
