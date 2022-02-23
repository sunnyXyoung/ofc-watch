<template>
<!--          <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg">-->
  <v-app id="inspire">
    <v-app-bar
        app
        color="white"
        flat
    >
      <v-container class="py-0 fill-height">

        <v-btn
            text
            to="/"
        >
          OFC WATCH
        </v-btn>

        <v-btn
            v-for="link in links"
            :key="link"
            :to=link.path
            text
        >
          {{ link.label }}
        </v-btn>
        <v-responsive max-width="260">
          <v-select
              dense
              flat
              hide-details
              rounded
              solo-inverted
              :items="options"
          >
          </v-select>
        </v-responsive>
        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-text-field
              dense
              flat
              hide-details
              rounded
              solo-inverted
              v-model=search_text
              append-icon="mdi-eye"
              @keydown.enter.prevent="send_search"
          ></v-text-field>

        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3 fill-height">
      <v-container>


        <router-view></router-view>

      </v-container>

        <v-footer
            fixed
            dense
            padless
        >
          <v-card-text
              class="text-center"

          >Copyright © {{ new Date().getFullYear() }}  ofc-watch.kulimi.tw All rights reserved.</v-card-text>
        </v-footer>

    </v-main>
  </v-app>
<!--              </v-parallax>-->
</template>

<script>
import router from "./router";

export default {
  data() {
    return {
      search_text: "",
      options: [
        {text: '第四輪', value: '4'},
        {text: '第五輪', value: '5'},
        {text: '幕間劇場', value: '5.5'},
        {text: '第六輪', value: '6'},
        {text: '第七輪 端午亂鬥', value: '7'},
        {text: '第八輪 疫苗亂鬥', value: '8'},
        {text: '第九輪 吳剛', value: '9'},
        {text: '第十輪 bang利商店大亂鬥', value: '10'},
        {text: '第十二輪 年夜飯', value: '11'}
      ],
      links: [
        {label: '玩家', path: "Dashboard"},
        {label: '會戰', path: "Messages"},
        {label: '訊息牆', path: "Profile"},
        {label: '關於', path: "Updates"},
      ],
    }
  },
  methods: {
    send_search() {
      router.replace("/")

      router.replace({name: "Search", params: {payload: this.search_text}})
      // alert(0)
    }
  }
  ,
}
</script>
<style>
html {
  height: 100%;
  font-family: "Helvetica", "Arial","LiHei Pro","黑體-繁","微軟正黑體", sans-serif;
}
body {
  height: 100%;
}

</style>