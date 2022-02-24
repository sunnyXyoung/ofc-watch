<template>
  <v-container>
    <v-container
        fluid
        row
        class="align-center justify-center"
    >

        <v-card
            style="width: 100%;display: flex"
            class="pa-10 ma-5 justify-center align-center flex-column"
        >

          <img alt="Vue logo" src="../assets/big-eye.png" class="eye">
          <h1>Our Floating Castle Watcher</h1>
          <h1>我們的浮游城 觀察者</h1>
        </v-card>


        <v-card
            class="ma-5"
            width="500"

        >
          <v-card-title>最新事件</v-card-title>
          <v-virtual-scroll
              :bench="5"
              :items="events"
              height="400"
              item-height="32"
          >
            <template v-slot:default="{ item }">
                  <v-list-item
                      :key="item"
                      link
                      dense
                      color="red"
                      :to="item.link"
                  >
                    {{item.text}}
                  </v-list-item>
            </template>
          </v-virtual-scroll>
        </v-card>

      <v-card
          class="ma-5"
      >
        <v-card-title>狩獵</v-card-title>

        <v-container
            v-for="hunt in hunts"
            :key="hunt"
            style="display: flex"
            class="justify-end"
        >
          <v-dialog
              :v-model="hunt.dialog"
              width="500"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                  plain
                  color="black"
                  v-bind="attrs"
                  v-on="on"
              >
                {{hunt.name}}
              </v-btn>
            </template>

            <v-card>
              <v-card-title>
                {{hunt.name}}
              </v-card-title>

              <v-simple-table
                  fixed-header
                  height="300px"
              >
                <template v-slot:default>
                  <thead>
                  <tr>
                    <th class="text-left">
                      層數
                    </th>
                    <th class="text-left">
                      次數
                    </th>
                    <th class="text-left">
                      怪物組成
                    </th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr
                      v-for="item in hunt.dist"
                      :key="item"

                  >
                    <td>{{ item.level }}</td>
                    <td>{{ item.count }}</td>
                    <td>
                      <v-menu

                          close-on-click
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn
                              plain
                              v-bind="attrs"
                              v-on="on"
                          >
                            點擊查看
                          </v-btn>
                        </template>

                        <v-list
                            width="500"
                        >
                          <v-list-item
                              v-for="i in item.monster"
                              :key="i"
                          >
                            <v-list-item-title>{{ i.type }}</v-list-item-title>
                            <v-list-item>{{i.count}}</v-list-item>
                          </v-list-item>
                        </v-list>
                      </v-menu>
                    </td>
                  </tr>
                  </tbody>
                </template>
              </v-simple-table>

            </v-card>
          </v-dialog>
          <v-menu

              close-on-click
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                  plain
                  v-bind="attrs"
                  v-on="on"
              >
                點擊查看
              </v-btn>
            </template>

            <v-list
                width="500"
            >
              <v-list-item
                  v-for="i in hunt.loot"
                  :key="i"
              >
                <v-list-item-title>{{ i.name }}</v-list-item-title>
                <v-list-item>{{i.count}}</v-list-item>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-container>
      </v-card>


      <v-card
          class="ma-5"
          width="500"

      >
        <v-card-title>裝備種類統計</v-card-title>
        <v-simple-table>
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-left">
                種類
              </th>
              <th class="text-left">
                次數
              </th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="item in weapon_type_count"
                :key="item.name"

            >
              <td>{{ item.name }}</td>
              <td>{{ item.count }}</td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card>



    </v-container>
  </v-container>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  data() {
    return {
      benched: 0,
      events: [
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "FF0000",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "black",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "gray",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "fsdf died",
          color: "info",
          link: "/12/54fff5454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },

      ],

      page: 1,
      hunts: [

        {
          name: "vul3蝙蝠動",
          dialog: false,
          loot: [
            {
              name: "依",
              count: 67
            },
            {
              name: "斷入",
              count: 67
            },
          ],
          dist: [
            {
              level: 1,
              count : 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 2,
              count : 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 3,
              count : 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 4,
              count : 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },


          ]
        },
        {
          name: "迷宮區",
          dialog: false,
          dist: [
            {
              level: 1,
              count : 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 2,
              count : 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 3,
              count : 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 4,
              count : 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },


          ]
        }
      ],
      weapon_type_count:[
        {name: "水龍頭", count: 87878787},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
      ]
    }
  },
  mounted() {


  },
  components: {

  }
}
</script>

<style scoped lang="scss">

@keyframes eye-open {
  0%{
    transform: matrix(1, 0, 0, 0, 0, 0);
  }
  50%{
    transform: matrix(1, 0, 0, 0.0001, 0, 0);
  }
  60%{
    transform: matrix(1, 0, 0, 0.3, 0, 0);
  }
  70%{
    transform: matrix(1, 0, 0, 0.3, 0, 0);
  }
  80%{
    transform: matrix(1.01, 0, 0, 0.01, 0, 0);
  }

  100% {
    transform: matrix(1, 0, 0, 1, 0, 0);
  }
}

.eye{
  width: 500px;
  height: 500px;
  animation-name: eye-open;
  animation-duration: 2.5s;

}

.eye2{
  width: 500px;
  height: 500px;
  //animation-name: eye-open;
  //animation-duration: 2.5s;

}

</style>
