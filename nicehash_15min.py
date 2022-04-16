import requests 
import json
import csv
import os
import datetime as dt
import sys
import boto3
import mysql.connector
import pymysql
import time
import pytz

#must be run as python3
#pip install pytz
#pip install boto3
#pip install mysql.connector

import time
milli_sec = int(round(time.time() * 1000))

epoch = dt.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

def tz_from_utc_ms_ts(utc_ms_ts, tz_info):
    """Given millisecond utc timestamp and a timezone return dateime

    :param utc_ms_ts: Unix UTC timestamp in milliseconds
    :param tz_info: timezone info
    :return: timezone aware datetime
    """
    # convert from time stamp to datetime
    utc_datetime = dt.datetime.utcfromtimestamp(utc_ms_ts / 1000.)

    # set the timezone to UTC, and then convert to desired timezone
    return utc_datetime.replace(tzinfo=pytz.timezone('UTC')).astimezone(tz_info)

api_key = os.environ.get('nicehash_API_KEY_1')

#get current date/time from nicehash server for verification
datetime = requests.get('https://api2.nicehash.com/api/v2/time')
date = datetime.json()
date = date['serverTime']

host = 'https://api2.nicehash.com'
org_id = '4ecfcf59-c3af-4923-b402-dc710e500934'
key = 'ecfdf1d7-db0e-436b-aaa4-408d7cbc4774'
secret = api_key
rigId = '125-02'
walletId = '33EkwcdMqbgtPGZFB4xWt6ouXj88UDqMXy'

mainStats = requests.get('https://api2.nicehash.com/main/api/v2/mining/external/' + walletId + '/rigs2')
mainStats = mainStats.json()
mainStats = json.dumps(mainStats,sort_keys=True, indent = 4)

mainStats = requests.get('https://api2.nicehash.com/main/api/v2/mining/external/' + walletId + '/rigs2')
mainStats = mainStats.json()

totalHash = 0

for s in range(len(mainStats['miningRigs'])):
    rig = mainStats['miningRigs'][s]['rigId']
    rig = rig.ljust(15)
    hashrate = mainStats['miningRigs'][s]['stats'][0]['speedAccepted']
    totalHash = totalHash + hashrate

profitCurrent = mainStats['totalProfitability']
profitCurrent = round(profitCurrent,8)

respond3 = requests.get('https://api2.nicehash.com/exchange/api/v2/info/prices')
currency = respond3.json()

btcCurrent = currency['BTCUSDC']
ethCurrent = currency['ETHUSDC']
ethbtcRatio = ethCurrent / btcCurrent * 100
profitUSD = btcCurrent * profitCurrent
perHash = profitUSD / totalHash *100

myDB = pymysql.connect(host="database-2.cf9iiadrwdnt.us-west-2.rds.amazonaws.com",port=3306,user="sstraughen",passwd="S3r3n1ty83",db="completeserve_database_2")
cHandler = myDB.cursor()
cHandler.execute('use base_inventory')

insert_statement2 = "insert into sas_btc_data (wallet_add,event_time, btc_price, eth_price, cents_per_mh, total_hash_rate, btc_profit) \
values ('%s', '%d', '%f', '%f', '%f', '%f', '%f')" % (walletId, milli_sec, btcCurrent, ethCurrent, perHash, totalHash, profitCurrent)

cHandler.execute(insert_statement2)
myDB.commit()

