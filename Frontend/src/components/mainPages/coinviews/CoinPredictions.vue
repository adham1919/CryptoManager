<template>
<div id="app">

    <h1>Predictions</h1>
    <ul v-if="coinPred">
       <li>{{coinPred.day_1}}</li>
       <li>{{coinPred.day_2}}</li>
       <li>{{coinPred.day_3}}</li>
       <li>{{coinPred.day_4}}</li>
       <li>{{coinPred.day_5}}</li>
       <li>{{coinPred.day_6}}</li>
       <li>{{coinPred.day_7}}</li>

    </ul>
   



</div>



</template>

<script>

export default {
  name: 'CoinPredictions',
    data()
  {
    return {
      coinPred:null
    }

  },
    props:
  {
   symbol : String,
   userData: Object

  },

   methods: {
    getCoinPredictions()
    {
          console.log("mama")
           fetch(`http://localhost:5000/predictions/${this.symbol}` , {
         'method' : 'GET',
         headers : { 
         'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
     }
     }).then(resp => resp.json() )
      .then(data =>  {this.coinPred = data})
      .catch(error  =>{ console.log(error);})

    }
      },
      
    
    created()
  {
     
     this.getCoinPredictions();
  }



}


</script>


<style scoped>



</style>
