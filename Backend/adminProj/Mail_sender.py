import json

from requests import get

from models import User,db
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
port = 465  # For SSL
smtp_server = "smtp.gmail.com"

class Mail_sender:
    def createMails(self,user):
        watchlist = user.watchlist
        print(user)
        output=[]
        coins=''
        result=''
        if len(watchlist) != 0:
            for w in watchlist:
                coins+=w.symbol+','
            coins = coins[:-1]
            raw=get("https://api.nomics.com/v1/currencies/ticker?key=1fa23732b0289bd71509ac43062dfc2487a6ece6&ids=" + coins + "&interval=1d,30d&convert=USD&per-page=100&page=1")
            print(raw.status_code)
            coinData=json.loads(raw.text)
            for coin in coinData:
                coin_data={}
                coin_data['price']=coin['price']
                coin_data['name']=coin['name']
                #      coin_data['admin']=coin.admin
                output.append(coin_data)
            print(output)
        else :
            raw=get("https://api.nomics.com/v1/currencies/ticker?key=1fa23732b0289bd71509ac43062dfc2487a6ece6&ids=BTC,ETH,LTC&interval=1d,30d&convert=USD&per-page=100&page=1")
            print(raw.status_code)
            coinData=json.loads(raw.text)
            for coin in coinData:
                coin_data={}
                coin_data['price']=coin['price']
                coin_data['name']=coin['name']
                #      coin_data['admin']=coin.admin
                output.append(coin_data)

            for coin in output:
                result+="coin name :"+coin["name"] + "Price:"+coin["price"]  +" $\n"
        print(result)
        return result

    def sendMails(self):
        users = User.query.filter_by(newsletter=True)
        for user in users:
            res = self.createMails(user)
            port=465  # For SSL
            smtp_server="smtp.gmail.com"
            sender_email="cryptomanagernewsletter@gmail.com"  # Enter your address
            receiver_email=user.email  # Enter receiver address
            password="ofrmutgfkbeckakj"

            message2="CryptoNewsletter\n Hello "+user.user_name+"here is the lastest prices for the cryptocurrences\n"+res
            print(message2)
            message=MIMEMultipart()
            message['From']=sender_email
            message['To']=receiver_email
            message['Subject']='A test mail sent by Python. It has an attachment.'  # The subject line
            # The body and the attachments for the mail
            message.attach(MIMEText(message2,'plain'))
            context=ssl.create_default_context()

            text=message.as_string()
            print(text)
            with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
                server.login(sender_email,password)
                server.sendmail(sender_email,receiver_email,text)

        pass