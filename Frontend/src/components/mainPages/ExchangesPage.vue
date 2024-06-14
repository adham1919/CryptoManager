<template>
<div id="app">

    <h1>Exchanges</h1>


  <table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">website</th>
      <th scope="col">Volume</th>
      <th scope="col">Weekly Visitors</th>
      <th scope="col">maker fee</th>
      <th scope="col">taker fee</th>
    </tr>
  </thead>
 
<tbody>


    <tr v-for="(exchange,i) in exchanges" :key="i">
      <th class="website-style">   <a :href="exchange.url">
        <img class='img-fluid img-style ms-auto rounded' :src="exchange.logo"/>  {{exchange.name}}
        </a> 
        </th>
      <td>{{exchange.vol}} $</td> 
      <td>{{exchange.weekly}}</td>
   
      <td>{{exchange.maker_fee}}</td>
      <td>{{exchange.taker_fee}}</td>

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
      exchanges:[]
    }

  },

   methods: {
    getExchanges()
    {
          console.log("mama")
           fetch('http://localhost:5000/exchanges' , {
         'method' : 'GET',
         headers : { 
         'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
     }
     }).then(resp => resp.json() )
      .then(data =>  {this.exchanges = data.exchanges})
      .catch(error  =>{ console.log(error);})

    }
      },
      
    
    created()
  {
     
     this.getExchanges();
  }



}


</script>


<style scoped>

.website-style img 
{
   width: 100;
   height: 100;
   margin-right: 5px;
}

.website-style a
{
   color:black;
   text-decoration: none;
}

</style>
