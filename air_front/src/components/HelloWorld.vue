<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

  <div class="widget" v-if="errorStr">
    Sorry, but the following error
    occurred: {{errorStr}}
  </div>

    <div class="widget" v-if="place">
Sprawdź aktualną zajętość kolejki w urzędzie lub zaplanuj wizytę w najmniej uczęszczanych godzinach. Aby rozpocząć,
      wybierz urząd lub zezwól aplikacji na dostęp do lokalizacji, aby znalazła najbliższy z dostępnych.

    </div>

    <div class="widget" v-if="place">
        Najbliższa placówka to {{place}}, znajduje się w odległości {{distance}}km


    </div>

    <div class="widget" v-if="queues_name">
      <dropdown :options="queues_name" :selected="object" v-on:updateOption="methodToRunOnSelect"></dropdown>

    </div>

        <div class="widget" v-if="places_name">
      <dropdown :options="places_name" :selected="place_obj" v-on:updateOption="places_methodToRunOnSelect"></dropdown>

    </div>

    <div class="widget">
      Aktualna liczba osób w kolejce: {{object.queue_len}}. Aktualny numerek kolejki: {{object.curr_num}}
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
      places_name: ['a','b'],
    object: {
              name: 'Object Name',
              queue_len: null,
              curr_num: null
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
            this.$parent.plotX = [1,2,3,4,5]
            this.$parent.plotY = [1,3,4,5,6]
            console.log(this.$parent.plotY)
            console.log(this.object)
          },
    getCurrentStatus: function () {
      axios
      .get('https://kolejki.herokuapp.com/1')
          .then(response => {
            console.log(response)
            var tmp_res = response.data.queues
            console.log('GOT LIST?')
            console.log(tmp_res)
            //this.queues_name = []
            var tmp_list = []
            tmp_res.forEach(function (value){
              tmp_list.push({'name': value[2], 'queue_len': value[4], 'curr_num': value[5]})
            })
            this.queues_name = tmp_list
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
