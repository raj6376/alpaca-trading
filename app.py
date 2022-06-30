from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd

URL = 'https://paper-api.alpaca.markets'
API_Key = 'PKUAZ4FKQQONFW44SX4H'
Secret_Key = 'yQbdDs7m6FlLzjHM1zfYLbVNey9Z3fIfsuyKu5v0'

print("... Welcome to Alpaca Trading Bot ...")

api = REST(key_id=API_Key,secret_key=Secret_Key, base_url=URL)

bars = api.get_crypto_bars("BTCUSD", TimeFrame.Minute).df
# bars = api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df
# print(bars)

#order_buy = api.submit_order('BTCUSD', qty=1, side='buy')
#print(order_buy)

def get_position(symbol):
    positions = api.list_positions()
    # positions_qty = float(api.get_position(symbol).qty)
    for p in positions:
        if p.symbol == symbol:
            return symbol, float(p.qty)
    return symbol, float(0)

a = get_position('BTCUSD')
print(a)




