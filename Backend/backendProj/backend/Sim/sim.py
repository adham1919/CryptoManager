from decimal import Decimal

from . import database

def buyCoin(coinName,current_price,coinQuantity,Money,user_id):
    maximum_quantity=Money/current_price
    if coinQuantity<=maximum_quantity:
            Money-=(current_price*coinQuantity)
    else :
            return False
    #update money
    database.update_Client_money(Money,user_id)
    #insert to wallet
    database.add_Wallet(current_price,coinQuantity,user_id,coinName)
    return True




def sellCoin(user_id,coinName,coinQuantity,current_price,Money):
     #check the coin quantity
    print("COIN NAME",coinName)
    print("ID",user_id)
    print("money",Money)
    Wallet_quantity=database.get_Wallet_Quantity(coinName,user_id)
    Wallet_buyPrice=database.get_Wallet_buyPrice(coinName,user_id)
    print("coin",coinQuantity)
    print("wallet",Wallet_quantity)

    if coinQuantity<=Wallet_quantity:

        database.update_Wallet_Quantity(coinName,coinQuantity,user_id)
    else:
        return False
    #update data base
    Client_Money=database.get_Client_money(user_id)
    current_price=Decimal(current_price)
    Wallet_buyPrice=Decimal(Wallet_buyPrice)
    Money=Client_Money+(current_price/Wallet_buyPrice)*coinQuantity*current_price
    database.update_Client_money(Money,user_id)
    return True





