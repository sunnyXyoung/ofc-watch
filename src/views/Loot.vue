<template>
  <div>
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
          <th>耐久（最低）</th>
          <th>出場次數</th>
        </tr>
        <tr v-for="(item) in laList" :key="item">
          <td>{{ item.floor }}</td>
          <td>{{ item.type }}
          <td>{{ item.quality }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.attack }}</td>
          <td>{{ item.defence }}</td>
          <td>{{ item.minepower }}</td>
          <td>{{ item.durability }}</td>
          <td>{{ item.times }}</td>
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

export default {
  name: "Loot",
  components: {
    RanksMenu
  },
  data() {
    return {
      killBoardList: [
        {name: "Kulimi", faction: "吳", times: 48763, loots: "第一層 黑夜大衣、第一層 黑夜大衣、第一層 黑夜大衣"},
        {name: "Kulidfasdfasdfasdfmi2", faction: "吳", times: 8888},
      ],
      laList: [
        {
          floor: 1,
          type: "水龍頭",
          quality: "垃圾般的",
          name: "火龍頭",
          attack: "8787",
          defence: "7414",
          minepower: "400",
          durability: "2234",
          times: "2"
        }
      ]
    }
  },
  mounted: function () {
    var jsonify = res => res.json();
    fetch(
        "./" + this.$store.state.round + "/Loot.json"
    ).then(jsonify).then(data => {
      this.killBoardList = data
    });
    fetch(
        "./" + this.$store.state.round + "/laList.json"
    ).then(jsonify).then(data => {
      this.laList = data
    });

  }
}
</script>

<style scoped>

</style>