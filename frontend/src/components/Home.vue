<template>
    <div>
        <h1>Home Page</h1>
        <h3>Currently playing:</h3>
        <div id="currentSong">
            <template v-if="!currentSong.rate">
                <span>{{ currentSong.pos }}</span>
                <span>{{ currentSong.artist }}</span>
                <span>{{ currentSong.album }}</span>
                <span>{{ currentSong.title }}</span>
                <span>none</span>
            </template>
            <template v-else>
                <span>{{ currentSong.pos }}</span>
                <span>{{ currentSong.artist }}</span>
                <span>{{ currentSong.album }}</span>
                <span>{{ currentSong.title }}</span>
                <span>
                  <span v-for="n in Number(currentSong.rate)" :key="n">
                     *
                  </span>
                </span>
            </template>
        </div>
        <br>
        <Playlist />
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Playlist from './Playlist.vue'
export default{
  name: 'Home',
  components: {
    Playlist
  },
  computed: {
    ...mapGetters(['currentSong', 'connection'])
  },
  methods: {
  },
  created () {
  }
}
</script>

<style scoped>
#currentSong {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
</style>
