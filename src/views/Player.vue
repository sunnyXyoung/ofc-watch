<template>
  <div>
    <div v-if="!loading">
      資料載入中
    </div>
    <div v-if="loading">
      <h1>{{ player.name }}的個人資料</h1>
      <div class="">
        <table style="display: none">
          <tr v-if="player.id"><th>id</th><td>{{player.id}}</td></tr>
          <tr v-if="player.role"><th>職業</th><td>{{player.role}}</td></tr>
          <tr v-if="player.role2"><th>副職業</th><td>{{player.role2}}</td></tr>
          <tr v-if="player.factions"><th>陣營時間佔比</th><td><p v-for="faction in player.factions" v-bind:key="faction">{{faction.name}}: {{faction.time}}</p></td></tr>
          <tr v-if="player.max_money_last_time"><th>金錢最大值</th><td>{{player.max_money}}</td><th>持續時間</th><td>{{player.max_money_last_time}}</td></tr>
          <tr v-if="player.now_money_last_time"><th>現在持有金錢</th><td>{{player.now_money}}</td><th>持續時間</th><td>{{player.now_money_last_time}}</td></tr>
          <tr v-if="player.fightExp"><th>戰鬥熟練</th><td>{{player.fightExp}}</td></tr>
          <tr v-if="player.forgeExp"><th>鍛造熟練</th><td>{{player.forgeExp}}</td></tr>
          <tr v-if="player.mineExp"><th>挖礦熟練</th><td>{{player.mineExp}}</td></tr>
          <tr v-if="player.forgeExp"><th>出戰次數</th><td>{{player.times}}</td></tr>
          <tr v-if="player.forgeExp"><th>擊殺數</th><td>{{player.kill}}</td></tr>
          <tr v-if="player.forgeExp"><th>被殺數</th><td>{{player.killed}}</td></tr>
          <tr v-if="player.forgeExp"><th>造成傷害</th><td>{{player.damage}}</td></tr>
          <tr v-if="player.forgeExp"><th>承受傷害</th><td>{{player.damaged}}</td></tr>
          <tr v-if="player.forgeExp"><th>對牆傷害</th><td>{{player.castleDamage}}</td></tr>
          <tr v-if="player.forgeExp"><th>藉由戰鬥獲得的熟練</th><td>{{player.xp}}</td></tr>
        </table>
        <div>
          <h1>參與戰報 {{player.times}}</h1><p>紅色代表有玩家死亡，藍色代表取得樓層獎勵，青色代表摧毀樓層。</p>
          <div class="row-div2">
            <div class="wide-table">
            <table>
              <tr><th>時間</th><th>會戰編號</th><th>進攻方</th><th>防守方</th><th>備註</th><th>id</th></tr>
              <tr v-for="summary in player.report_summary" v-bind:key="summary" :class="summary.spe">
                <td>{{format_time(summary.time)}}</td>
                <td><router-link class="player-link" :to="'/match/'+summary.match_id">{{summary.match_id}}</router-link></td>
                <td>{{summary.atk_f}} 的 <a class="player-link" :href="'/player/'+summary.atk_id"
                >{{summary.atk_name}}</a></td>
                <td>{{summary.def_f}} 的 <a class="player-link" v-if="summary.def_name" :href="'/player/'+summary.def_id">{{summary.def_name}}</a>{{(summary.def_name) ? none : "牆壁"}}</td>
                <td>{{(summary.floor === "衛兵") ? "衛兵": ("在"+summary.def_f)+"第"+summary.floor+"層"}}</td>
                <td><router-link class="player-link" v-bind:to="'/history/'+ this.$store.state.round +'/'+summary.id">{{summary.id}}</router-link></td>
              </tr>
            </table>
          </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import api from "@/api";

export default {
  name: "Player",
  data() {
    return {
      loading: false,
      player: {
        name: "Kulimi",
        role: "鍛造師",
        role2: "時裝設計師",
        id: 1,
        factions: [
          {
            name: "艾基爾",
            time: "40%"
          },
          {
            name: "吳",
            time: "60%"
          }
        ],
        max_money: 666666,
        max_money_last_time: 1234567,
        now_money: 10,
        now_money_last_time: 10,
        fightExp: 0,
        forgeExp: 0,
        mineExp: 0,
        times: 0,
        kill: 0,
        killed: 0,
        damage: 0,
        damaged: 0,
        castleDamage: 0,
        xp: 0,
        loot: [
          2,
          [
            {
              faction: "大麻神教",
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
        ],
        report_summary: [
          {
            atk_f : "艾基爾",
            def_f: "吳",
            atk_name: "Kulimi2",
            atk_id: 20,
            def_name: "Kulimi",
            def_id: 1,
            floor: 0,
            spe: "kill",
            time: 1617653222268.1222,
            id: 2,
            match_id: "asdfsdf"
          }
        ]
      }
    }
  },
  watch: {
    "$store.state.round": async function () {
      this.loading = false
      this.player = await api.getData( "player/" + this.$route.params.id + ".json")
      this.loading = true
    }
  },
  mounted: async function () {
    this.player = await api.getData( "player/" + this.$route.params.id + ".json")
    this.loading = true
  },
  methods:{
    format_time(ori_time){
      return (new Date(ori_time)).toLocaleString()
    }
  }
}
</script>

<style scoped lang="scss">
.kill{
  color: red ;
  .player-link{
    color: red ;

  }
}

.loot{
  color: #3a96ff ;
  .player-link{
    color: #3a96ff ;

  }
}

.floor{
  color: lightseagreen ;
  .player-link{
    color: lightseagreen ;
  }
}

.player-link{
  text-decoration: underline;
}

.player-link:hover{
  text-decoration: none;
}
</style>