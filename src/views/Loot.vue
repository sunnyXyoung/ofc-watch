<template>
  <div v-if="loading">
    黃底的樓層獎勵資料非來自搜集的戰報。
    <RanksMenu></RanksMenu>
    <div class="row-div2" style="margin-bottom: 50px; ">
      <table cellpadding="3">
        <tr>
          <th>層數</th>
          <th>種類</th>
          <th>品質</th>
          <th>名稱</th>
          <th>攻擊</th>
          <th>防禦</th>
          <th>挖礦</th>
          <th>出場次數</th>
        </tr>
        <tr v-for="(item) in laList" :key="item">
          <div v-bind:class="{unknown: item.isUnknown}">
            <td>{{ item.floor }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.quality }}</td>
            <td>{{ item.type }}
            <td>{{ item.atk }}</td>
            <td>{{ item.def }}</td>
            <td>{{ item.minePower }}</td>
            <td>{{ item.times }}</td>
          </div>
        </tr>
      </table>
    </div>
    <div class="row-div2">
      <table cellpadding="3">
        <tr>
          <th>名次</th>
          <th>陣營（最終）</th>
          <th>暱稱</th>
          <th>個人獲得樓層獎勵數</th>
          <th>獲得樓層獎勵</th>
        <tr v-for="(item, index) in killBoardList" :key="item">
          <td>{{ index + 1 }}</td>
          <td>{{ item.faction }}
          <td>{{ item.name }}</td>
          <td>{{ item.times }}</td>
          <td>{{ item.loots }}</td>
        </tr>
      </table>

    </div>
  </div>
</template>

<script>
import RanksMenu from '@/components/RanksMenu.vue'
import api from "../api";

export default {
  name: "Loot",
  components: {
    RanksMenu
  },
  data() {
    return {
      loading: false,
      killBoardList: [
        {name: "Kulimi", faction: "吳", times: 48763, loots: "第一層 黑夜大衣、第一層 黑夜大衣、第一層 黑夜大衣", isUnknown: false},
        {name: "Kulidfasdfasdfasdfmi2", faction: "吳", times: 8888 ,isUnknown: false},
      ],
      laList: [
        {
          floor: 1,
          name: "火龍頭",
          quality: "垃圾般的",
          type: "水龍頭",
          atk: "8787",
          def: "7414",
          minePower: "400",
          times: "2"
        }
      ]
    }
  },
  watch: {
    "$store.state.round": async function () {
      this.loading = false
      this.killBoardList = await api.getData("Loot.json")
      this.laList = await api.getData("laList.json")
      this.loading = true
    },
  },
  mounted:async function () {
    this.killBoardList = await api.getData("Loot.json")
    this.laList = await api.getData("laList.json")
    this.loading = true
  }
}
</script>

<style scoped>
.unknown {
  background-color: rgb(255, 229, 99);
}
</style>
