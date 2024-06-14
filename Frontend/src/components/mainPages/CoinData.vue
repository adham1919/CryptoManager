<template>
<div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark " >
  <div  class="container">
  <div class="collapse navbar-collapse" id=" navbarNav">
           
      
        <ul class=" navbar-nav item-style">
      <li class="nav-item item-style active">
        <button class="nav-link button-style " @click="viewOverview"  >Overview</button>
         </li>
      <li class="nav-item item-style">
         <button  class="nav-link button-style " @click="viewNews" >News</button>
      </li>
            <li class="nav-item item-style">
         <button  class="nav-link button-style " @click="viewPredictions"  >Predictions</button>
      </li>

      <li class="nav-item item-style ">
        <button  class="nav-link button-style " @click="viewHistorical"  >Histotical Data</button>
         </li>      
    </ul>
     </div>
  
  </div>
</nav>



<div v-if="myview==1">
<CoinOverview :userData="user" :symbol="id"/>
  
    </div>

  <div v-if="myview==2">
<CoinNews :userData="user " :symbol="id"/>

    </div>


  <div v-if="myview==3">
<CoinPredictions :userData="user" :symbol="id"/>

    </div>


  <div v-if="myview==4">
<CoinHistorical :userData="user" :symbol="id"/>

    </div>

</div>




</template>

<script>

import CoinHistorical from './coinviews/CoinHistorical.vue'
import CoinOverview from './coinviews/CoinOverview.vue'
import CoinNews from './coinviews/CoinNews.vue'
import CoinPredictions from './coinviews/CoinPredictions.vue'

export default {
  name: 'CoinData',
    components: {
    CoinHistorical,
    CoinOverview,
     CoinNews,
    CoinPredictions
  },
  data()
  {
    return {
      user : null,
      myview : 1,

    }

  },
    props : {
        id: { type:[Number, String],
        required:true

        },
        userData :Object 
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

      },
      viewOverview()
      {
        this.myview=1;
        

      },
      viewHistorical()
      {
        this.myview=4;
        console.log(this.myview)
        
      },      
      viewPredictions()
      {
        this.myview=3
      },
      viewNews()
      {
       this.myview=2
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
.button-style {
  background-color : rgb(33, 37, 41);
  color: red;
  border: 0px;
}


</style>
