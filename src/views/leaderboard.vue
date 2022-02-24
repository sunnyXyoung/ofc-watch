<template>
  <v-container>
    <v-row>
      <v-col
          cols="2"
      >
        <v-card>
          <v-card-title>目錄</v-card-title>
            <v-list-item
                dense
                v-for="n in 10"
                :key="n"
                @click="alert_m(n)"
            >
              {{ n }}
            </v-list-item>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
// @ is an alias to /src


export default {
  name: 'Home',
  data() {
    return {

    }
  },
  mounted() {


  },
  methods: {
    alert_m(n){
        alert(n)
    }
  },
  components: {

  }
}
</script>