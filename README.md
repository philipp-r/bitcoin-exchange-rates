# Bitcoin Exchange Rates

Uses the coingecko.com API to get the latest crypto exchange rates (docs: <https://www.coingecko.com/de/api>) and send the current value via Telegram bot API.

Like this? Donate bitcoins to _bc1q6ukhnrvkmp3zsy463sxh4g00f02vpxmc20kl0u_

## Execute the script

Call the script eg with a cronjob with:
```
python3 bitcoin.py bot_key chat_id
```

Replace `bot_key` with API key `chat_id` with Telegram chat id.

## License

Do what you want with the source code but keep a credit to the original author <https://github.com/philipp-r>.
