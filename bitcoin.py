import requests
import json
import urllib
import sys

# python3 bitcoin.py bot_key chat_id
## sys.argv[1] = bot_key
## sys.argv[2] = chat_id
## can find out chat_id with https://api.telegram.org/bot[bot_key]/getUpdates


# Coins: as in https://api.coingecko.com/api/v3/coins/list
coinsWatch = {
  "bitcoin": "BTC",
  "ethereum": "ETH",
  "bitcoin-cash": "BCH",
  "bitcoin-cash-sv": "BSV",
  "ripple": "XRP",
  "reserve-rights-token": "RSR",
  "binancecoin": "BNB",
  "dogecoin": "DOGE"
}


# get API data from coingecko
coinList = ""
for coin in coinsWatch:
    coinList = coinList+coin+","
print (coinList)
coingeckoUrl = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=EUR&ids="+coinList+"&include_24hr_change=true"
coinData = json.loads(requests.get(coingeckoUrl).text)


# build message
message = ""
for coin in coinsWatch:
    message = message + coinsWatch[coin] + ": <code>" + str( round(coinData[coin]["eur"],2) ).replace(".", ",") + " EUR (" + str( round(coinData[coin]["eur_24h_change"],1) ) + "%) </code>\n"
print (message)


# send message to telegram
telegramUrl = "https://api.telegram.org/bot"+sys.argv[1]+"/sendMessage?chat_id="+sys.argv[2]+"&parse_mode=HTML&text="+message
apiResponse = json.loads(requests.get(telegramUrl).text)
