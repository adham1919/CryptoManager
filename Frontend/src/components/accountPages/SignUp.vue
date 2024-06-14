<template>
<div id="app">
    <div v-if="error" class="alert alert-warning alert-dissmisable fade show mt-5" role="alert">

    <strong>
      {{error}}
    </strong>
</div>
  <div class="container mt-4">
    <h3>Join Now</h3>
    <form class="form-control" @submit.prevent="handleSubmit">
  <div class="mb-3 ">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input v-model="email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="userName" class="form-label">User name</label>
    <input v-model="user_name" type="text" class="form-control" id="userName">
  </div>
    <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input  v-model="password1" type="password" class="form-control" id="exampleInputPassword1">
  </div>
      <div class="mb-3">
    <label for="exampleInputPassword2" class="form-label">Repeat Password</label>
    <input v-model="password2" type="password" class="form-control" id="exampleInputPassword2">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</div>

</div>



</template>

<script>
export default {
  name: 'SignUp',

  data()
  {
    return {
      user : null,
      email : '',
      user_name : '',
      password1 : '',
      password2 : '',
      interval : null,
      error : null
    }

  },
  methods: {
    removeError()
    {
      this.error=null
    },
    handleSubmit()
    {
    if(!this.email || !this.user_name || !this.password1 || !this.password2)
      {
          this.error="Please enter the missing fields fields"
      } 
        else if(this.email.length<12)
      {
          this.error="email is invalid"
      }
      else if(this.user_name.length<5)
      {
          this.error="Username cant be less than 6 letters"
                this.interval = window.setTimeout(this.removeError, 15000);
      } 
      else if(this.password1.length<7)
      {
          this.error="Password cant be less than 7 letters"
      } 

      else if(this.password1!=this.password2)
      {
          this.error="Passwords don't match"
      } 
      
      else{
        const data ={
          email:this.email,
          user_name:this.user_name,
          password1:this.password1,
          password2:this.password2,
          }

          fetch(
          'http://localhost:5000/signup' , 
          {
          'method' : 'POST',
           headers : { 'Content-Type' : 'application/json'},
            body : JSON.stringify(data)
             }
     ).then(resp => resp.json() )
      .then(() => {
        this.$router.push({
        name:'login'}
        );})
      .catch(error  =>{ 
   
        console.log(error);})

      }
    }
    },
  beforeUnmount()
  {
   
     clearInterval(this.interval);
  }

  }




</script>


<style scoped>



</style>
