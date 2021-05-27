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

    <div>
      <dropdown :options="queues_name" :selected="object" v-on:updateOption="methodToRunOnSelect"></dropdown>

    </div>

  </div>

    </template>

<script>
import axios from 'axios';
import dropdown from 'vue-dropdowns';

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
      queues_name:null,
    object: {
              name: 'Object Name',
            }}
  },
          components: {
            'dropdown': dropdown,
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
            this.getCurrentStatus()

    }, err => {
      this.gettingLocation = false;
      this.errorStr = err.message;
    })
    // Make axios CALL

        })



  },
  methods: {
    methodToRunOnSelect(payload) {
            this.object = payload;
          },
    getCurrentStatus: function () {
      axios
      .get('https://kolejki.herokuapp.com/1')
          .then(response => {
            console.log(response)
            var tmp_res = response.data
            this.queues_name = []
            tmp_res.forEach(function (value){
              this.queues_name.push(value[3])
            })
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
