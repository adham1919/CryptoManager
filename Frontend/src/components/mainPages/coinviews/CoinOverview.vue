<template>
<div id="app">
  <br/>
     <div class="ms-2">
    <h1>Overview</h1>
    <br/><br/>
    </div>
     
     <ul class="list" v-if="overview">
     <div class="data-row">
     <li >
      <strong> Coin :</strong>  {{overview.name}}
     </li>
      <li>
      <strong>  Price  :</strong> {{overview.price}} $
     </li>
     </div>
     <br/><br/>
      <div class="data-row">
        <li>
     <strong>Highest price reached : </strong> {{overview.high}} $
     </li>
          <li>
    <strong>  Highest price timestamp : </strong>{{ overview.high_timestamp}} 
     </li>
     </div>
     <br/><br/>
     <div class="data-row">
      <li>
      <strong> Max supply  : </strong>  {{ overview.max_supply}}
     </li>

       <li>
      <strong>  Circulating supply : </strong> {{overview.circulating_supply}}
     </li>

     </div>
     <br/><br/>
     <div class="data-row">
          <li>
      <strong> Market cap : </strong>  {{overview.market_cap}}
     </li>
          <li>
   <strong> Market cap dominance : </strong> {{  overview.market_cap_dominance}}
     </li>
     </div>
     <br/><br/>

     <div class="data-row ">
        <li class="listrank " >
      rank : {{overview.rank}}{{pos}}
     </li>
     <li class="ms-auto pl-5 ">
    <pie-chart width="200px" height="200px" :data="[[ overview.name,overview.market_cap_dominance],['rest',1-overview.market_cap_dominance]]"></pie-chart>
</li>
</div>
     </ul>


<br/><br/>
<br/><br/>
   <div v-if="chartData">

   <br/><br/>
   
   <line-chart  :points="false"  :colors="['red']" :data="this.chartData"></line-chart>
   </div>
     


</div>



</template>

<script>

export default {
  name: 'CoinOverview',
    data()
  {
    return {
      chartData:[],
      pos:'',
      overview : null
    }

  },
    props:
  {
   symbol : String,
   userData: Object

  },

   methods: {
    getCoinOverview()
    {
          console.log("mama")
           fetch(`http://localhost:5000/overview/${this.symbol}` , {
         'method' : 'GET',
         headers : { 
         'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
     }
     }).then(resp => resp.json() )
      .then(data =>  {
        this.chartData = data.chartData;
        this.overview= data.overview;
        if(this.overview.rank=='1')
        this.pos="st";
        else  if(this.overview.rank=='2')
        this.pos="nd";
        else  if(this.overview.rank=='3')
        this.pos="rd";
       else 
        this.pos="th";
        
        
        })
      .catch(error  =>{ console.log(error);})

    }
      },
      
    
    created()
  {
     
     this.getCoinOverview();
  }



}


</script>


<style scoped>

.data-row  li{
  display:inline-block;
  width: 50%;
  vertical-align:  top;

}

.list{
  font-size : 20px !important;
  font-family : Arial !important;
  color: black !important;

}


.listrank{
  font-size : 40px !important;
  font-family : fantasy !important;
  color: brown !important;
  width: 50%;


}




</style>
