<template>
  <div>
    <h3>Bookmarks</h3>
    <button v-on:click="creator()">Add bookmark</button>
    <form v-show="showCreator" action="">
      <input v-model="payload.name" type="text" placeholder="name">
      <input v-model="payload.url" type="text" placeholder="url">
      <p>Adding: {{ payload.name }} with address: {{ payload.url }}</p>
      <button v-on:click="postBookmark(payload)">Add</button>
    </form>
    <ul>
      <li v-for="bookmark in bookmarks" :key="bookmark.name"><a :href="bookmark.url">{{ bookmark.name }}</a></li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default{
  name: 'Bookmarks',
  data () {
    return {
      showCreator: false,
      payload: {
        name: '',
        url: ''
      }
    }
  },
  methods: {
    ...mapActions(['getBookmarks', 'postBookmark']),
    creator () {
      this.showCreator = !this.showCreator
    }
  },
  computed: {
    ...mapGetters(['bookmarks'])
  },
  created () {
    this.getBookmarks()
  }
}
</script>

<style scoped>

</style>
