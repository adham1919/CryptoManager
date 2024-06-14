import database



def DataBaseUpdate(user_id,Money ):
        #update money
        database.update_Client_money(Money,user_id)
      
 
    




def sellCoin(user_id,coinName,coinQuantity,current_price,Money):
    #check the coin quantity
    Wallet_quantity=database.get_Wallet_ALL_Quantity(coinName,user_id)

    Wallet_buyPrice=database.get_Wallet_buyPrice(coinName,user_id)
   
    if coinQuantity<=Wallet_quantity:
        database.update_Wallet_Quantity(coinName,coinQuantity,user_id)
    else:
        return False
    #update data base
    Client_Money=database.get_Client_money(user_id)
    Money=Client_Money+(current_price/Wallet_buyPrice)*coinQuantity*current_price
    DataBaseUpdate(user_id,Money)
    return True









