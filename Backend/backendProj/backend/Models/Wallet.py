from backend import db
from backend import ma


class Wallet(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    symbol=db.Column(db.String(20),db.ForeignKey('coin.symbol'))
    quantity=db.Column(db.Numeric)
    buyprice=db.Column(db.Numeric)

class WalletSchema(ma.Schema):
    class Meta:
        fields =('id','uid','symbol','quantity','buyprice')