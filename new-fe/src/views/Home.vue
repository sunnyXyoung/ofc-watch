<template>
  <div class="app-container">
    <div id="side-bar">
      links <br>links <br>vlinks <br>links <br>links <br>
    </div>
    <div class="home">

      <h1>歡迎來到 OFC Watch</h1>
      最新會戰： <router-link to="/"> {{news.latest_match.id }} </router-link>
      <nav>
        <div class="nav nav-tabs" id="nav-tab" role="tablist">
          <button class="nav-link active" id="nav-home-tab" data-bs-toggle="tab" data-bs-target="#nav-home" type="button" role="tab" aria-controls="nav-home" aria-selected="true">Home</button>
          <button class="nav-link" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile" type="button" role="tab" aria-controls="nav-profile" aria-selected="false">Profile</button>
          <button class="nav-link" id="nav-contact-tab" data-bs-toggle="tab" data-bs-target="#nav-contact" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">Contact</button>
        </div>
      </nav>
      <div class="tab-content" id="nav-tabContent">
        <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab">...</div>
        <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">...</div>
        <div class="tab-pane fade" id="nav-contact" role="tabpanel" aria-labelledby="nav-contact-tab">...</div>
      </div>


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