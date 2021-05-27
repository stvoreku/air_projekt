<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

  <div class="widget" v-if="errorStr">
    Sorry, but the following error
    occurred: {{errorStr}}
  </div>


    <div class="widget" v-if="place">
        Najbliższa placówka to {{place}}, znajduje się w odległości {{distance}}


    </div>

        <div class="widget" v-if="queues_name">
        {{queues_name}}


    </div>

  </div>

    </template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
    data: function (){
    return {location:null,
    gettingLocation: false,
    errorStr:null,
    place:null,
    distance:null,
      queues_name:null,}
  },
    created() {
    //do we support geolocation
    if(!("geolocation" in navigator)) {
      this.errorStr = 'Geolocation is not available.';
      return;
    }

    this.gettingLocation = true;
    // get position
    navigator.geolocation.getCurrentPosition(pos => {
      this.gettingLocation = false;
      this.location = pos;
      console.log(pos)

     const req = JSON.stringify({x:pos.coords.latitude, y:pos.coords.longitude})


      axios
        .post('https://kolejki.herokuapp.com/', req)
        .then(response => {
            console.log(response)
            this.place = response.data.place_name
            this.distance = response.data.distance
          this.queues_name = this.getCurrentStatus()

    }, err => {
      this.gettingLocation = false;
      this.errorStr = err.message;
    })
    // Make axios CALL

        })



  },
  methods: {
    getCurrentStatus: function () {
      axios
      .get("https://api.um.warszawa.pl/api/action/wsstore_get/?id=bc83ab5a-0ccc-4e4a-b58d-b821e16df176")
          .then(response => {
            console.log(response)
    }, err => {
      this.gettingLocation = false;
      this.errorStr = err.message;
    })
      console.log('aaa')
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
