<template>
<div id="app">

    <h1>Historical data</h1>


  <table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">no.</th>
      <th scope="col">Date</th>
      <th scope="col">Close</th>
      <th scope="col">Open</th>
      <th scope="col">High</th>
       <th scope="col">Low</th>
         <th scope="col">Volume</th>
    </tr>
  </thead>
 
<tbody>


    <tr v-for="(coin,i) in coinData" :key="i">
       <th scope="row">{{i+1}}</th>
      <th> {{coin.date}}</th>
      <td>{{coin.close}}</td>
      <td>{{coin.open}}</td>
      <td>{{coin.high}}</td>
      <td>{{coin.low}}</td>
       <td>{{coin.volume}}</td> 
    </tr>
   

  </tbody>
</table>
     


</div>



</template>

<script>

export default {
  name: 'CoinHistorical',
    data()
  {
    return {
      coinData:[]
    }

  },
    props:
  {
   symbol : String,
   userData: Object

  },

   methods: {
    getCoinData()
    {
          console.log("mama")
           fetch(`http://localhost:5000/data/${this.symbol}` , {
         'method' : 'GET',
         headers : { 
         'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
     }
     }).then(resp => resp.json() )
      .then(data =>  {this.coinData = data.histData})
      .catch(error  =>{ console.log(error);})

    }
      },
      
    
    created()
  {
     
     this.getCoinData();
  }



}


</script>


<style scoped>



</style>
