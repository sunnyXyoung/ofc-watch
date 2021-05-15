<template>
  <div id="app">
    <div id="nav">

      <router-link to="/">OFC Watch</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>

</script>

<style>
#app{
  margin: 5% 10% 0;
  border: 10px rgb(23, 23, 23);
  background: rgba(12, 12, 12, 0.8);

  position: relative;
  overflow: hidden;
}

html{
  background-color: #000000;
  background-image: url("./assets/big-eye.png");
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
  height: 100%;
  color: white;
}


#nav{
  height: 10%;
  display: flex;

}

</style>
