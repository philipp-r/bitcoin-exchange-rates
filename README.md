# Bitcoin Exchange Rates

Uses the blockchain.info API to get the latest bitcoin exchange rates (docs: <https://blockchain.info/de/api/exchange_rates_api>) and send the current value in Euros via Telegram API.

Like this? Donate bitcoins to 13nr9dTqCYdrhifeVaS6AwAUgz2U4EGxXZ 

## Execute the script

Call the script eg with a cronjob with:
```
./bitcoin.sh TELEGRAM_BOT_KEY CHAT_ID
```

Replace `TELEGRAM_BOT_KEY` with API key `CHAT_ID` with Telegram chat id.

## License

Do what you want with the source code but keep a credit to the original author (<https://github.com/philipp-r>).
