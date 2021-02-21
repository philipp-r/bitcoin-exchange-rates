import requests
import json
import urllib
import sys

# python3 bitcoin.py bot_key chat_id
## sys.argv[1] = bot_key
## sys.argv[2] = chat_id
## can find out chat_id with https://api.telegram.org/bot[bot_key]/getUpdates



# Coins: as in https://api.coingecko.com/api/v3/coins/list
## bitcoin
## ethereum
## bitcoin-cash
## bitcoin-cash-sv
## ripple
## reserve-rights-token
## binancecoin
## dogecoin

# get API data from coingecko
coingeckoUrl = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=EUR&ids=bitcoin,bitcoin-cash,bitcoin-cash-sv,ethereum,ripple,reserve-rights-token,dogecoin,binancecoin&include_24hr_change=true"
coinData = json.loads(requests.get(coingeckoUrl).text)

message = ""
message = message + "BTC: <code>" + str( round(coinData["bitcoin"]["eur"],2) ).replace(".", ",") + "</code> EUR (" + str( round(coinData["bitcoin"]["eur_24h_change"],1) ) + "%) \n"
message = message + "ETH: <code>" + str( round(coinData["ethereum"]["eur"],2) ).replace(".", ",") + "</code> EUR (" + str( round(coinData["ethereum"]["eur_24h_change"],1) ) + "%) \n"
message = message + "BCH: <code>" + str( round(coinData["bitcoin-cash"]["eur"],2) ).replace(".", ",") + "</code> EUR (" + str( round(coinData["bitcoin-cash"]["eur_24h_change"],1) ) + "%) \n"
message = message + "BSV: <code>" + str( round(coinData["bitcoin-cash-sv"]["eur"],2) ).replace(".", ",") + "</code> EUR (" + str( round(coinData["bitcoin-cash-sv"]["eur_24h_change"],1) ) + "%) \n"
message = message + "XRP: <code>" + str( round(coinData["ripple"]["eur"],2) ).replace(".", ",") + "</code> EUR (" + str( round(coinData["ripple"]["eur_24h_change"],1) ) + "%) \n"
message = message + "RSR: <code>" + str( round(coinData["reserve-rights-token"]["eur"],2) ).replace(".", ",") + "</code> EUR (" + str( round(coinData["reserve-rights-token"]["eur_24h_change"],1) ) + "%) \n"
message = message + "BNB: <code>" + str( round(coinData["binancecoin"]["eur"],2) ).replace(".", ",") + "</code> EUR (" + str( round(coinData["binancecoin"]["eur_24h_change"],1) ) + "%) \n"
message = message + "DOGE: <code>" + str( round(coinData["dogecoin"]["eur"],2) ).replace(".", ",") + "</code> EUR (" + str( round(coinData["dogecoin"]["eur_24h_change"],1) ) + "%) \n"
print (message)

# send message to telegram
telegramUrl = "https://api.telegram.org/bot"+sys.argv[1]+"/sendMessage?chat_id="+sys.argv[2]+"&parse_mode=HTML&text="+message
apiResponse = json.loads(requests.get(telegramUrl).text)
