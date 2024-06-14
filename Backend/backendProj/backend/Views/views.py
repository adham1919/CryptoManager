from decimal import Decimal

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from backend.Annots.annotations import token_required
from backend import db
from  backend.utils.data_retriever import Live_Data_Retriver
from requests import get
from backend.Models.Coin import Coin
from backend.Models.Coin_data import Coin_data
from backend.Models.Watchlist import Watchlist
import json
from backend.utils.visualizer import Visulizer
from backend.Sim.sim import buyCoin,sellCoin

views = Blueprint('views', __name__)

res = [0]*12
res2 = [0]*12

@views.route('/market', methods=['GET'])
@token_required
def market(current_user):
    coins=Coin.query.all()
    mycoins=''
    for c in coins:
        print(c.name,c.symbol)
        mycoins+=c.symbol + ','
    mycoins=mycoins[:-1]
    raw = get("https://api.nomics.com/v1/currencies/ticker?key=1fa23732b0289bd71509ac43062dfc2487a6ece6&ids="+mycoins+"&interval=1d,30d&convert=USD&per-page=100&page=1")
    print(raw.status_code)
    coinData = json.loads(raw.text)
    coinNum = len(coins)
    movement = [None]*coinNum
    for i in range(coinNum):
        p = coinData[i]['price']
        res2[i]=res[i]
        res[i]=float(p)
        if float(res[i]) > float(res2[i]):
            movement[i]=2
            print(i)
        elif float(res[i]) < float(res2[i]):
            movement[i] = 0
            print(i)
        elif float(res[i]) == float(res2[i]):
            movement[i] = 1
        output=[]

        for coin in coinData:
            coin_data={}
            coin_data['symbol']=coin['symbol']
            coin_data['price']=coin['price']
            coin_data['name']=coin['name']
            coin_data['logo_url']=coin['logo_url']
      #      coin_data['admin']=coin.admin
            output.append(coin_data)

    return jsonify({'status' : 200,'coinData': output ,'movement': movement})



@views.route('/converter', methods=['GET'])
@token_required
def converter(current_user):
    raw=get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,USDC,USDT,BNB,BUSD,XRP,ADA,SOL,DOGE,USD,EUR,EGP,GBP,CNY&tsyms=BTC,ETH,USDC,USDT,BNB,BUSD,XRP,ADA,SOL,DOGE,USD,EUR,EGP,GBP,CNY&api_key=33f62d682ecbade2a70de0fb93a5f5c4c390c839f07c4debb300cb9b9cbbe768")
    print(raw.status_code)
    result=json.loads(raw.text)
    return jsonify({'status' : 200,'converterData': result})



@views.route('/news/<id>', methods=['GET'])
@token_required
def coinNews(current_user,id):
    ldr = Live_Data_Retriver
    articles= ldr.getNews("bitcoin")
    return jsonify({'status' : 200,'articles': articles})




@views.route('/data/<id>', methods=['GET'])
@token_required
def coinData(current_user,id):
        output=[]
        coins=Coin.query.filter_by(symbol=id).all()
        if coins:
            for coin in reversed(coins):
                coin_data={}
                each=coin.date.split('/')
                date=each[2] + '/' + each[1] + '/' + each[0]
                coin_data['date']=date
                coin_data['close']=coin.close
                coin_data['open']=coin.open
                coin_data['high']=coin.high
                coin_data['low']=coin.low
                coin_data['volume']=coin.volume
                #      coin_data['admin']=coin.admin
                output.append(coin_data)
            return jsonify({'status' : 200,'histData': output})

        print("here")
        return jsonify({'status' : 300 ,'histData': output })


@views.route('/exchanges', methods=['GET'])
@token_required
def getExchanges(current_user):
    ldr =  Live_Data_Retriver()
    excgh =ldr.getExchanges()
    return jsonify({'status' : 200 ,'exchanges': excgh })



@views.route('/newsletter', methods=['GET'])
@token_required
def newsletter(current_user):
    old=current_user.newsletter
    current_user.newsletter= not old
    db.session.commit()
    return jsonify({'status' : 200 ,'subscription ': 'done' })

@views.route('/buy', methods=['POST'])
@token_required
def buy(current_user):
    data=request.get_json()
    coinprice=data['coinprice']
    quantity=data['quantity']
    symb=data['symb']
    coinprice=Decimal(coinprice)
    quantity=Decimal(quantity)
    res = buyCoin(coinName=symb,current_price=coinprice,coinQuantity=quantity,Money=current_user.budget,user_id=current_user.id)
    return jsonify({'status' : 200 ,'subscription ': res})


@views.route('/sell', methods=['POST'])
@token_required
def sell(current_user):
    data=request.get_json()
    coinprice=data['coinprice']
    quantity=data['quantity']
    symb=data['symb']
    print("mamamia")

    coinprice=Decimal(coinprice)

    quantity=Decimal(quantity)

    res = sellCoin(coinName=symb,current_price=coinprice,coinQuantity=quantity,Money=current_user.budget,user_id=current_user.id)
    return jsonify({'status' : 200 ,'subscription ': res })



