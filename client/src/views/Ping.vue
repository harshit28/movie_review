<template>
  <div class="home">
    <div class="container">
    <button type="button" class="btn btn-primary" @click="ping">
        Ping</button>
        {{ msg }}
  </div>

  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Ping",
  components: {
  },

  data() {
    return {
      msg: "",
    };
  },
  mounted() {},
  methods: {
    ping() {
      const url = "http://127.0.0.1:5000/working";
      axios.get(url).then((res) => {
        this.msg = res.data
        console.log("response", res.data);
      });
    },
  },
};
</script>
<style scoped>
.home {
    display: grid;
}
</style>
