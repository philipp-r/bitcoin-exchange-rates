<?php

/*

$telegram_URL = "https://api.telegram.org/botYOUR_API_KEY_FROM_TELEGRAM/";

$post_data_json = file_get_contents('php://input');
$post_data = json_decode($post_data_json, true);


function telegram_send($message, $keyboard=""){
	global $telegram_URL, $post_data;
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $telegram_URL."sendMessage");
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_POST, 1);
	$telegram_message = urlencode($message);
	curl_setopt($ch, CURLOPT_POSTFIELDS, "chat_id=".$post_data['message']['chat']['id']."&text=".$telegram_message.$keyboard);
	curl_exec($ch);
	curl_close($ch);
}



// Conatains command /get
if (strpos($post_data['message']['text'], '/get') !== false) {

	// get bitcoin exchange rates
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://blockchain.info/ticker");
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$bitcoin_json_data = curl_exec($ch);
	$bitcoin_data = json_decode($bitcoin_json_data, true);
	curl_close($ch);
	// usage: $bitcoin_data['EUR']['15m']

	// EUR
	if( $post_data['message']['text'] == "/get EUR" ){
		// send message with Telegram API
		telegram_send($bitcoin_data['EUR']['15m']." EUR");
		die();
	}
	elseif( $post_data['message']['text'] == "/get USD" ){
		// send message with Telegram API
		telegram_send($bitcoin_data['USD']['15m']." USD");
		die();
	}
	elseif( $post_data['message']['text'] == "/get CHF" ){
		// send message with Telegram API
		telegram_send($bitcoin_data['CHF']['15m']." CHF");
		die();
	}
	elseif( $post_data['message']['text'] == "/get GBP" ){
		// send message with Telegram API
		telegram_send($bitcoin_data['GBP']['15m']." GBP");
		die();
	}
	else{
		// send message with Telegram API
		telegram_send("Please select a currency by entering /get CURRENCY", '&reply_markup={"keyboard":[["/get EUR"],["/get USD"],["/get CHF"],["/get GBP"]],"resize_keyboard":false,"one_time_keyboard":true}');
		die();
	}
}


// /start /end command
if( $post_data['message']['text'] == "/start" ||  $post_data['message']['text'] == "/end" ){
	// send message with Telegram API
	telegram_send("Sorry, this is not working yet. The bot is under construction.");
	die();
}



// ignore all messages that are no commands
telegram_send("I do not understand your message :(");
die();
