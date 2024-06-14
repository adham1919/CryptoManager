<template>
<div id="app">

    <h1>Coin chart</h1>
    
    

</div>




</template>

<script>

export default {
  name: 'HomePage',
    data()
  {
    return {
      user : null
    }

  },
   methods: {
    getUserData()
    {
          fetch(
          'http://localhost:5000/user' , 
          {
          'method' : 'GET',
           headers : { 
            'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
           
           }
             }
     ).then(resp => resp.json() )
       .then(data  => {
        console.log(data);
        this.user = data 
        var tmp = data.user_name;
        if(tmp)
        {
        this.user = data 
        }
               else
        {
        
       this.user = null
        }
        
        })

      .catch(error  =>{ console.log(error);})

      }
    
    },created() 
    {
     this.getUserData()
     
  },ready()
  {
     if(this.user==null) {this.$router.push({ name:'login'} );}
  }



}


</script>


<style scoped>



</style>
