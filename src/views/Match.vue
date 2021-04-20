<template>
  <div>
    <div  v-if="loading">
      <div class="row-div2" v-for="faction in matchIndex" :key="faction">

          <div class="wide-table">
            <h3>{{faction.factionName}}</h3>
            <horizontal-scroll class="horizontal-scroll">

              <table>
                <tr>
                  <th>會戰編號</th>
                  <th>發生時間</th>
                  <th>持續時間</th>
                  <th>進攻人數</th>
                  <th>防守人數</th>
                  <th>初始狀態</th>
                  <th>結束狀態</th>
                </tr>
                <tr v-for="match in faction.matchList" :key="match">
                  <td><router-link class="player-link" v-bind:to="'/match/'+match.id">{{match.id}}</router-link></td>
                  <td>{{format_time(match.startTime)}}</td>
                  <td>{{format_past_time(match.endTime-match.startTime)}}</td>
                  <td>{{match.atk}}</td>
                  <td>{{match.def}}</td>
                  <td>第 <b>{{match.initCastle[0]}}</b> 層 <b>{{match.initCastle[1]}}</b></td>
                  <td>第 <b>{{match.finalCastle[0]}}</b> 層 <b>{{match.finalCastle[1]}}</b></td>
                </tr>
              </table>
            </horizontal-scroll>
          </div>

        </div>

      </div>
    <div v-if="!loading">
      資料載入中，若等候過久請嘗試重新整理頁面
    </div>

  </div>

</template>

<script>
import api from "@/api";
import HorizontalScroll from 'vue-horizontal-scroll'
import 'vue-horizontal-scroll/dist/vue-horizontal-scroll.css'

export default {
  name: "Match",
  components: {
    HorizontalScroll
  },
  data() {
    return {
      loading: false,
      matchIndex: [
        {
          factionName: "吳",
          matchList: [
            {
              id: "B_001",
              startTime: 234567890,
              endTime: 1234567890,
              atk: 34,
              def: 3,
              initCastle: [1, 2400],
              finalCastle: [2, 2400]
            }
          ]
        }
      ]
    }
  },
  watch: {
    "$store.state.round": async function () {
      this.loading = false
      this.matchIndex = await api.getData(  "MatchIndex.json")
      this.loading = true

    },
  },
  mounted: async function () {


    this.matchIndex = await api.getData( "MatchIndex.json")
    this.loading = true
  },
  methods: {
    format_time(ori_time) {
      return (new Date(ori_time)).toLocaleString()
    },
    format_past_time(ori_time) {
      let text = ''
      if (Math.floor(ori_time / 1000 / 60 / 60) > 0) {
        text = text + Math.floor(ori_time / 1000 / 60 / 60) + '時'
      }
      if (Math.floor(ori_time / 1000 / 60) % 60 > 0) {
        text = text + Math.floor(ori_time / 1000 / 60) % 60 + '分'
      }
      if (Math.floor(ori_time / 1000) % 60 > 0) {
        text = text + Math.floor(ori_time / 1000) % 60 + '秒'
      }
      return text
    }
  }
}
</script>

<style scoped lang="scss">

h3{
  min-width: 100%;
}

.player-link:hover{
  text-decoration: underline;
}

.horizontal-scroll {
  display: flex;
  width: 100%;

}
</style>