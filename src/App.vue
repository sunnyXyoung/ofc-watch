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
    <div class="m-menu">
      <router-link class="m-btn" to="/"><p class="m-btn">OFC WATCH</p></router-link>
      <router-link class="m-icon" to="/report"><img class="m-img" src="./assets/history.svg" alt="戰報"></router-link>
      <router-link class="m-icon" to="/fighter"><img class="m-img"  src="./assets/man-with-two-swords.svg" alt="戰鬥員"></router-link>
      <router-link class="m-icon" to="/faction"><img class="m-img"  src="./assets/flag.svg" alt="陣營"></router-link>
      <router-link class="m-icon" to="/weapon"><img class="m-img" src="./assets/sword.svg" alt="裝備"></router-link>
      <router-link class="m-icon" to="/about"><img class="m-img"  src="./assets/information.svg" alt="關於"></router-link>
    </div>

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
    return {
      round: this.$store.state.round,
      options: [
        {text: '第四輪', value: '4'},
        {text: '第五輪', value: '5'},
        {text: '幕間劇場', value: '5.5'}
      ],
      sidebar: false

    }
  },
  watch: {
    "$store.state.dark": async function () {
      if(this.$store.state.dark){
        document.getElementsByTagName('html')[0].className="dark"
      }else {
        document.getElementsByTagName('html')[0].classList.remove('dark')
      }
    },
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
    const round = localStorage.getItem("round");
    const isDark = localStorage.getItem("dark");

    if (round === '6') {
      this.round = '5.5'
      this.$store.commit("ChangeRound", '5.5')
    }
    if (round) {
      this.round = round
    }
    else {
      this.$store.commit("ChangeRound", this.round)
    }

    if (isDark === "false") {

      this.$store.commit("ChangeTheme", false)
    }
    else {
      this.$store.commit("ChangeTheme", isDark)
    }

    if(!this.$store.state.dark){

      document.getElementsByTagName('html')[0].classList.remove('dark')
    }
    else {

      document.getElementsByTagName('html')[0].className="dark"

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



.black-layout {
  position: fixed;
  top: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 2;
  width: 100%;
  height: 100%;
}

.m-menu{
  display: none;
  width: 100%;
  height: 40px;
  box-shadow:3px 3px 5px 6px #cccccc;
  align-content: center;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-bottom: 20px;

  @include phone-width{
    display: flex;
  }
  @include small-pad-width{
    display: flex;
  }
}

body {
  margin: 0;
  height: 100%;
  width: 100%;
  max-width: 100%;
  overflow-x: hidden;
}

.m-btn{
  font-weight: bold;
  color: #2c3e50;
  display: flex;
  height: 50px;
  width: auto;
  align-content: center;
  justify-content: center;
  z-index: 2;

}

.m-icon {
  width: 30px;
  height: 50px;
  display: flex;
  align-content: center;
  justify-content: center;
}

.m-img{
  width: 30px;
  height: 50px;
}

html{
  max-width: 100%;
  overflow-x: hidden;
  font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  line-height: 1.4;
}

.dark{
  background-color: #081524;
  //.left-btn{
  //  color: white;
  //}
  //.link{
  //  color: #2ba1fe;
  //}
  //nav{
  //  background-color: #313340 !important;
  //  .navbar-brand{
  //    color: white !important;
  //  }
  //  .nav-link{
  //    color: #dedede !important;
  //    &:hover{
  //      color: #e3e3e3 !important;
  //    }
  //  }
  //}
  //#sidebar-nav{
  //  background-color: #313340 !important;
  //  .sidebar-link{
  //    color: #dedede !important;
  //  }
  //  .router-link-exact-active{
  //    color: #7885d2 !important;
  //  }
  //}
  //div,.box{
  //  color: #dedede !important;
  //}
  //.box{
  //  background-color: #313340 !important ;
  //  border-color: gray !important;
  //  input,textarea{
  //    background-color: #313340 !important;
  //  }
  //}
  //input,textarea,select{
  //  background-color: #5f6582 !important ;
  //  color: lightgray;
  //}
  //.sheets:hover{
  //  background-color: #656b8b;
  //}
  //.systems-title-tile:hover{
  //  background-color: #757aa1 !important;
  //}
  //.tab-name:hover{
  //  background-color: #757aa1 !important;
  //}
  //.active{
  //  background-color: #5f6582 !important;
  //}
  //
  //#footer{
  //  background-color: #313340 !important;
  //  color: #dedede !important;
  //  border-top: #434a5c !important;
  //}
  -webkit-filter: invert(100%) hue-rotate(180deg) contrast(3) brightness(2);
  filter: invert(100%) hue-rotate(180deg) contrast(3) brightness(2);

}

</style>
