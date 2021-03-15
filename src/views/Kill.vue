<template>
  <div>
    <ul>
      <li v-for="(item, index) in killBoardList" :key="item">
        {{ index+1 }}: name: {{ item.name }} Kill: {{ item.Kill }}
      </li>
    </ul>

  </div>
</template>

<script>
export default {
  name: "Kill",
  data() {
    return {
      killBoardList: [
        {name: "Kulimi", Kill: 48763},
        {name: "Kulimi2", Kill: 30678},
      ]
    }
  },
  mounted: function () {
    var jsonify = res => res.json();
    fetch(
        "http://localhost:3000/Kill.json"
    ).then(jsonify).then(data => {
      this.killBoardList = data
    });

  }
}
</script>

<style scoped>

</style>