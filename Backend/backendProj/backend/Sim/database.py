from flask import Flask,jsonify
from backend.Models.User import db
from backend.Models.User import User
from backend.Models.Wallet import Wallet


#############################################################################
# check if user exisit
def checkClient(user_id):
    check=User.query.filter_by(id=user_id)
    if not check:
        return False
    return True


# add wallet
def add_Wallet(buy_price,quantity,uid,coin_name):
    new_todo=Wallet(buyprice=buy_price,quantity=quantity,uid=uid,symbol=coin_name)
    db.session.add(new_todo)
    db.session.commit()


# add_auto Stop time


# get money client data
def get_Client_money(user_id):
    todos=User.query.filter_by(id=user_id).first()
    return todos.budget


# get coin Quantity
def get_Wallet_Quantity(coin_name,userid):
    todos=Wallet.query.filter_by(uid=userid).first()
    print(todos)
    return todos.quantity


# get all Quantity
def get_Wallet_ALL_Quantity(coin_name,userid):

    coinQuantity=Wallet.query.with_entities(Wallet.quantity)
    coinQuantity=coinQuantity.filter_by(symbol=coin_name,uid=userid).all()
    totalQuantity=0.0
    for i in coinQuantity:
        totalQuantity+=i.quantity
    return totalQuantity


# get auto stop coin name
def get_Wallet_buyPrice(coin_name,userid):
    todos=Wallet.query.filter_by(symbol=coin_name,uid=userid).first()
    if todos:
        return todos.buyprice
    return todos


# update Wallet
def update_Wallet_Quantity(coin_name,coinQuantity,user_id):
    while True:
        todos=Wallet.query.filter_by(symbol=coin_name,uid=user_id).first()
        print("Coin",coinQuantity)
        print("user",todos.quantity)
        if todos.quantity < coinQuantity:
            coinQuantity-=todos.quantity
            delete_Wallet(todos)
            continue
        elif todos.quantity == coinQuantity:
            delete_Wallet(todos)
            break
        else:
            todos.quantity-=coinQuantity
            db.session.commit()
            break


def delete_Wallet(WalletID):
    db.session.delete(WalletID)
    db.session.commit()


# update money
def update_Client_money(Money,user_id):
    todos=User.query.filter_by(id=user_id).first()
    todos.budget=Money
    db.session.commit()


# update Stop price


##################################################################
# Terminators
# delete wallet

def Genocide_Wallet(user_id):
    WalletID=Wallet.query.get_or_404(user_id)
    db.session.delete(WalletID)
    db.session.commit()
    return jsonify({'message': 'delete'})


# delete client

def Genocide_Client(user_id):
    ClientID=User.query.get_or_404(user_id)
    db.session.delete(ClientID)
    db.session.commit()
    return jsonify({'message': 'delete'})
