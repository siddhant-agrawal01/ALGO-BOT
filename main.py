
import os
from dotenv import load_dotenv
from bot import BasicBot
from binance.enums import *

load_dotenv()

api_key = 'd5b5b1cd35ed73bf52c930ebcc69c807c5ad5abef192a37dc97c4e96ccf9ca52'
api_secret = '70f19d43bd8149c08c6bb3e690067292c0251ef40441be2c21efdd4c311766b2'

bot = BasicBot(api_key, api_secret, testnet=True)

def ask_order_details():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY/SELL): ").strip().upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").strip().upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter limit price: "))

    return symbol, side, order_type, quantity, price

if __name__ == "__main__":
    symbol, side, order_type, quantity, price = ask_order_details()

    print(f"\n Placing {order_type} {side} order for {symbol} with qty={quantity}, price={price}\n")

    order = bot.place_order(
        symbol=symbol,
        side=SIDE_BUY if side == "BUY" else SIDE_SELL,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    if order:
        print("Order placed successfully!")
        print("Order ID:", order['orderId'])
        print("Status:", order['status'])
    else:
        print(" Failed to place order. Check log.txt for more details.")
