from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
import pandas as pd
import os
from main import db

app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:adham12345@localhost/crypto_db2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['CORS_HEADERS']='Content-Type'
db=SQLAlchemy(app)
import datetime


class Coin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    symbol=db.Column(db.String(20),nullable=False)
    name=db.Column(db.String(50))
    data=db.relationship("Coin_data",backref="coin")


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    public_id=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(150))
    user_name=db.Column(db.String(50),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=True)
    budget=db.Column(db.Numeric,default=50000)
    newsletter=db.Column(db.Boolean,default=False)
    active=db.Column(db.Boolean,default=False)
    wallet=db.relationship("Wallet",backref="user")
    watchlist=db.relationship("Watchlist",backref="user")





class Coin_data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    symbol=db.Column(db.String(20),db.ForeignKey('coin.symbol'),nullable=False)
    close=db.Column(db.Numeric,default=0.0)
    open=db.Column(db.Numeric,default=0.0)
    high=db.Column(db.Numeric,default=0.0)
    low=db.Column(db.Numeric,default=0.0)
    volume=db.Column(db.Integer,default=0.0)
    date=db.Column(db.String(50))



class Wallet(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    symbol=db.Column(db.String(20),db.ForeignKey('coin.symbol'))
    quantity=db.Column(db.Numeric)
    buyprice=db.Column(db.Numeric)

class Watchlist(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    symbol=db.Column(db.String(20),db.ForeignKey('coin.symbol'))





