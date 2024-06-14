<template>
<div id="app">
<div class=" mb-5 container">
    <center><h1 class="mt-2">Profile</h1></center>
    <div class="list-profile">
     <div>
    <strong> UserName :</strong> {{user.user_name}}
    </div>
         <div>
    <strong> Email :</strong> {{user.email}}
      <input v-if="user.newsletter==false"  class=" ms-4 form-check-input" @change="newsletter()"   type="checkbox" >

    <input v-if="user.newsletter==true" class=" ms-4 form-check-input"  checked @change="newsletter()"    type="checkbox" >
 <label class=" ms-2 label-checkbox" >Subscribe to Newsletter</label>
    </div>
   
</div>
<br/>
 <div class="ms-3">
<h3>Watchlist</h3>
<br/>

<button class="btn-primary" data-bs-target="#myModal" data-bs-toggle="modal"> edit </button>
  <table class="table-sm table-hover">
  <thead>
    <tr>
      <th scope="col">no.</th>
      <th scope="col">Coin Name</th>
      <th scope="col">Coin Symbol</th>
    </tr>
  </thead>
 <tbody>


    <tr v-for="(coin,i) in user.watchlist" :key="i">
       <th scope="row">{{i+1}}</th>
      <th> {{coin.name}}</th>
      <td>{{coin.symbol}}</td>
    </tr>
   

  </tbody>
</table>
</div>


 <!-- Start of Modal 1 -->
   <div class="py-2">

        <div class="modal" id="myModal">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Edit Watchlist</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                      <div class="modal-body">
                       <select class="form-select" size="3" v-model="selectVal" aria-label="size 3 select example">
                                 <option v-for="(coin,i) in allCoins" :key="i" >
                                  {{coin.symbol}}
                                  </option></select>     

>
           
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button"  @click="removeFromWatchlist(selectVal)" class="btn btn-danger">
                        remove
                        </button>
                        <button type="button" @click="addToWatchlist(selectVal)" class="btn btn-success">
                        Add
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
  <!-- End of modal 1 -->





<div class="mt-5" > <h2> Simulation Data  </h2>
 <div class="form-control" >
  <div class="mb-3 ">

         <div class="list-profile">
    <strong> Money :</strong> {{user.budget}} $
    </div>

             <div class="mt-3 list-profile">
    <strong> Coins owned</strong> 
    </div>
  
      <table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">no.</th>
      <th scope="col">Coin Name</th>
      <th scope="col">Quantity</th>
    </tr>
  </thead>
 <tbody>


    <tr v-for="(coin,i) in user.wallet" :key="i">
       <th scope="row">{{i+1}}</th>
      <th> {{coin.symbol}}</th>
      <td>{{coin.quantity}}</td>
    </tr>
   

  </tbody>
</table>
    

</div>
</div>
</div>
  





</div>




</div>

</template>

<script>

export default {
  name: 'MyProfile',
    data()
  {
    return {
      user : null,
      selectVal : null,
      checked : true,
      allCoins : null
    }

  },
   methods: {

    addToWatchlist(symbol)
    {
      console.log(symbol)
          fetch(
          `http://localhost:5000/addToWatchlist/${symbol}`, 
          {
          'method' : 'GET',
           headers : { 
            'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')

           
           }
             }
     ).then(resp => resp.json())
     .then(() => 
     {
 this.getUserData() ;
     })
    
  
     },
     
    removeFromWatchlist(symbol)
    {
          fetch(
          `http://localhost:5000/removeFromWatchlist/${symbol}` , 
          {
          'method' : 'GET',
           headers : { 
            'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
           
           }
             }
     ).then(resp => resp.json() )
          .then(() => 
     {
 this.getUserData() ;
     })
     
     },

    newsletter()
    {
          fetch(
          'http://localhost:5000/newsletter' , 
          {
          'method' : 'GET',
           headers : { 
            'Content-Type' : 'application/json',
           'x-access-token' : localStorage.getItem('token')
           
           }
             }
     ).then(resp => resp.json() )},

    getAllCoins()
    {
          fetch(
          'http://localhost:5000/coins' , 
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
        this.allCoins = data  })
     
     
     },
    
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
        this.user = data ;
        this.checked = this.user.newsletter;
        }
               else
        {
        
       this.user = null
        }
        
        })

      .catch(error  =>{ console.log(error);})

      }
    
    },created() 
    {
     this.getUserData();
     this.getAllCoins();
  },ready()
  {
     if(this.user==null) {this.$router.push({ name:'login'} );}
  }



}



</script>


<style >


.list-profile{
  font-size : 25px !important;
  font-family : Arial !important;
  color: black !important;
  
}

.label-checkbox{
  font-size : 15px !important;
  font-family : Arial !important;
  color: rgb(66, 65, 65) !important;
  
}


</style>
