import datetime


from backend import db

class Coin_data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    symbol=db.Column(db.String(20),db.ForeignKey('coin.symbol'),nullable=False)
    close=db.Column(db.Numeric,default=0.0)
    open=db.Column(db.Numeric,default=0.0)
    high=db.Column(db.Numeric,default=0.0)
    low=db.Column(db.Numeric,default=0.0)
    volume=db.Column(db.Integer,default=0.0)
    date=db.Column(db.String(50))