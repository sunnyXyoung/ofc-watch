<template>
  <v-container
      fluid
      row
      class="align-center justify-center"
  >
    <v-card class="ma-5"
            :color="m.color"
            width="500"
            v-for="m in messages"
            :key="m"
    >
      <v-card-text>
        <strong>{{ m.content }}</strong>
      </v-card-text>

      <v-card-title class="justify-end" style="display: flex">{{ m.author }}</v-card-title>

    </v-card>



  </v-container>
</template>
<script>
// @ is an alias to /src


export default {
  name: 'Home',
  data() {
    return {
      messages: [
        {
          author: "Kulimi",
          content: "記得尿尿",
          color: "yellow"
        },
        {
          author: "asdfsadf",
          content: "ertyukljhgfdsdfghjklkjhgfdsdertyuioiuytrewqwertghujikuytfrdfghj",
          color: "red"
        },
      ]
    }
  },
  mounted() {


  },
  components: {

  }
}
</script>