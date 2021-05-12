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

  background: hsla(0,0%,100%,.3);

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

#app::before {
  content: '';
  background: hsla(0,0%,100%,.3);
  position: absolute;
  left: 0;top: 0;right: 0;bottom: 0;
  height: 100%;
  width: 100% ;
  filter: blur(20px);
  -webkit-filter: blur(20px);
  z-index: -1;
  margin: -30px ;

}
</style>
