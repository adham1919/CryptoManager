from backend import db
from backend import ma


class Watchlist(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    symbol=db.Column(db.String(20),db.ForeignKey('coin.symbol'))

class WatchlistSchema(ma.Schema):
    class Meta:
        fields =('id','uid','symbol')