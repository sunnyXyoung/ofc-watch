<template>
  <div>
    <RanksMenu></RanksMenu>
    <p>小提示：可以使用瀏覽器的「尋找」功能，更快地找到想要的資料喔！</p>
    <h1>戰鬥員查詢</h1>
    <div class="row-div2" id="pusher" v-if="loading">
      <v-select label="name" id="search-bar" class="reverse" style="display: block" @input="setSelected"
                :options="players" :reduce="name => name.id"></v-select>
    </div>
    <div v-if="!loading"><p>資料載入中</p></div>

  </div>

</template>

<script>
import RanksMenu from '@/components/RanksMenu.vue'
import 'vue-select/dist/vue-select.css';
import api from "@/api";


export default {
  name: "Fighter",
  components: {
    RanksMenu
  },
  watch: {
    "$store.state.round": async function () {
      this.loading = false
      this.players = await api.getData("Players.json")
      this.loading = true
    },
  },
  data() {
    return {
      loading: true,
      players: [
        {
          name: "Kulimi",
          id: 32
        },
        {
          name: "Kulimi2",
          id: 1
        },

      ]
    }
  },
  methods: {
    setSelected(id) {
      this.$router.push('/player/'+id)
    }
  },
  mounted: async function () {
    this.players = await api.getData("Players.json")
    this.loading = true
  }
}


</script>

<style scoped lang="scss">
#search-bar {

  width: 50%;

  @include phone-width {
    width: 90%;
  }
  @include small-pad-width {
    width: 90%;
  }
}

#pusher {
  position: absolute;
  z-index: 1;
}


</style>