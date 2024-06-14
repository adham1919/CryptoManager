import database
import userBuy
import livedata
import userSell

while True:
    #enter user id
    user_id=int(input("Enter your id "))
    #check if user exsist
    if not database.checkClient(user_id):
        print("no such user")
        continue
    answer=input("what do you wish to do?")
    #buy coin
    if answer == "buy coin":
        #specify coin name
        coinName=input("coin Name ")
        Money=database.get_Client_money(user_id)
        current_price=livedata.realTimeData(coinName)
        #how much does he want to buy
        maximum_quantity=Money/current_price
        print(maximum_quantity)
        coinQuantity=float(input("how much do you want to buy"))
        TransactionFlag=userBuy.buyCoin(user_id,coinName, coinQuantity,maximum_quantity,current_price,Money)
        if TransactionFlag :
            print("Transction done Successfully")
            continue
        else :
            print("Not enough Money , Transaction Failed")
        
        
    #sell coin
    if answer == "sell coin":
        #specify coin name
        coinName=input("coin Name ")
        Money=database.get_Client_money(user_id)
        current_price=livedata.realTimeData(coinName)
        #how much does he want to sell
        coinQuantity=float(input("how much do you want to sell"))
        TransactionFlag=userSell.sellCoin(user_id,coinName, coinQuantity,current_price,Money)
        if TransactionFlag :
            print("Transction done Successfully")
            continue
        else :
            print("Not enough Coin , Transaction Failed")
    

    #check balance
    if answer == "check balance" :
        print(database.get_Client_money(user_id))
    #check coin
    if answer == "check coin" :
        #specify coin name
        coinName=input("coin Name ")
        print(database.get_Wallet_ALL_Quantity(coinName,user_id))
    #stop Loss
    if answer == "stop loss":
         coinName=input("coin Name ")
         StopLossPrice=input("Stop loss price ")
         #checking if i am adding a row or updating a row
         if database.checkAutoStop(user_id,coinName):
             
                database.update_Auto_Stop(user_id,coinName,StopLossPrice)
         else:       
                database.add_auto_stop_Loss(user_id,coinName,StopLossPrice)


    #Exit
    if answer == "exit":
        break