<template>
  <div id="app">
    <div id="nav">
      <div id="menu">
        <img alt="ofc logo" id="logo" src="@/assets/big-eye.png">
        <router-link class="router-link-btn" to="/">OFC Watch</router-link>
        <router-link class="router-link-btn" to="/leaderboard">排行榜</router-link>
        <router-link class="router-link-btn" to="/about">關於</router-link>
        <div>
          <input type="text"
                 placeholder="搜尋..."
          >
        </div>
        <div>
          <select id="round-selector" v-model="round" @change="ChangeRound">
            <option v-for="option in options" :key="option.value" :value="option.value" >
              {{ option.text }}
            </option>
          </select>
        </div>
      </div>
    </div>
    <router-view/>
  </div>
</template>
<script>
export default {
  data() {
    return {
      round: 6,
      options: [
        {text: '第四輪', value: '4'},
        {text: '第五輪', value: '5'},
        {text: '幕間劇場', value: '5.5'},
        {text: '第六輪', value: '6'}
      ],
    }
  },
}
</script>
<style>
html {
}
#app {
  font-family: "Helvetica", "Arial","LiHei Pro","黑體-繁","微軟正黑體", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  display: flex;
  flex-flow: row;
  justify-content: space-around;
  padding-top: 15px;
  padding-bottom: 30px;
  width: 100%;
}
#menu{
  display: flex;
  flex-flow: row;
  justify-content: space-around;
  align-items: center;
  width: 50%;
}
.router-link-btn {
  font-weight: bold;
  color: #0c0c0c;
  text-decoration: none;
}
.router-link-btn.router-link-exact-active {
  text-decoration: underline;
}
#logo{
  width: 100px;
}

</style>