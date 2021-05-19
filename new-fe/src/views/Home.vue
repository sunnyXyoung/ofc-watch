<template>
  <div class="app-container">
    <div id="side-bar">
      links <br>links <br>vlinks <br>links <br>links <br>
    </div>
    <div class="home">
      <img alt="ofc logo" id="logo" src="../assets/big-eye.png">
      <h1>歡迎來到 OFC Watch</h1>
      今日戰報數：{{news.count}}，第{{news.day}}天。
      <div>
        近期事件：

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

#logo{
  width: 70%;
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
