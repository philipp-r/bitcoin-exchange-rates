# Bitcoin Kurs

Uses the blockchain.info API to get the latest bitcoin exchange rates (docs: <https://blockchain.info/de/api/exchange_rates_api>) and send the current value in Euros via Pushover API (docs: <https://pushover.net/api>).

## Execute the script

Call the script eg with a cronjob with:
```
./bitcoin.sh PUSHOVER_USER_KEY PUSHOVER_API_TOKEN
```

Replace `PUSHOVER_USER_KEY` with your user key from Pushover App and `PUSHOVER_API_TOKEN` with your API token

## License

Do what you want with the source code but keep a credit to the original author (<https://github.com/philipp-r>).
