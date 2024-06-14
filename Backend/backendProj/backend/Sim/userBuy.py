import database



def DataBaseUpdate(coinName,current_price,coinQuantity,Money,user_id):
        #update money
        database.update_Client_money(Money,user_id)
        #insert to wallet
        database.add_Wallet(current_price,coinQuantity,user_id,coinName)
 
        return




def buyCoin(user_id,coinName,coinQuantity,maximum_quantity,current_price,Money) :
    while True :  
        if coinQuantity<=maximum_quantity:
            Money-=(current_price*coinQuantity)
        else :
            return False
        #update data base
        DataBaseUpdate(coinName,current_price,coinQuantity,Money,user_id)
        return True









