from backend import db
from sqlalchemy.orm import backref
from backend.Models.Wallet import Wallet
from backend.Models.Watchlist import Watchlist


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
