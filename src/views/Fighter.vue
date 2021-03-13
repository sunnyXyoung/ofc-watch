<template>
  <div>
    <div class="row-div">
      <div id="ranks">
        <router-link class="ranks-link" to="kill">擊殺排行</router-link>
        <router-link class="ranks-link" to="killed">被擊殺排行</router-link>
        <router-link class="ranks-link" to="damage">輸出排行</router-link>
        <router-link class="ranks-link" to="damaged">被輸出排行</router-link>
        <router-link class="ranks-link" to="xp">戰鬥經驗排行</router-link>
        <router-link class="ranks-link" to="loot">樓層獎勵排行</router-link>
      </div>
    </div>

  </div>

</template>

<script>

export default {
name: "Fighter",
  components: {

  }
}



</script>

<style scoped>

#ranks {
  text-align: center;
  width: 100%;
}

.ranks-link {
  font-weight: bold;
  color: #2c3e50;

  margin-right: 20px;
  margin-left: 20px;
}

.ranks-link:hover {
  text-decoration: underline;
}

</style>