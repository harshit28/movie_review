<template>
  <div class="moviereview">
<div>
    <!-- <b-button @click="edit = !edit">Open Modal</b-button> -->

    <b-modal  v-model="edit" @ok="update"> 

          <template v-slot:modal-title>
      Update entry for <code> {{form.movie}} </code> 
    </template>
    <div class="col-md-8 order-md-1">
      <form class="needs-validation">
        <div class="row">
          <div class="col-md-6 mb-3">
            <!-- <label for="firstName">Review</label> -->
            <input type="text" class="form-control" v-model="form.review" id="review"  required>
            <div class="invalid-feedback">
              Valid movie name is required.
            </div>
          </div>
          
        </div>
           <div class="mb-3">
          <star-rating v-model="form.rating"></star-rating>
        </div>
      </form>
    </div>
    </b-modal>
  </div>
      <div class="container">


<table class="table">
  <thead>
    <tr>
      <!-- <th scope="col">#</th> -->
      <th data-editable="true" scope="col">Movie</th>
      <th data-editable="true" scope="col">Reviewer</th>
      <th data-editable="true" scope="col">Feedback</th>
      <th data-editable="true" scope="col">Rating</th>
      <th></th>
    </tr>
  </thead>
  <tbody v-for="(movie,index) in movieList">


    <tr>
      <!-- <th scope="row">{{movie.id}}</th> -->
      <td>{{movie.movie}}</td>
      <td>{{movie.name}}</td>
      <td>{{movie.review}}</td>
    <td>{{movie.rating}}</td>
<td><button
                          type="button"
                          class="btn btn-danger btn-sm  mr-1"
                          @click="deleteMovie(movie.id)">
                      Delete
                  </button>
                  <button
                          type="button"
                          class="btn btn-info btn-sm"
                          @click="editMovie(movie)">
                      Edit
                  </button>
                  
                  </td>

    </tr>

  </tbody>
</table>
      </div>

<!-- {{movieList}} -->
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import StarRating from 'vue-star-rating'

export default {
  name: "MovieReview",
  components: {
      axios,
      StarRating
  },

  data() {
    return {
      movieList: [],
      movie:"",
      edit:false,
      form:{},
    };
  },
  mounted() {
       this.getBooks()
  },
  methods: {
    deleteMovie(id) {
        const url = `http://localhost:5000/api/deletereview/${id}`
        axios.delete(url).then(res=>{
            this.getBooks()
            console.log(res.data.message)
        })

    },
    getBooks() {
const url = "http://localhost:5000/api/getreview";
      axios.get(url).then((res) => {
        this.movieList = res.data
      });
    },
    editMovie(movie) {
        this.edit=true
        this.form = movie
      
    },
    update() {
          const url= `http://localhost:5000/api/updatereview/${this.form.id}`
        axios.put(url,this.form).then(res=>{
            console.log(res)
        }).catch(err=>{
            console.error("Error",err)
        })
    }
  },
};
</script>
<style scoped>
.home {
    display: grid;
}
</style>
