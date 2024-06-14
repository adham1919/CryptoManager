from backend import db
from backend.Models.Watchlist import Watchlist
from backend.Models.Coin_data import Coin_data

class Coin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    symbol=db.Column(db.String(20),nullable=False)
    name=db.Column(db.String(50))
    data=db.relationship("Coin_data",backref="coin")
    watchlist=db.relationship("Watchlist",backref="coin")