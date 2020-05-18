<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

const dataURL = 'https://api.jsonbin.io/b/5e90e8278e85c84370140777';

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
