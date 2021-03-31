<template>
  <div>
    <RanksMenu></RanksMenu>
    <div class="row-div2">
      <table cellpadding="3">
        <tr>
          <th>名次</th>
          <th>陣營（最終）</th>
          <th>暱稱</th>
          <th>造成傷害</th>
        <tr v-for="(item, index) in killBoardList" :key="item">
          <td>{{ index + 1 }}</td>
          <td>{{ item.faction }}
          <td>{{ item.name }}</td>
          <td>{{ item.damage }}</td>
        </tr>
      </table>

    </div>
  </div>
</template>

<script>
import RanksMenu from '@/components/RanksMenu.vue'
import api from "../api";

export default {
  name: "CastleDamage",
  components: {
    RanksMenu
  },
  data() {
    return {
      killBoardList: [
        {name: "Kulimi", faction: "吳", damage: 48763},
        {name: "Kulidfasdfasdfasdfmi2", faction: "吳", damage: 8888},
      ]
    }
  },
  mounted: async function () {
    this.killBoardList = await api.getData("CastleDamage.json")
  }
}
</script>

<style scoped>

</style>
