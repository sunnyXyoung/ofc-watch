<template>
<div>
  <RanksMenu></RanksMenu>
  <div class="row-div2">
    <table cellpadding="3">
      <tr>
        <th>名次</th><th>陣營（最終）</th><th>暱稱</th><th>出戰次數</th>
      <tr v-for="(item, index) in killBoardList" :key="item">
        <td>{{ index+1 }}</td><td>{{item.faction}}<td>{{ item.name }}</td><td>{{ item.times }}</td>
      </tr>
    </table>

  </div>
</div>
</template>

<script>
import RanksMenu from '@/components/RanksMenu.vue'
export default {
name: "Times",
  components:{
    RanksMenu
  },
  data() {
    return {
      killBoardList: [
        {name: "Kulimi",faction:"吳", times: 48763},
        {name: "Kulidfasdfasdfasdfmi2",faction:"吳", times: 8888},
      ]
    }
  },
  mounted: function () {
    var jsonify = res => res.json();
    fetch(
        "http://localhost:3000/Killed.json"
    ).then(jsonify).then(data => {
      this.killBoardList = data
    });

  }
}
</script>

<style scoped>

</style>