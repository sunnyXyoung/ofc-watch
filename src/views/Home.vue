<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/big-eye.png" class="eye">
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
  @include phone-width{
    width: 60%;
    height: 60%;
  }
  @include pad-width{
    width: 70%;
    height: 70%;
  }
}

</style>
