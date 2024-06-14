<template>
<div id="app">
    <div class="container mt-4">
    <h3>Log In</h3>
  <form class="form-control " @submit.prevent="handleSubmit">
  <div class="mb-3 ">
    <label for="userName" class="form-label">User name</label>
    <input type="text" v-model="user_name" class="form-control" id="userName" aria-describedby="emailHelp">
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" v-model="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">remember me</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</div>
</div>




</template>

<script>

export default {
  name: 'LoginPage',
    data()
  {
    return {
          user : null,
          user_name:'',
          password:''
    }

  },
    methods: {
    handleSubmit()
    {
    if(!this.user_name || !this.password)
      {
          this.error="Please enter the missing fields fields"
      } 
      else if(this.user_name.length<5)
      {
          this.error="Username cant be less than 5 letters"
      } 
      else if(this.password.length<7)
      {
          this.error="Password cant be less than 7 letters"
      } 
      
      else{
        const inp ={
          user_name:this.user_name,
          password:this.password,
          }
          console.log(inp)
          fetch(
          'http://localhost:5000/login' , 
          {
          'method' : 'POST',
           headers : { 'Content-Type' : 'application/json'},
            body : JSON.stringify(inp)
             }
     ).then(resp => resp.json() )
       .then(data  => {
        console.log(data.message);
        localStorage.setItem('token',data.token); 
        console.log(localStorage.getItem('token') );
        }).then(() => { window.location.replace("http://localhost:8080/home");})
        .catch(error  =>{ console.log(error);})

      }
    }
    }


}

</script>


<style scoped>



</style>
