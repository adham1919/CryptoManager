<template>
<div id="app">

  <div class="container mb-5">
    <div class="d-flex justify-content-center">
  
    <table>
       <tr >
           <th class="col">Coin Name</th>
           <th class="col">Current price</th>
           <th class="col">Action</th>
       </tr>
       <tr v-for="(coin,i) in coins" :key="i">
           <td><strong>{{coin.symbol}}</strong> </td>
           <td >{{coin.price+' $'}}</td>
           <td ><button class="buy_sell_button" @click="buy(coin.symbol,coin.price)" >BUY</button><button class="buy_sell_button" @click="sell(coin.symbol,coin.price)">SELL</button></td>
         </tr>
         
                 <tr ><td colspan="3">

           <input type="number" v-model="quantity" min="0" class=" form-control" id="userName" ></td>
       </tr> 
  

    </table>
    
    
</div>
</div>

</div >



</template>


<script>

export default {
  name: 'HomePage',
    data()
  {
    return {
      user : null,
      quantity : 1,
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
      },
      buy(coinSymb,price)
      {
        console.log(coinSymb)
        console.log(price)
        console.log(this.quantity)
                const inp ={
          coinprice:price,
          quantity:this.quantity,
          symb:coinSymb
          }
           fetch(
          'http://localhost:5000/buy' , 
          {
          'method' : 'POST',
           headers : { 'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')},
            body : JSON.stringify(inp)
             }
     ).then(resp => resp.json() )
      .catch(error  =>{ console.log(error);})
      },
 
      sell(coinSymb,price)
      {
        console.log(coinSymb)
        console.log(price)
        console.log(this.quantity)
                const inp ={
          coinprice:price,
          quantity:this.quantity,
          symb:coinSymb
          }
           fetch(
          'http://localhost:5000/sell' , 
          {
          'method' : 'POST',
           headers : { 'Content-Type' : 'application/json'
           ,'x-access-token' : localStorage.getItem('token')},
            body : JSON.stringify(inp)
             }
     ).then(resp => resp.json() )
      .catch(error  =>{ console.log(error);})
      }

    
    
    }
    
    ,created() 
    {
     
     this.getUserData();
     this.coinData();
    
    
     
    
     
     
  }
  ,mounted()
  {

     //this.interval = window.setInterval(this.coinData, 25000);
    
  },
  beforeUnmount()
  {
   
     clearInterval(this.interval);
  }



}


</script>



<style scoped>

.col{
            padding: 1rem;
            background-color: #293462;
            border: 2px solid white;
            color: white;
            text-align: left;
            
        }
        .buy_sell_button{
            padding: 1rem;
            background-color: #000000e0;
            border: 2px solid white;
            color: white;
        }
        .stop_loss_button{
            padding: 1rem;
            background-color: red;
            border: 2px solid white;
            color: white;
        }
        .buy_sell_button:hover{
            padding: 1rem;
            background-color: white;
            border: 2px solid white;
            color: #000000e0;
        }
        .stop_loss_button:hover{
            padding: 1rem;
            background-color: white;
            border: 2px solid white;
            color: red;
        }

        
        .number-box{
             width: 50%;
        }

</style>