@views.route('/predictions/<id>', methods=['GET'])
@token_required
def coinPredictions(current_user,id):
    r=get("http://127.0.0.1:5005/ml")
    print(r.status_code)
    d=json.loads(r.text)
    print(r.text)
    out={}
    for i in range(7):
      key='day '+str(i+1)
      key2='day_'+str(i+1)
      out[key2]=  d[key]
    return jsonify(out)

@views.route('/coins', methods=['GET'])
@token_required
def getCoins(current_user):
    coins=Coin.query.all()
    all =[]
    for c in coins:
        tmp = {}
        tmp['name']=c.name
        tmp['symbol']=c.symbol
        all.append(tmp)
    return jsonify(all)



@views.route('/overview/<id>', methods=['GET'])
@token_required
def coinOverview(current_user,id):
        output=[]
        coins=Coin_data.query.filter_by(symbol=id).all()

        if coins:
            for coin in reversed(coins):
                print(coin.date)
                coin_data={}
                each=coin.date.split('/')
                date=each[2] + '/' + each[1] + '/' + each[0]
                coin_data['date']=date
                coin_data['close']=coin.close
                #      coin_data['admin']=coin.admin
                output.append(coin_data)
            output2 =[]
            resChart={}
            for i in range(365):
                 resChart[output[i]['date']]=output[i]['close']
            r=get("https://api.nomics.com/v1/currencies/ticker?key=1fa23732b0289bd71509ac43062dfc2487a6ece6&ids=" + id + "&interval=1d,30d&convert=USD&per-page=100&page=1")
            print(r.status_code)
            d=json.loads(r.text)
            res = {}
            for n in d:
                res['name']=n['name']


                res['market_cap']=n['market_cap']
                res['market_cap_dominance']=n['market_cap_dominance']
                res['high_timestamp']=n['high_timestamp']
                res['rank']=n['rank']
                res['price']=n['price']
            return jsonify({'status' : 200,'overview':res,'chartData': resChart})

        print("here")
        return jsonify({'st AZZZZZZatus' : 300 ,'histData': output })



@views.route('/simulation', methods=['GET'])
@token_required
def simulation(current_user):
    raw = get("https://api.nomics.com/v1/currencies/ticker?key=1fa23732b0289bd71509ac43062dfc2487a6ece6&ids=BTC,ETH,USDT,BNB,USDC,XRP,SOL,LINK,ADA,AAVE,TRX,DOGE&interval=1d,30d&convert=USD&per-page=100&page=1")
    print(raw.status_code)
    coinData = json.loads(raw.text)
    movement = [None]*12
    for i in range(12):
        p = coinData[i]['price']
        res2[i]=res[i]
        res[i]=float(p)
        if float(res[i]) > float(res2[i]):
            movement[i]=2
            print(i)
        elif float(res[i]) < float(res2[i]):
            movement[i] = 0
            print(i)
        elif float(res[i]) == float(res2[i]):
            movement[i] = 1
        output=[]

        for coin in coinData:
            coin_data={}
            coin_data['symbol']=coin['symbol']
            coin_data['price']=coin['price']
            coin_data['name']=coin['name']
            coin_data['logo_url']=coin['logo_url']
      #      coin_data['admin']=coin.admin
            output.append(coin_data)

    return jsonify({'status' : 200,'coinData': output ,'movement': movement})



@views.route('/addToWatchlist/<symbol>', methods=['GET'])
@token_required
def addToWatchlist(current_user,symbol):
    print(symbol)
    watchlist = Watchlist(uid=current_user.id,symbol=symbol)
    db.session.add( watchlist)
    db.session.commit()
    return jsonify({'status': 200,'operation': "done"})




@views.route('/removeFromWatchlist/<symbol>', methods=['GET'])
@token_required
def removeFromWatchList(current_user,symbol):
        watchlistRecord=Watchlist.query.filter((Watchlist.uid==current_user.id) & (Watchlist.symbol==symbol)).first()
        db.session.delete(watchlistRecord)
        db.session.commit()
        return jsonify({'status' : 200 ,'operation': "done" })


@views.route('/search', methods=['POST'])
@token_required
def search(current_user):
    res='notfound'
    data=request.get_json()
    query=data['query']
    symb=query.upper()
    name=query.lower()
    coin = Coin.query.filter((Coin.symbol==symb) | (Coin.name==name)).first()
    if coin:
        res=coin.symbol
        return jsonify({'status': 200,'result': res})
    else :
        return jsonify({'status': 404,'result': res})







@views.route('/profile', methods=['GET'])
def profile():

    return jsonify({'status' : 200 })
