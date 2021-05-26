<template>
  <div id="app">
    <HelloWorld msg="SYSTEM KOLEJKOWY"/>
    <div class="widget">

          <chart1/>

    </div>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import chart1 from "./components/chart1.vue";

export default {
  name: 'App',
  components: {
    HelloWorld,
    chart1
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
