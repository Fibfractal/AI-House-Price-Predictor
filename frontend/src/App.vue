<template>
  <div>
    <main>
      <Navbar/>
      <router-view/>
      <Footer/>
    </main>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue"
import Footer from "./components/Footer.vue"


export default {
  name: 'App',
  components: {
    Navbar,
    Footer
  },
  created() {
    this.$store.dispatch("initPredictions")
  },
}
</script>
