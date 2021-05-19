<template>
  <div id="container">
    <input type="text" class="input-bar"
           placeholder="account"
    >
    <input type="text" class="input-bar"
           placeholder="password"
    >
  </div>
</template>

<script>
export default {
  name: "Login.vue"
}
</script>

<style scoped>
#container {
  display: flex;
  justify-content: center;
  align-content: center;
  flex-flow: column;
}

.input-bar{
  width: 10%;
}
</style>