<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
<div class="widget"> TU BEDZIE JAKIES LOGO CZY NAZWA</div>

  <div class="widget" v-if="errorStr">
    Sorry, but the following error
    occurred: {{errorStr}}
  </div>

  <div class="widget" v-if="gettingLocation">
    <i>Getting your location...</i>
  </div>

  <div class="widget" v-if="location">
    Your location data is {{ location.coords.latitude }}, {{ location.coords.longitude}}
  </div>

    <div class="widget" v-if="place">
        Najbliższa placówka to {{place}}, znajduje się w odległości {{distance}}


    </div>
    <div class="widget">
        Czy to ptak? Czy to samolot? Nie, tu będzie wykresik


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
    distance:null,}
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

    }, err => {
      this.gettingLocation = false;
      this.errorStr = err.message;
    })
    // Make axios CALL

        })



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
