<template>
  <div style="line-height: 24px ; display: flex; flex-flow: column ; justify-content: center" v-if="loading">
    <h1>關於網站</h1>
    <div >
        這是一個基於戰報分析做出來的遊戲攻略網站(如果這算攻略的話) <br>
        因為我無聊很閒做的網站，所以大概看起來很簡陋吧？<br>
        我從第四輪結束前就開始製作了，一直拖到第七輪都開始了還沒弄好，<br>
        過程中遭遇了非常多的技術障礙，感謝

        <a href="https://github.com/ItisCaleb" style="size: A4;text-decoration: #2c3e50">@ItisCaleb</a>
        的鼎力相助。<br>
      </div>
      <hr align="center" width="20%" style="margin-bottom: 25px;margin-top: 25px;border-color: rgba(12, 34, 56, 0.5)">
      <div>
          戰報分析後呈現的資料大致分為四種，分別是 <br>
          <router-link to="/report">戰報的時間</router-link>
          、
          <router-link to="/fighter">戰鬥員</router-link>
          、
          <router-link to="/faction">陣營</router-link>
          、
          <router-link to="/weapon">裝備</router-link>
          等等統計資料的呈現。
      </div>

      <div class="row-div2">
        <h1>關於作者</h1>
        <div class="row-div2">
          <div>
            暱稱為Kulimi，
            自詡賺錢大師，興趣為提醒大家尿尿， <br>
            實為所屬陣營從來沒有贏過的菜雞。 <br>
            因為實在是太閒了，所以做了這個網站。
          </div>
        </div>
      </div>


      <hr align="center" width="20%" style="margin-bottom: 25px;margin-top: 25px;border-color: rgba(12, 34, 56, 0.5)">
      <div class="row-div2">
        <div>
          這個網站所有的資訊都是從戰報抓的，所以大概算是公開的資訊。<br>
          而且對茅場的伺服器造成的負擔應該很小（吧? <br>
          所以不用擔心影響效能的問題。<br>
        </div>
      </div>

      <hr align="center" width="20%" style="margin-bottom: 25px;margin-top: 25px;border-color: rgba(12, 34, 56, 0.5)">
      資料每小時更新一次，所以不用猛按重新整理。<br>
      上次更新時間： {{ aboutList[0] }}
    </div>

</template>

<script>


export default {
  name: "About",
  components: {},
  data() {
    return {
      loading: false,
      aboutList: ['11/23 48:76:03']
    }
  },
  mounted: function () {
    var jsonify = res => res.json();
    fetch(
        "./About.json"
    ).then(jsonify).then(data => {
      this.aboutList = data
    });
    this.loading = true
  }
}
</script>

<style scoped>
p {
  size: A3;
}

div {

}


</style>