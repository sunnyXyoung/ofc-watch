<template>
  <div class="app-container">
    <div id="side-bar">
      links <br>links <br>vlinks <br>links <br>links <br>
    </div>
    <div class="home">

      <h1>歡迎來到 OFC Watch</h1>
      最新會戰： <router-link to="/"> {{ this.news.latest_match.id }} </router-link>


    </div>
  </div>
</template>

<script>
import api from '@/api.js'
export default {
  name: 'Home',
  components: {
  },
  data(){
    return{
      news:{
        latest_match:{
          id: "民進黨001",
        },
        count: 0,
        day: 1
      }
    }
  },
  mounted: async function () {
    this.news = await api.getData("News.json")
  }
}
</script>
<style scoped>
.app-container{
  display: flex;
  justify-content: space-around;
}

.home{
  width: 60%;
}
#side-bar{
  position: fixed;
  width: 20%;
  left: 0;
  top: 60px;
}
</style>