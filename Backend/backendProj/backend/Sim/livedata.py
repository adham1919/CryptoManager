# Import libraries
import json
import requests


# running loop to print all crypto prices
def realTimeData(coinName):
    # Defining Binance API URL
    key = "https://api.binance.com/api/v3/ticker/price?symbol="

    # Making list for multiple crypto's

    coinNameUsd=coinName+"USDT" 
        # completing API for request
    url = key+coinNameUsd
    data = requests.get(url)
    data = data.json()

    str=f"{data['price']}"
    price=float(str)
    return price

    