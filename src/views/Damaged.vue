<template>
<div>
  <RanksMenu></RanksMenu>
  <div class="row-div2">
    <table>
      <tr>
        <th>名次</th><th>暱稱</th><th>承受傷害</th>
      <tr v-for="(item, index) in killBoardList" :key="item">
        <td>{{ index+1 }}</td><td>{{ item.name }}</td><td>{{ item.damaged }}</td>
      </tr>
    </table>

  </div>
</div>
</template>

<script>
import RanksMenu from '@/components/RanksMenu.vue'
export default {
name: "Damaged",
  components:{
    RanksMenu
  },
  data() {
    return {
      killBoardList: [
        {name: "Kulimi", damaged: 48763},
        {name: "Kulidfasdfasdfasdfmi2", damaged: 8888},
      ]
    }
  },
  mounted: function () {
    var jsonify = res => res.json();
    fetch(
        "http://localhost:3000/Damaged.json"
    ).then(jsonify).then(data => {
      this.killBoardList = data
    });

  }
}
</script>

<style scoped>

</style>