<template>
  <div id="playlist">
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
        <tr v-for="song in playlist" v-bind:key="song.pos" v-bind:class="{'active':(currentSong.pos === song.pos)}" v-on:click="playPos(song.pos)">
          <td>{{ song.pos }}</td>
          <td>{{ song.artist }}</td>
          <td>{{ song.title }}</td>
          <td>
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
form {
  margin: 0 auto;
  width: 100%;
  position: relative;
}
select {
  width: 90%;

}
#playlist { 
  overflow: scroll;
  position: fixed;
  top: 0;
  width: 500px;
  background-color: #000;
  height: 100%;
  font: monospace;
  color: #fff;
  font-size: 10px;
}

table {
  margin: 0 auto;
}
tbody tr:hover {
  cursor: pointer;
  background: #ccc;
}
.active {
  background: #ccc;
}
</style>
