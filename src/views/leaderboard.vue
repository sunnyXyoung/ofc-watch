<template>
  <v-container>
    <v-row>
<!--      <v-col-->
<!--          cols="2"-->
<!--      >-->
<!--        <v-card class="ma-5">-->
<!--          <v-card-title>目錄</v-card-title>-->
<!--            <v-list-item-->
<!--                dense-->
<!--                v-for="n in 10"-->
<!--                :key="n"-->
<!--                @click="alert_m(n)"-->
<!--            >-->
<!--              {{ n }}-->
<!--            </v-list-item>-->
<!--        </v-card>-->
<!--      </v-col>-->
      <v-col
          fluid
          row
          style="display: flex; flex-wrap: wrap"
          class="align-center justify-center float-right"
      >
        <v-card
            v-for="c in data_list"
            :key="c"
            width="300"
            height="500"
            style="overflow: scroll"
            class="ma-5"
        >
          <v-card-title>{{ c.json.name }}</v-card-title>
            <v-simple-table>
              <thead>
              <tr>
                <th class="text-left">
                  陣營
                </th>
                <th class="text-left">
                  名稱
                </th>
                <th class="text-left">
                  數量
                </th>
              </tr>
              </thead>
              <tbody>
              <tr
                  v-for="item in c.json.list"
                  :key="item"
              >
                <td>{{ item.faction }}</td>
                <td><router-link :to="generate_link(item.id)">{{ item.name }}</router-link></td>
                <td>{{ item.count }}</td>
              </tr>
              </tbody>
            </v-simple-table>
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>
<script>
// @ is an alias to /src


export default {
  name: 'Home',
  data() {
    return {
      data_list: [
        {
          name: 'kill',
          json: {
            name: "擊殺排行",
            list: [
              {
                faction: "佛跳牆",
                name: "Kulimi",
                id: 1,
                count: 65656
              },
            ]
          }
        },
        {name: 'be_kill', json: {}},
        {name: 'damage', json: {}},
        {name: 'be_damage', json: {}},
        {name: 'wall_damage', json: {}},
        {name: 'all_xp', json: {}},
        {name: 'battle_xp', json: {}},
        {name: 'adventure_xp', json: {}},
        {name: 'hunt_xp', json: {}},
        {name: 'battle_count', json: {}},
        {name: 'hunt_count', json: {}},
      ]
    }
  },
  mounted() {


  },
  methods: {
    alert_m(n){
        alert(n)
    },
    generate_link(id){
      return ("/" + localStorage.round + "/player/" + id.toString())
    }
  },
  components: {

  }
}
</script>