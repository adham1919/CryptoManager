<template>
<div id="app">

 
    <!--    <div class="container ml-5">
           <h1>Live Market</h1>
   <p  v-if="user">Hello {{user.user_name}}</p> 
     <p  v-if="user">{{coins[1].symbol}}</p>  
</div>-->
     <div class=" display-inline mt-3">
      <center>
        <h1 >Live Market</h1>
        </center>
        <br/>
  <div v-for="(coin,i) in coins" :key="coin.symbol">
  <h3>
    <router-link  class=" nav-link"  :to="{name:'coinData', params:{id:coin.symbol}}">
    <div >
     <img class='img-fluid img-style ms-5 rounded' :src="getImageUrl(coin)"/>
     <label class="ms-3 mt-2" >{{coin.name}} <label class="label-style" >({{coin.symbol}})</label></label> 
      
      <label style="position: absolute;right: 100px;" class="text-right me-auto close">{{coin.price+' $'}}</label>
       <img v-if="movements[i]==2" style="position: absolute;right: 10px;" class='img-fluid movement-style rounded' src="../../assets/up.png"/> 
       <img v-if="movements[i]==1" style="position: absolute;right: 10px;" class='img-fluid movement-style rounded' src="../../assets/dash.png"/>
        <img v-if="movements[i]==0" style="position: absolute;right: 10px;" class='img-fluid movement-style rounded' src="../../assets/down.png"/>
               </div>
    </router-link>
    </h3> 
 <!--
    <ul class="list-group list-group-flush" id="coines">
  <div v-for="(coin,index) in coins" :key="coin.symbol">
   <router-link  class=" nav-link"  :to="{name:'coinData', params:{id:coin.symbol}}">
  <li class="list-group-item ">
      <div class="row">

        <img class="img-fluid" style="width:50px;height:50px"  :src="getImageUrl(coin)"  >

        <div class="pt-2 pl-2 close">


    {{coin.symbol}}

      </div>
       <div class="ml-auto close">
        {{coin.price+' '+index}}$
            </div>


      

    </div>


  </li>
  </router-link>
  </div>
</ul>
-->

 
  
</div>
</div>
</div>




</template>

<script>

export default {
  name: 'HomePage',
    data()
  {
    return {
      user : null,
      coins : null,
      interval : null,
      movements : null
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

      },


    coinData()
    {
          fetch(
          'http://localhost:5000/market' , 
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
        this.coins = data.coinData;
        this.movements=data.movement;
        console.log(this.coins);
        console.log(this.movements);

        
        })

      .catch(error  =>{ console.log(error);})

      },
      getImageUrl(coin)
      {
        return coin.logo_url;
      }
    
    }
    
    ,created() 
    {
     
     this.getUserData();
     this.coinData();
    
    
     
    
     
     
  }
  ,mounted()
  {

     this.interval = window.setInterval(this.coinData, 25000);
    
  },
  beforeUnmount()
  {
   
     clearInterval(this.interval);
  }



}


</script>


<style scoped>

.img-style
{

   width: 50px;
   height: 50px;
}

.label-style
{

  font-size: small;
  color : rgb(126, 125, 125);
}

.movement-style
{

   width: 30px;
   height: 30px;
}


</style>
