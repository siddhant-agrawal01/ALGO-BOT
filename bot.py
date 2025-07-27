# bot.py
from binance.client import Client
from binance.enums import *
import logging
import os
import traceback

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info(" Initialized Binance Futures Client (Testnet: %s)", testnet)

    def get_price(self, symbol):
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol)
            return float(ticker['price'])
        except Exception as e:
            logging.error(f" Error fetching price: {e}")
            logging.error(traceback.format_exc())  #
            return None

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logging.info(f" Placing {order_type} order: symbol={symbol}, side={side}, qty={quantity}, price={price}")
            
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                if price is None:
                    raise ValueError(" Price is required for LIMIT orders")
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            logging.info(f" Order response: {order}")
            return order
        except Exception as e:
            logging.error(f" Error placing order: {e}")
            logging.error(traceback.format_exc())  
            print(f" Error placing order: {e}")   
            return None
