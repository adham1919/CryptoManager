import joblib as joblib
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sklearn
from flask_marshmallow import Marshmallow
from flask_cors import CORS,cross_origin
import os


app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:adham12345@localhost/crypto_db2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False




app.config['CORS_HEADERS']='Content-Type'
CORS(app , resources={'/*': {"origins" : "*"}})
db=SQLAlchemy(app)





class Coin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    symbol=db.Column(db.String(20),nullable=False)
    volume=db.Column(db.Numeric,default=0.0)
    close=db.Column(db.Numeric,default=0.0)
    open=db.Column(db.Numeric,default=0.0)
    high=db.Column(db.Numeric,default=0.0)
    low=db.Column(db.Numeric,default=0.0)
    date=db.Column(db.String(50))


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    public_id=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(150))
    user_name=db.Column(db.String(50),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=True)
    budget=db.Column(db.Numeric)
    Ownerships=db.relationship("Ownership",backref="user")


class Ownership(db.Model):
    oid=db.Column(db.Integer,primary_key=True)
    owner_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    symbol=db.Column(db.String(20))
    quantity=db.Column(db.Integer)






@app.route('/ml',methods=['GET'])
def get_Ml():
    x=joblib.load('linreg2.pkl',"r")
    coins=Coin.query.filter_by(symbol='BTC').all()
    if coins:
      coins = list(reversed(coins))
      arr =[]
      for i in range(7):
        day=[coins[i].close]
        arr.append(day)
    y=x.predict(arr)
    out={}
    for i in range(7):
      key='day '+str(i+1)
      out[key]= y[i]



    return jsonify(out)

if __name__ == '__main__':
    app.run(debug=True,port=5005)
