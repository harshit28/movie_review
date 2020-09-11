<template>
  <div class="home">
     <div class="container">
  <div class="py-5 text-center">
    <h2>Movie Review form</h2>
    <p class="lead">Please Enter your movie review's</p>
  </div>

 
    <div class="col-md-8 order-md-1">
      <form class="needs-validation" novalidate>
        <div class="row">
          <div class="col-md-12 mb-3">
            <label for="firstName">Movie name</label>
            <input type="text" class="form-control" v-model="form.movie" id="firstName" placeholder="" value="" required>
            <div class="invalid-feedback">
              Valid movie name is required.
            </div>
          </div>
         
        </div>

        <div class="mb-3">
          <label for="name">Reviewer</label>
          <div class="input-group">
           
            <input type="text" class="form-control" v-model="form.name" id="name" placeholder="name" required>
            <div class="invalid-feedback" style="width: 100%;">
              Your name is required.
            </div>
          </div>
        </div>

        <div class="mb-3">
          <label for="email">Email <span class="text-muted">(Optional)</span></label>
          <input type="email" v-model="form.email" class="form-control" id="email" placeholder="you@example.com">
          <div class="invalid-feedback">
            Please enter a valid email address for shipping updates.
          </div>
        </div>

        <div class="mb-3">
           <div class="form-group">
    <label for="exampleFormControlTextarea1">Example textarea</label>
    <textarea class="form-control" v-model="form.review" id="exampleFormControlTextarea1" rows="3"></textarea>
  </div>
        </div>

        <div class="mb-3">
          <star-rating v-model="form.rating"></star-rating>
        </div>

        


   

      </form>
                <button type="submit" class="btn btn-primary mb-2" @click="postreview">Submit Review</button>

    </div>
  </div>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";

import StarRating from 'vue-star-rating'


export default {
  name: "Home",
  components: {
    axios,
  StarRating
  },

  data() {
    return {
      msg: "",
      form: {},
    };
  },
  mounted() {},
  methods: {
    ping() {
      const url = "http://addyourreview.herokuapp.com/working";
      axios.get(url).then((res) => {
        this.msg = res.data
        console.log("response", res.data);
      });
    },
    postreview() {
      const url = "http://addyourreview.herokuapp.com/addreview";
      axios.post(url,this.form).then((res) => {
        this.msg = res.data
        this.$router.push('/getReview')
        console.log("response", res.data);
      });
    }
  },
};
</script>
