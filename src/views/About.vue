<template>
  <div style="line-height: 24px">
    {{aboutList[0]}}
    <hr align="center" width="20%" style="margin-bottom: 25px;margin-top: 25px;border-color: rgba(12, 34, 56, 0.5)">
    {{aboutList[1]}}
    <hr align="center" width="20%" style="margin-bottom: 25px;margin-top: 25px;border-color: rgba(12, 34, 56, 0.5)">
    資料每小時更新一次，所以不用猛按重新整理。<br>
    上次更新時間： {{aboutList[2]}}
  </div>

</template>

<script>


export default {
  name: "About",
  components: {},
  data (){
    return {
      aboutList: ['<h1>關於</h1>\n' +
      '    這是我無聊很閒做的網站，所以大概看起來很簡陋吧？<br>我從第四輪結束前就開始製作了，一直拖到第六輪都開始了還沒弄好，<br>\n' +
      '      過程中遭遇了非常多的技術障礙，感謝\n' +
      '    <a href="https://github.com/ItisCaleb" style="size: A4;text-decoration: #2c3e50">@ItisCaleb</a>\n' +
      '    的鼎力相助。<br>\n' +
      '    GitHub: <a href="https://github.com/Xialai-Kulimi/ofc-watch">https://github.com/Xialai-Kulimi/ofc-watch</a><br>', '    這個網站所有的資訊都是從戰報抓的，所以大概算是公開的資訊。<br>\n' +
      '    而且對茅場的伺服器造成的負擔應該很小（吧? <br>\n' +
      '    不用擔心影響效能的問題。<br>', '11/23 48:76:03']
    }
  },
  mounted: function () {
    var jsonify = res => res.json();
    fetch(
        "./About.json"
    ).then(jsonify).then(data => {
      this.aboutList = data
    });

  }
}
</script>

<style scoped>
p {
  size: A3;
}

</style>