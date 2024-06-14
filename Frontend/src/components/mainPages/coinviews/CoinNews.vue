<template>
<div id="app">

    <h1>News</h1>
    <div v-for="(coin,i) in coinNews" :key="i">
    <div class=" form-control div-style container mt-4">
  
  <a :href="coin.url">
  <div class=" mb-3 ">
      <div class="div-section">
      <h5 class="h-style"> {{coin.title}}</h5>
      <label>source : {{coin.source}}</label>
      <br/>
      <label>  published at {{coin.date}} : {{coin.Time}} </label>
      </div>
      <div class="div-section">
      <img class='img-fluid img-style ms-auto rounded' :src="coin.image"/>
      </div>


</div>
   </a>

    </div>
    </div>
   

     


</div>



</template>

<script>

export default {
  name: 'CoinHistorical',
    data()
  {
    return {
      coinNews:[]
    }

  },
    props:
  {
   symbol : String,
   userData: Object

  },

   methods: {
    getCoinNews()
    {
          console.log("mama")
           fetch(`http://localhost:5000/news/${this.symbol}` , {
         'method' : 'GET',
         headers : { 
         'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
     }
     }).then(resp => resp.json() )
      .then(data =>  {this.coinNews = data.articles})
      .catch(error  =>{ console.log(error);})

    }
      },
      
    
    created()
  {
     
     this.getCoinNews();
  }



}


</script>


<style scoped>

.img-style{
     width: 100px;
   height: 100px;
   font: 1em sans-serif;
   float:right;
 
}

.div-style{
     overflow:auto;
}

.h-style{
     width:50%;
}

.div-section {
  display:inline-block;
  width: 50%;
  vertical-align:  top;

}

</style>
