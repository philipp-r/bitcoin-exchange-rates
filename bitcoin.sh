#!/bin/bash

curl https://blockchain.info/de/ticker -o blockchain-data.txt
bitcoinJSON="blockchain-data.txt"

oldValueEur=$(<value.EUR.txt)


cat $bitcoinJSON | while read line
do

	val1=$(echo $line | cut -f3 -d:)
	val2=$(echo $val1 | cut -f1 -d",")
	# value is stored in $val2
	cur1=$(echo $line | cut -f2 -d'"')
	cur2=$(echo $cur1 | cut -f1 -d'"')
	# currency is stored in $cur2


	# Check only EUR
	# write current value in txt files
	if [ $cur2 == "EUR" ]; then
		if (( $(echo $val2'>'$oldValueEur | bc -l) )); then
			pushMessage="↗ $val2 EUR"
		fi
		if (( $(echo $val2'<'$oldValueEur | bc -l) )); then
			pushMessage="↘ $val2 EUR"
		fi
		if [ $val2 == $oldValueEur ]; then
			pushMessage="➡ $val2 EUR"
		fi
	
		echo $pushMessage
		# Pushover user key is passed as argument to this script $1
		# API token $2
		curl --data "token=$2&user=$1&message=$pushMessage&title=Bitcoin%20Kurs&url=https%3A%2F%2Fwww.bitcoin.de%2Fde&sound=cashregister" https://api.pushover.net/1/messages.json
		
		# write new value in txt file
		echo "$val2" > "value.EUR.txt"
	fi

done

