<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

const dataURL = 'https://api.myjson.com/bins/10dxnx';

export default {
  name: 'Fetch',
  data() {
    return {
      msg: 'Запрос ещё не прошёл',
    };
  },
  methods: {
    getMessage() {
      axios.get(dataURL)
        .then((response) => {
          // console.log(response);
          this.msg = response.data.message;
        });
    },
  },
  created() {
    // this.getMessage();
    axios.get(dataURL)
      .then((response) => {
        // console.log(response);
        this.msg = response.data.message;
      });
  },
};
</script>
