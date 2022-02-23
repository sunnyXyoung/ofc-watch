<template>
  <v-container>
    <v-row>
      <v-col cols="6">
        <v-card
            class="pa-10"
        >

          <img alt="Vue logo" src="../assets/big-eye.png" class="eye">
          <h1>Our Floating Castle Watcher</h1>
          <h1>我們的浮游城 觀察者</h1>
        </v-card>

        <v-card>
          <v-card-title>裝備種類統計</v-card-title>
          <v-list
              style=" overflow-y: scroll"
          >
            <v-list-item
                v-for="n in 10"
                :key="n"
            >
              <v-list-item-content>
                <v-list-item-title>{{n}} Single-line item</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>

      </v-col>
      <v-col cols="6">
        <v-card>
          <v-card-title>最新事件</v-card-title>
          <v-list
              style=" overflow-y: scroll"
          >
            <v-list-item
                v-for="n in 10"
                :key="n"
            >
              <v-list-item-content>
                <v-list-item-title>{{n}} Single-line item</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
          <v-container class="max-width">
            <v-pagination
                v-model="page"

                :length="100"
            ></v-pagination>
          </v-container>
        </v-card>

        <v-card>
          <v-card-title>狩獵</v-card-title>

        </v-card>
      </v-col>

    </v-row

    >
  </v-container>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  data() {
    return {
      page: 200000,
    }
  },
  mounted() {


  },
  components: {

  }
}
</script>

<style scoped lang="scss">

@keyframes eye-open {
  0%{
    transform: matrix(1, 0, 0, 0, 0, 0);
  }
  50%{
    transform: matrix(1, 0, 0, 0.0001, 0, 0);
  }
  60%{
    transform: matrix(1, 0, 0, 0.3, 0, 0);
  }
  70%{
    transform: matrix(1, 0, 0, 0.3, 0, 0);
  }
  80%{
    transform: matrix(1.01, 0, 0, 0.01, 0, 0);
  }

  100% {
    transform: matrix(1, 0, 0, 1, 0, 0);
  }
}

.eye{
  width: 500px;
  height: 500px;
  animation-name: eye-open;
  animation-duration: 2.5s;

}

.eye2{
  width: 500px;
  height: 500px;
  //animation-name: eye-open;
  //animation-duration: 2.5s;

}

</style>
