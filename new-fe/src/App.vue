<template>
  <v-app id="inspire">
    <v-app-bar
        app
        color="white"
        flat
    >
      <v-container class="py-0 fill-height align-center ">
        <!--        <v-avatar-->
        <!--            class="mr-10"-->
        <!--            color="grey darken-1"-->
        <!--            size="32"-->
        <!--        ></v-avatar>-->




            <v-col>
              <v-row>
                <v-col
                    v-for="(link, text) in links"
                    :key="text"
                    cols="auto"
                >
                  <v-btn
                      :to="link"
                      text
                      class="text-body-1"
                  >
                    {{ text }}
                  </v-btn>
                </v-col>

                <v-col>
                  <v-responsive max-width="260">
                    <v-text-field
                        dense
                        flat
                        hide-details
                        rounded
                        solo-inverted
                    ></v-text-field>
                  </v-responsive>
                </v-col>
                <v-col>
                  <v-select :items="options"
                            v-model="round"
                            label="請選擇輪數"
                            dense
                            solo
                  ></v-select>
                </v-col>

              </v-row>
            </v-col>

      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <!--        <v-row>-->
        <!--          <v-col cols="2">-->
        <!--            <v-sheet rounded="lg">-->
        <!--              <v-list color="transparent">-->
        <!--                <v-list-item-->
        <!--                    v-for="n in 5"-->
        <!--                    :key="n"-->
        <!--                    link-->
        <!--                >-->
        <!--                  <v-list-item-content>-->
        <!--                    <v-list-item-title>-->
        <!--                      List Item {{ n }}-->
        <!--                    </v-list-item-title>-->
        <!--                  </v-list-item-content>-->
        <!--                </v-list-item>-->

        <!--                <v-divider class="my-2"></v-divider>-->

        <!--                <v-list-item-->
        <!--                    link-->
        <!--                    color="grey lighten-4"-->
        <!--                >-->
        <!--                  <v-list-item-content>-->
        <!--                    <v-list-item-title>-->
        <!--                      Refresh-->
        <!--                    </v-list-item-title>-->
        <!--                  </v-list-item-content>-->
        <!--                </v-list-item>-->
        <!--              </v-list>-->
        <!--            </v-sheet>-->
        <!--          </v-col>-->

        <!--          <v-col>-->
        <v-sheet
            min-height="70vh"
            rounded="lg"
        >
          <router-view/>
        </v-sheet>
        <!--          </v-col>-->
        <!--        </v-row>-->
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: function () {
    return {
      round: 6,
      options: [
        {text: '第四輪', value: '4'},
        {text: '第五輪', value: '5'},
        {text: '幕間劇場', value: '5.5'},
        {text: '第六輪', value: '6'}
      ],
      links: {
        "OFC Watch": "/",
        "排行榜": "scoreboard",
        "個人頁面": "user",
        "關於": "about",

      }
    }
  },
};
</script>
<style>
router-link {
  color: black;
}
</style>