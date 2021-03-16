<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/eye-fill.svg" class="eye">
    <h1>Our Floating Castle Watcher</h1>
    <h1>我們的浮游城 觀察者</h1>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  components: {

  }
}
</script>

<style scoped>

@keyframes eye-open {
  0%{
    transform: matrix(1, 0, 0, 0, 0, 0);
  }
  1%{
    transform: matrix(1.01, 0, 0, 0.005, 0, 0);
  }

  100% {
    transform: matrix(1, 0, 0, 1, 0, 0);
  }
}

.eye{
  width: 500px;
  height: 500px;
  animation-name: eye-open;
  animation-duration: 2s;

}

</style>
