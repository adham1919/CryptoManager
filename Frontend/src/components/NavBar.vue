<template>
<div id="app">
    
  <nav class="shadow-lg   navbar navbar-expand-lg sticky-top nav-color" >
    
  <router-link  class=" nav-color  navbar-brand text-style ms-3" to="/" >
    <img class='img-fluid img-style rounded' src="../assets/cml3.png"/>
      </router-link>


    <div  v-if="!user" class="container">
  <div class="collapse navbar-collapse" id=" navbarNav">
    <ul class=" navbar-nav ms-auto">
      <li class="nav-item item-style active">
        <router-link  class="nav-link"  to="/login">Login </router-link>
         </li>
      <li class="nav-item item-style">
         <router-link  class="nav-link"  to="/signup">Sign Up </router-link>
      </li>
      
    </ul>
     </div>
  
  </div>
      

    <div nav-color  v-if="user" class="container">
  <div class="collapse navbar-collapse" id=" navbarNav">
        <ul class=" navbar-nav ">
      <li class="nav-item item-style active">
        <router-link  class="nav-link"  to="/market">Live Market </router-link>
         </li>
      <li class="nav-item item-style">
         <router-link  class="nav-link"  to="/exchanges">Exchanges</router-link>
      </li>
            <li class="nav-item item-style">
         <router-link  class="nav-link"  to="/converter">Converter </router-link>
      </li>
            <li class="nav-item item-style">
         <router-link  class="nav-link"  to="/investmentData">Simulation</router-link>
      </li>
      
    </ul>
    <ul class=" navbar-nav  ms-auto me-0">
               
        <input class="form-control me-2" v-model="query" type="search" placeholder="Search Coins" aria-label="Search">
        <button class="btn btn-outline-success" @click="search()">Search</button>



    
         
        <li class="nav-item dropdown">
          <button class="btn btn-default dropdown-toggle" id="navbarScrollingDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img class=' img-fluid prof-style rounded' src="../assets/profile6.png"/>
          </button>
          <ul class="dropdown-menu drop-style " aria-labelledby="navbarScrollingDropdown">
            <li class="drop-style-link"><router-link class="dropdown-item " to="/profile">Profile</router-link></li>
            <li class="drop-style-link"><router-link class="dropdown-item " to="/settings">Settings</router-link></li>
            <li><hr class="dropdown-divider"></li>
           <button  class="nav-link  logout-style" @click="logout"  >Logout </button>
          </ul>
        </li>
      
    </ul>
     </div>
  
  </div>
</nav>
<router-view/>
</div>




</template>

<script>

export default {
  name: 'NavBar',  

   data()
  {
    return {
      user : null,
      query : ''
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

      },

    logout() 
    {
    fetch(
          'http://localhost:5000/logout' , 
          {
          'method' : 'POST',
           headers : { 
            'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
           
           }
             }
     ).then(resp => resp.json())
        . then(() => { window.location.replace("http://localhost:8080/login");})
      .catch(error  =>{ console.log(error);})
  },
      search() 
    {
         const inp ={
          query:this.query,

          }
    fetch(
          'http://localhost:5000/search' , 
          {
          'method' : 'POST',
           headers : { 
            'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token'),
           
           },
          body : JSON.stringify(inp)
           
             }
     ).then(resp => resp.json())
        . then(data => {
            const result=data.result
            console.log(result);
            if (result=='notfound')
            {
                window.location.replace("http://localhost:8080/"+result);
            }
            
            else
           window.location.replace("http://localhost:8080/cointData/"+result);

            })
      .catch(error  =>{ console.log(error);})
  }
    
    
    },created() 
    {
     this.getUserData()
  }
  
}



</script>


<style scoped>



.text-style
{
  font-size : 30px !important;
  font-family : fantasy !important;
  color: rgb(177, 136, 22) !important;
}

.button-color
{
  background-color: rgb(1, 7, 120);
  border : 0px;
}

.logout-style
{
 background-color: white;
  border : 0px;
}



.drop-style
{
 

   min-width: 30px;
   
}


.drop-style a
{
 

   color: black !important;
   
}


.img-style
{
  height: auto;
   width: auto;
   max-width: 250px;
    max-height: 72px;
}

.prof-style
{
  height: auto;
   width: auto;
   max-width: 50px;
    max-height: 50px;
}

.item-style
{
  font-size : 20px !important;
  font-family : Garamond !important;
  color: rgb(252, 250, 250) !important;
}

.nav-color{
  background-color: rgb(0, 42, 92);
  color : black;
}

.nav-color a{

  color : rgb(255, 255, 255);
}

</style>
