<template>
  <div class="row-div2">
    <div id="ranks">
      <router-link class="ranks-link" to="kill">擊殺排行</router-link>
      <router-link class="ranks-link" to="killed">被擊殺排行</router-link>
      <router-link class="ranks-link" to="damage">對人傷害排行</router-link>
      <router-link class="ranks-link" to="castleDamage">對牆傷害排行</router-link>
      <router-link class="ranks-link" to="damaged">承受傷害排行</router-link>
      <router-link class="ranks-link" to="xp">戰鬥經驗排行</router-link>
      <router-link class="ranks-link" to="times">出戰次數排行</router-link>
      <router-link class="ranks-link" to="loot">樓層獎勵排行</router-link>
    </div>
    <div class="navbar-toggler" style="border: none">
      <i @click="SideBarOn" class="fa fa-ellipsis-h fa-lg m-dots" style="cursor: pointer"></i>
    </div>
    <div v-if="sidebar" @click="SideBarOn" class="black-layout"></div>
    <transition>
      <div v-if="sidebar" id="sidebar-nav" :class="{'nav-show':sidebar}">
        <router-link class="ranks-link m-ranks-link" to="kill">擊殺排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="killed">被擊殺排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="damage">對人傷害排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="castleDamage">對牆傷害排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="damaged">承受傷害排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="xp">戰鬥經驗排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="times">出戰次數排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="loot">樓層獎勵排行</router-link>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "RanksMenu",
  data() {
    return {
      sidebar: false
    }
  },
  methods: {
    SideBarOn() {
      this.sidebar = (!this.sidebar);
    }
  }
}
</script>

<style scoped lang="scss">

.ranks-link {
  font-weight: bold;
  color: #2c3e50;
  margin-right: 20px;
  margin-left: 20px;
}

.ranks-link:hover {
  text-decoration: underline;
}

#ranks {
  text-align: center;
  width: 100%;
  margin-bottom: 50px;
  display: flex;
  justify-content: center;
  @include phone-width{
    display: none;
  }
  @include small-pad-width{
    display: none;
  }

}

.m-ranks-link{
  margin-bottom: 10%;
}

.navbar-toggler {
  height: 40px;
  width: 40px;
  border-radius: 80px;
  background-color: white;
  box-shadow:3px 3px 5px 6px #cccccc;
  display: none;
  justify-content: center;
  align-content: center;
  position: fixed;
  right: 55px;
  top: 95px;
  @include phone-width{
    display: flex;
  }
  @include small-pad-width{
    display: flex;
  }
}

.m-dots {
  display: flex;
  justify-content: center;
  align-content: center;
  line-height: 40px;

}

</style>