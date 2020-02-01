<template>
  <div>
    <h3>Playlist:</h3>
    <table>
      <thead>
        <tr>
          <td>POS</td>
          <td>ARTIST</td>
          <td>TITLE</td>
          <td>ALBUM</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="song in playlist" v-bind:key="song.pos">
          <td>{{ song.pos }}</td>
          <td>{{ song.artist }}</td>
          <td>{{ song.title }}</td>
          <td>{{ song.album }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default{
  name: 'Playlist',
  computed: {
    ...mapGetters(['playlist'])
  },
  methods: {
    ...mapActions(['getPlaylist'])
  },
  created () {
    this.getPlaylist()
  }
}
</script>

<style scoped>

</style>
