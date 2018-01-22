# live price on BX & Bittrex
import time, json, requests
from datetime import datetime
# from forex_python.converter import CurrencyRates
# Bitfinex api https://api.bitfinex.com/v1/pubticker/btcusd

//thaibai rate 
def thbrate():
    thb = requests.get("https://v3.exchangerate-api.com/bulk/76662b71dfb2c14a89b1afda/USD")
    return thb.json()['rates']['THB']
//-----coins-----
def bx_BTC():
    bx_BTC_tick = requests.get("https://bx.in.th/api/orderbook/?pairing=1")
    return bx_BTC_tick.json()['bids'][0][0]
def bx_XRP():
    bx_XRP_tick = requests.get("https://bx.in.th/api/orderbook/?pairing=25")
    return bx_XRP_tick.json()['bids'][0][0]
def bx_OMG():
    bx_OMG_tick = requests.get("https://bx.in.th/api/orderbook/?pairing=26")
    return bx_OMG_tick.json()['bids'][0][0]
def bx_EVX():
    bx_EVX_tick = requests.get("https://bx.in.th/api/orderbook/?pairing=28")
    return bx_EVX_tick.json()['bids'][0][0]

def bt_BTC():
    bt_BTC_tick = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc")
    return  bt_BTC_tick.json()['result']['Last']
def bt_XRP():
    bt_XRP_tick = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=usdt-xrp")
    return  bt_XRP_tick.json()['result']['Last']
def bt_OMG():
    bt_OMG_tick = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=usdt-omg")
    return  bt_OMG_tick.json()['result']['Last']
    
thb_l  = float(thbrate())
while True:   
    bbtc_l = float(bx_BTC())
    bxrp_l = float(bx_XRP())
    bomg_l = float(bx_OMG())
    bevx_l = float(bx_EVX())

    btbtc_l = float(bt_BTC())
    btxrp_l = float(bt_XRP())
    btomg_l = float(bt_OMG())

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),">> 1USD = {:.2f}THB <<".format(thb_l))
    print("-------BX--------|------Bittrex(THB)-----")
    print("BTC =  {0:.2f}".format(bbtc_l),"|\t{0:.2f}".format(btbtc_l*thb_l))
    print("XRP =  {0:.2f}".format(bxrp_l), "\t |\t{0:.2f}".format(btxrp_l*thb_l))
    print("EVX =  {0:.2f}".format(bevx_l), "\t |\t-")
    print("OMG =  {0:.2f}".format(bomg_l),"\t |\t{0:.2f}".format(btomg_l*thb_l))
    print("-------------r4fr4sh---------------------")
    
    time.sleep(5)
