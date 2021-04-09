<template>
  <div class="row-div2" id="base" >
    <div id="report-box" v-if="loading">
      <table>
        <tr><th>在 </th><td>{{report.report.location}}</td></tr>
      </table>
      <div id="info-box" class="row">

        <div class="player">
          <b><i>攻擊方</i></b>
          <table class="player-table">
            <tr><th>陣營</th><td>{{report.report.aFactionName}}</td></tr>
            <tr><th>名稱</th><td>{{report.report.messages.stats.a.name}}</td></tr>
            <tr><th>職業</th><td>{{report.report.messages.stats.a.role}}</td></tr>
            <tr><th>副職</th><td>{{report.report.messages.stats.a.role2}}</td></tr>
            <tr><th>HP</th><td>{{report.report.messages.stats.a.hp}}</td></tr>
            <tr><th>熟練</th><td>{{report.report.messages.stats.a.fightExp}}</td></tr>
            <tr><th>ID</th><td>{{report.report.aId}}</td></tr>
            <tr><th>裝備</th><td><p v-for="(item) in report.report.messages.stats.a.equipments" :key="item">
              {{item.quality}}的 <b>{{item.name}}</b>（{{item.type}}）<b>攻擊</b>{{item.atk}}、<b>防禦</b>{{item.def}}、<b>礦力</b>{{item.minePower}}
            </p></td></tr>
         </table>
        </div>
        <div class="player">
          <b><i>防守方</i></b>
          <table class="player-table">
            <tr><th>陣營</th><td>{{report.report.bFactionName}}</td></tr>
            <tr><th>名稱</th><td>{{report.report.messages.stats.b.name}}</td></tr>
            <tr><th>職業</th><td>{{report.report.messages.stats.b.role}}</td></tr>
            <tr><th>副職</th><td>{{report.report.messages.stats.b.role2}}</td></tr>
            <tr><th>HP</th><td>{{report.report.messages.stats.b.hp}}</td></tr>
            <tr><th>熟練</th><td>{{report.report.messages.stats.b.fightExp}}</td></tr>
            <tr><th>ID</th><td>{{report.report.bId}}</td></tr>
            <tr><th>裝備</th><td><p v-for="(item) in report.report.messages.stats.b.equipments" :key="item">
              {{item.quality}}的 <b>{{item.name}}</b>（{{item.type}}）<b>攻擊</b>{{item.atk}}、<b>防禦</b>{{item.def}}、<b>礦力</b>{{item.minePower}}
            </p></td></tr>
          </table>
        </div>
      </div>
      <hr align="center" width="87%" style="margin-bottom: 25px;margin-top: 25px;border-color: rgba(12, 34, 56, 0.5)">
      <div id="message-box">
        <p>{{format_time}}</p>
        <table id="message-table">
          <tr v-for="(item, index) in report.report.messages.messages" :key="item">
            <th>{{index+1}}</th><td :class="item.s">{{item.m}}</td>
          </tr>
        </table>
      </div>
    </div>
    <div v-if="!loading"><p>正在載入戰報</p></div>
  </div>

</template>

<script>
import api from "@/api";

export default {
  name: "History",
  components: {},
  data() {
    return {
      loading: true,
      format_time: "",
      report: {
        "report": {
          "id": 8787,
          "messages": {
            "messages": [{
              "m": "魔三玖使出火球術，對聖光會阿阿阿阿阿造成 375 點傷害",
              "s": "skill"
            }, {"m": "聖光會阿阿阿阿阿被擊殺身亡了，魔三玖還有 250 點體力", "s": "critical"}, {
              "m": "BLUE CLAPPER耗損了 2 點耐久",
              "s": "info"
            }, {"m": "單手錘耗損了 5 點耐久", "s": "info"}, {"m": "單手錘耗損了 4 點耐久", "s": "info"}, {
              "m": "魔三玖獲得了 21 點經驗值",
              "s": "info"
            }, {"m": "聖光會阿阿阿阿阿獲得了 8 點經驗值", "s": "info"}],
            "stats": {
              "a": {
                "name": "魔三玖",
                "role": "戰鬥員",
                "hp": 250,
                "fightExp": 4362,
                "equipments": [{
                  "name": "單手錘",
                  "quality": "上等",
                  "type": "賢者魔杖",
                  "atk": 1099,
                  "def": 614,
                  "minePower": 294
                }, {"name": "單手錘", "quality": "上等", "type": "賢者魔杖", "atk": 499, "def": 1280, "minePower": 182}],
                "role2": "斥候"
              },
              "b": {
                "name": "聖光會阿阿阿阿阿",
                "role": "戰鬥員",
                "hp": 205,
                "fightExp": 1135,
                "equipments": [{
                  "name": "BLUE CLAPPER",
                  "quality": "頂級",
                  "type": "長槍",
                  "atk": 1778,
                  "def": 1432,
                  "minePower": 255
                }],
                "role2": "長槍使"
              }
            }
          },
          "location": "鋼之鍊金術師的城堡",
          "time": 1616597661294,
          "aFactionName": "進擊的巨人",
          "bFactionName": "鋼之鍊金術師",
          "aName": "魔三玖",
          "bName": "聖光會阿阿阿阿阿",
          "aId": 398,
          "bId": 414,
          "aBadgeColor": null,
          "bBadgeColor": null
        }
      }

    }
  },

  mounted: async function () {
    this.report = await api.getReport(this.$route.params.round + "/" + this.$route.params.id + ".json")
    this.format_time = (new Date(this.report.report.time)).toLocaleString()
    this.loading = true
  }

}
</script>

<style scoped lang="scss">

#report-box{
  box-shadow:3px 3px 5px 6px #cccccc;
  width: 60%;
  min-width: 250px;
  padding: 30px;
}
.player{
  width: 50%;
  display: flex;
  text-align: left;
  flex-flow: column;
  background-color: rgb(254, 255, 255);
  @include phone-width{
    width: 100%;
  }
  @include small-pad-width {
    width: 100%;
  }
}

.player-table > tr > td{
  display: flex;
  flex-flow: column;
  text-align: left;
  padding-left: 20px;
}

#message-table > tr > td{
  display: flex;
  flex-flow: column;
  text-align: left;
  padding-left: 12px;
}

.player-table > tr > th{
  min-width: 50px;
}

.player-table > tr > td > p{
  margin: 0;
}


#base{
  margin-bottom: 20px;
}


.row{
  display: flex;
  flex-direction: row;
  @include phone-width{
    flex-flow: column;
  }
  @include small-pad-width {
    flex-flow: column;
  }
}

.skill{
  color: #00887e;
}

.info{
  color: #006da7;
}

.critical{
  color: #ff1200;
}


</style>