# Save these values right now. They won't be shown ever again!

# API Key: 4r7dyUKMVhY9e67fEs6eviEnzC8mBWidxj0mM93XPmhViBRyCuN2fKiO6OuVMxcL

# Secret Key: Id3O0zl8iaPlezo1R2T3i0bcYOfx4MzxV0EZPODcyCwqJ8DL6wybJb8lRCjtB7Rc 

from binance.client import Client
import time


API_KEY='4r7dyUKMVhY9e67fEs6eviEnzC8mBWidxj0mM93XPmhViBRyCuN2fKiO6OuVMxcL'

SECRET_KEY= 'Id3O0zl8iaPlezo1R2T3i0bcYOfx4MzxV0EZPODcyCwqJ8DL6wybJb8lRCjtB7Rc'

client = Client(API_KEY, SECRET_KEY,testnet='true')

account_status=client.get_account()
print(account_status)

symbol = 'BTCUSDT'
buy_price_threshold = 100000
sell_price_threshold = 120000
trade_quantity = 0.001 

def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

get_current_price(symbol)

def place_buy_order(symbol, quantity):
    try:
        order = client.order_market_buy(
            symbol=symbol,
            quantity=quantity
        )
        print(f"Buy order placed: {order}")
    except Exception as e:
        print(f"Error placing buy order: {e}")

place_buy_order(symbol, trade_quantity)


