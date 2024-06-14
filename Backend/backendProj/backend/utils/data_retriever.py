from requests import Request, Session,get
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import date,timedelta

class Live_Data_Retriver:
    def getExchanges(self):
        url='https://pro-api.coinmarketcap.com/v1/exchange/info'
        parameters={
            'slug': 'binance,coinbase-exchange,okx,bybit,ftx,kucoin,kraken,gate-io,upbit,nicehash'
         }
        headers={
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '23e537a4-3a2c-4ddc-978b-e178bf8f78c2',
        }
        session=Session()
        session.headers.update(headers)
        data=None
        try:
            response=session.get(url,params=parameters)
            data=json.loads(response.text)
        except (ConnectionError,Timeout,TooManyRedirects) as e:
            print(e)
        all=[]
        for exc in data['data']:
            smol={}
            name=data['data'][exc]['name']
            maker_fee=data['data'][exc]['maker_fee']
            taker_fee=data['data'][exc]['taker_fee']
            logo=data['data'][exc]['logo']
            url=data['data'][exc]['urls']['website'][0]
            week=data['data'][exc]['weekly_visits']
            vol=data['data'][exc]['spot_volume_usd']
            smol['name']=name
            smol['url']=url
            smol['logo']=logo
            smol['vol']=vol
            smol['weekly']=week
            smol['maker_fee']=maker_fee
            smol['taker_fee']=taker_fee
            all.append(smol)
        return all


    def getNews(topic):
        today=date.today()
        yesterday=today - timedelta(days=1)
        r=get("https://newsapi.org/v2/everything?q=" + topic + "&from=" + str(
            yesterday) + "&language=en&sortBy=publishedAt&apiKey=0b5b334e628746cd96618fc1522fe321")
        d=json.loads(r.text)
        articles=[]
        n=0
        titles=set()
        for art in d['articles']:
            tmp={}
            if art['title'] in titles or not art['urlToImage']:
                continue
            tmp['title']=art['title']
            tmp['url']=art['url']
            tmp['image']=art['urlToImage']
            tmp['source']=art['source']['name']
            mydateTime=art['publishedAt']
            mydateTimeSplit=mydateTime.split("T")
            tmp['date']=mydateTimeSplit[0]
            tmp['Time']=mydateTimeSplit[1][:-1]
            articles.append(tmp)
            n+=1
            titles.add(art['title'])
            if n == 20:
                break
        return articles
