<template>
<div id="app">

    <h1>Converter</h1>


        <div class="shadow-lg form-control  container mt-4">
    <h3>{{fromSymb}}</h3>
 <div class="row">
    <div class="input-group mb-3 div-block">
  <div class="input-group">
  

        <div class="nav-item dropdown">
          <button class="btn btn-outline-secondary dropdown-toggle-split btn-default dropdown-toggle" id="navbarScrollingDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
             
          </button>
          <ul class="dropdown-menu drop-style " aria-labelledby="navbarScrollingDropdown">
            <li> <button  class="nav-link  logout-style" @click="setCurrencyFrom('BTC')"  >BTC </button></li>
             <li><button  class="nav-link  logout-style" @click="setCurrencyFrom('ETH')"  >ETH </button> </li>
             <li> <button  class="nav-link  logout-style" @click="setCurrencyFrom('USDC')"  >USDC </button></li>
             <li><button  class="nav-link  logout-style" @click="setCurrencyFrom('BNB')"  >BNB </button> </li>
          </ul>
        </div>
       <span class="input-group-text" id="basic-addon2">{{fromSymb}}</span>
   
     <input type="text" @change="calCurrencyTo"  v-model="fromVal" class=" input-width form-control" aria-label="Text input with segmented dropdown button">
  </div>
 
</div>
<div class="input-group equal-block">
<span class="ms-4">=</span>
</div>
<div class="input-group div-block">
 
  <div class="input-group">
    <input type="text" @change="calCurrencyFrom" v-model="toVal" class="input-width form-control" aria-label="Text input with segmented dropdown button">
     <span class="input-group-text" >{{toSymb}}</span>
      <div class="nav-item dropdown">
          <button class="btn btn-outline-secondary dropdown-toggle-split btn-default dropdown-toggle" id="navbarScrollingDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
             
          </button>
          <ul class="dropdown-menu drop-style " aria-labelledby="navbarScrollingDropdown">
               <li> <button  class="nav-link  logout-style" @click="setCurrencyTo('USD')"  >USD </button></li>
             <li><button  class="nav-link  logout-style" @click="setCurrencyTo('EUR')"  >EUR </button> </li>
             <li> <button  class="nav-link  logout-style" @click="setCurrencyTo('EGP')"  >EGP </button></li>

          </ul>
        </div>
  </div>
</div>
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
      fromSymb : "BTC",
      toSymb : "USD",
      fromVal : 1,
      toVal: 1,
      user : null,
      converter: null
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
      getConverterData()
    {
          fetch(
          'http://localhost:5000/converter' , 
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
        this.converter = data.converterData
        
        this.toVal=this.converter.BTC.USD} )

      .catch(error  =>{ console.log(error);})

      },

      setCurrencyFrom(curren)
    {
        this.fromSymb=curren
        this.fromVal=this.toVal*this.converter[this.toSymb][this.fromSymb]
        
      },
      setCurrencyTo(curren)
    {
        this.toSymb=curren

         this.toVal=this.fromVal*this.converter[this.fromSymb][this.toSymb]
      },
      calCurrencyFrom()
    {
        this.fromVal=this.toVal*this.converter[this.toSymb][this.fromSymb]
      },
      calCurrencyTo()
    {
        this.toVal=this.fromVal*this.converter[this.fromSymb][this.toSymb]
      }
    
    },created() 
    {
     this.getUserData();
     this.getConverterData();
     
  },ready()
  {
     if(this.user==null) {this.$router.push({ name:'login'} );}
  }



}


</script>


<style scoped>

.input-width {
  max-width : 350px;
}

.div-block
{
    display:inline-block;
  width: 45%;
  vertical-align:  top;
}

.equal-block
{
  display:inline-block;
  width: 10%;
  vertical-align:  top;
}

</style>
