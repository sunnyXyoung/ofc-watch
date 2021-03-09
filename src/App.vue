<template>


  <div id="app">
    <div id="nav">
      <div>
        <router-link class="left-btn"  to="/">首頁</router-link>|
        <router-link class="left-btn"  to="/report">戰報分析</router-link>|
        <router-link class="left-btn"  to="/fighter">戰鬥員分析</router-link>|
        <router-link class="left-btn"  to="/faction">陣營分析</router-link>|
        <router-link class="left-btn"  to="/weapon">裝備分析</router-link>|
        <router-link class="left-btn"  to="/about">關於</router-link>
      </div>
      <div class="pusher"></div>
      <div>
        <router-link class="right-btn" to="/login">登入</router-link>
      </div>
    </div>
    <select id="round-selector" v-model="round">
      <option>第四輪</option>
      <option>第五輪</option>
    </select>

    <router-view/>
  </div>
</template>
<script>

  export default {
    data (){
      return{
        round : "第五輪",

      }
    }
  }

  // export default {
  //   name: 'Home',
  //   components: {
  //    mymenu
  //   }
  // }
</script>
<style>

.row-div {
  display: flex;
  flex-flow: row;
}

.row-div2 {
  display: flex;
  width: 100%;
  justify-content: center;
  flex-flow: row;
}

a {
  text-decoration:none;
}

#app {
  width: 100%;
  flex-direction: row-reverse;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#round-selector {
  display: flex;
  flex-flow: row;
  margin-left: 50px;
}

body {
  display: flex;
}

.pusher {
  display: flex;
  flex-grow: 10;
}

#nav {
  display: flex;
  padding: 30px;
  flex-direction: row;
  text-align: left;
}

@keyframes menu-hover {
  0% {
    background-color: #ffffff;
    color: white;
    margin-left: 20px;
    margin-right: 20px;
    padding: 0px;
    border-radius: 0 10px 0 10px;
  }
  100% {
    background-color: #123456;
    color: white;
    margin-left: 10px;
    margin-right: 10px;
    padding: 10px;
    border-radius: 0 10px 0 10px;
  }

}

.left-btn:hover {
  animation-name: menu-hover;
  animation-duration: 0.5s;
  background-color: #123456;
  color: white;
  margin-left: 10px;
  margin-right: 10px;
  padding: 10px;
  border-radius: 0 10px 0 10px;

}


.left-btn {
  font-weight: bold;
  color: #2c3e50;

  margin-right: 20px;
  margin-left: 20px;
}

.left-btn.router-link-exact-active {
  color: #6c8eb0;

}

.right-btn {
  background-color: #123456;
  color: white;
  margin-left: 10px;
  margin-right: 10px;
  padding: 10px;
  border-radius: 0 10px 0 10px;
}

</style>


