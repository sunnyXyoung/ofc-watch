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
  </div>
</template>

<script>
export default {
name: "RanksMenu"
}
</script>

<style scoped>

</style>