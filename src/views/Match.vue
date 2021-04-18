<template>
  <div>
    <div class="row-div2">
      <div v-for="faction in matchIndex" :key="faction">
        <h3>{{faction.factionName}}</h3>
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
      </div>
    </div>
  </div>

</template>

<script>
import api from "@/api";

export default {
  name: "Match",
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
    },
  },
  mounted: async function () {
    alert(this.report.dead.includes(this.report.atk_name))
    this.loading = false
    this.matchIndex = await api.getData( + "MatchIndex.json")
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
.match-report {
  display: flex;
  text-align: left;
  padding: 10px;
}

.column-line {
  min-height: 80%;
  width: 0;

  @include phone-width {
    display: none;
  }
  @include small-pad-width {
    display: none;
  }
}

.wide-table {
  padding: 10px;
  text-align: left;

  @include phone-width {
    overflow-x: scroll;
    width: 100% ;

    table {
      width: 120%;

      tr {
        * {
          flex-wrap: nowrap;
          white-space: nowrap;
        }
      }
    }
  }
  @include small-pad-width {
    overflow-x: scroll;
    width: 100% ;

    table {
      width: 120%;

      tr {
        * {
          flex-wrap: nowrap;
          white-space: nowrap;
        }
      }
    }
  }
}

.died{
  .player-link{
    color: red;
  }
}

.player-link:hover{
  text-decoration: underline;
}
</style>