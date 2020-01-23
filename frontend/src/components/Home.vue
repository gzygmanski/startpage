<template>
    <div>
        <h1>Home Page</h1>
        <h3>Currently playing:</h3>
        <div id="currentSong">
            <span>{{ currentSong[0].id }}</span>
            <span>{{ currentSong[0].artist }}</span>
            <span>{{ currentSong[0].album }}</span>
            <span>{{ currentSong[0].title }}</span>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default{
  name: 'Home',
  computed: {
    ...mapGetters(['currentSong'])
  },
  methods: {
    ...mapActions(['fetch'])
  },
  created () {
    this.fetch()
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
