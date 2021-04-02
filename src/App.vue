<template>
  <div id="app">
    <div id="nav">
      <div>
        <router-link class="left-btn" to="/">首頁</router-link>
        |
        <router-link class="left-btn" to="/report">戰報分析</router-link>
        |
        <router-link class="left-btn" to="/fighter">戰鬥員分析</router-link>
        |
        <router-link class="left-btn" to="/faction">陣營分析</router-link>
        |
        <router-link class="left-btn" to="/weapon">裝備分析</router-link>
        <!--        |
                <router-link class="left-btn" to="/about">關於</router-link>-->
      </div>
      <div class="pusher"></div>
      <div>
        <router-link class="right-btn" to="/about">關於</router-link>
      </div>
    </div>
    <div class="navbar-toggler" style="border: none;text-align: right">
      <i @click="SideBarOn" class="fa fa-navicon fa-lg" style="cursor: pointer"></i>
    </div>
    <div v-if="sidebar" @click="SideBarOn" class="black-layout"></div>
    <transition>
      <div v-if="sidebar" id="sidebar-nav" :class="{'nav-show':sidebar}">
        <ul class="navbar-nav" style="display: inline-block;width: 100%">
          <li class="nav-item sidebar-item" @click="SideBarOn">
            <router-link class="sidebar-link" to="/">首頁</router-link>
          </li>
          <li class="nav-item sidebar-item" @click="SideBarOn">
            <router-link class="sidebar-link" to="/report">戰報分析</router-link>
          </li>
          <li class="nav-item sidebar-item" @click="SideBarOn">
            <router-link class="sidebar-link" to="/fighter">戰鬥員分析</router-link>
          </li>
          <li class="nav-item sidebar-item" @click="SideBarOn">
            <router-link class="sidebar-link" to="/faction">陣營分析</router-link>
          </li>
          <li class="nav-item sidebar-item" @click="SideBarOn">
            <router-link class="sidebar-link" to="/weapon">裝備分析</router-link>
          </li>
          <li class="nav-item sidebar-item" @click="SideBarOn">
            <router-link class="sidebar-link" to="/about">關於</router-link>
          </li>
        </ul>
      </div>
    </transition>
    <select id="round-selector" v-model="round" @change="ChangeRound">
      <option v-for="option in options" :key="option.value" :value="option.value" >
        {{ option.text }}
      </option>

    </select>

    <router-view/>
  </div>
</template>
<script>


export default {
  data() {

    // this.$store.commit("ChangeRound");
    return {
      round: this.$store.state.round,
      options: [
        {text: '第四輪', value: '4'},
        {text: '第五輪', value: '5'},
        {text: '幕間劇場', value: '6'}
      ],
      sidebar: false

    }
  },

  methods: {
    ChangeRound() {
      this.$store.commit("ChangeRound", this.round);
    },
    SideBarOn() {
      this.sidebar = (!this.sidebar);
    }
  },
  mounted() {
//     if (this.$cookies.isKey("round")) {
//       this.$store.commit("ChangeRound", this.$cookies.get("round"))
//     }
//     else {
//       this.$cookies.set("round", this.$store.state.round)
//     }
    const round = localStorage.getItem("round");
    if (round) {
      this.round = round
    }
    else {
      this.$store.commit("ChangeRound", this.round)
    }
  }
}


</script>
<style lang="scss">

.row-div {
  display: flex;
  flex-flow: row;
  justify-content: center;
  width: 100%;
}

.row-div2 {
  display: flex;
  width: 100%;
  justify-content: center;
  flex-flow: row;
  flex-wrap: wrap;
}

a {
  text-decoration: none;
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
  @include phone-width{
    display: none;
  }
  @include small-pad-width{
    display: none;
  }
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

.charts{
  width: 40%;
  @include phone-width{
    width: 90%;
  }
  @include small-pad-width{
    width: 100%;
  }
  @include pad-width{
    width: 100%;
  }
  @include pc-width{
    width: 80%
  }
}

.navbar-toggler{
  display: none;
  @include phone-width{
    display: block;
  }
  @include small-pad-width{
    display: block;
  }
}

.sidebar-link {
  font-size: x-large;
  font-weight: bold;
  color: #2c3e50;
  display: flex;
  width: 85%;
  margin: auto;
  align-items: center;
  justify-content: left;
  @include pad-width{
    font-size: 35px;
  }
  @include small-pad-width{
    font-size: 35px;
  }
  @include phone-width{
    font-size: 20px;
  }
}

.black-layout {
  position: fixed;
  top: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 2;
  width: 100%;
  height: 100%;
}

#sidebar-nav {
  position: fixed;
  top: 0;
  background: white;
  z-index: 3;
  width: 45%;
  height: 100%;
  text-align: center;
  padding-top: 5%;
  @include pad-width{
    width: 40%;
  }
  @include small-pad-width{
    width: 40%;
  }
  @include pc-width{
    width: 20%;
  }
  @include big-pc-width{
    width: 20%;
  }
}
.nav-show{
  right: 0;
}
.v-enter{
  right: -55%;
  @include pad-width{
    right: -40%;
  }
  @include small-pad-width{
    right: -40%;
  }
  @include pc-width{
    right: -20%;
  }
  @include big-pc-width{
    right: -20%;
  }
}
.v-enter-active{
  transition: all ease 0.4s;
}
.v-enter-to{
  right: 0;
}

</style>


