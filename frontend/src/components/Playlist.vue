<template>
  <div>
    <h3>Playlist:</h3>
    <form>
      <select v-model="selected" v-on:change="loadPlaylistAndUpdate(selected)">
        <option v-for="playlist in playlistList" v-bind:key="playlist.playlist" v-bind:value="playlist.playlist">{{ playlist.playlist }}</option>
      </select>
    </form>
    <table>
      <thead>
        <tr>
          <td>POS</td>
          <td>ARTIST</td>
          <td>TITLE</td>
          <td>ACTIONS</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="song in playlist" v-bind:key="song.pos" v-bind:class="{'active':(currentSong.pos === song.pos)}" >
          <td>{{ song.pos }}</td>
          <td>{{ song.artist }}</td>
          <td>{{ song.title }}</td>
          <td>
            <button v-on:click="playPos(song.pos)">play</button>
            <button v-on:click="removePosAndUpdate(song.pos)">remove</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default{
  name: 'Playlist',
  data () {
    return {
      selected: ''
    }
  },
  computed: {
    ...mapGetters(['playlist', 'playlistList', 'currentSong'])
  },
  methods: {
    ...mapActions(['getCurrentPlaylist', 'getPlaylistList', 'playPos', 'removePos', 'loadPlaylist']),
    removePosAndUpdate (pos) {
      this.removePos(pos)
      this.getCurrentPlaylist()
    },
    loadPlaylistAndUpdate (name) {
      console.log(name)
      this.loadPlaylist(name)
      this.getCurrentPlaylist()
    }
  },
  created () {
    this.getPlaylistList()
    this.getCurrentPlaylist()
  }
}
</script>

<style scoped>
tbody tr:hover {
  background: #ccc;
}
.active {
  background: #ccc;
}
</style>
