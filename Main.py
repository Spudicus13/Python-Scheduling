import requests 
import json
import csv
import nicehash
import os
import datetime as dt
import sys
import boto3
import mysql.connector
import MySQLdb
import time
import pytz


#pip install pytz
#pip install boto3
#pip install mysql.connector


import time
milli_sec = int(round(time.time() * 1000))
print(milli_sec)

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

#response = requests.get('https://api2.nicehash.com/main/api/v2/public/apiVersion')
#print(response.text)
#hopeful = requests.get('https://api2.nicehash.com/main/api/v2/public/simplemultialgo/info')
#data = response.json()
#json_data = json.loads(hopeful.content)
#with open('hopeful.txt', 'w') as json_file:
#    json.dump(json_data, json_file)
#hopeful2 = requests.get('https://api2.nicehash.com/main/api/v2/mining/algorithms')
#json_data2 = json.loads(hopeful2.content)
#with open('hopeful2.txt', 'w') as json_file:
#    json.dump(json_data2, json_file)
#print(json_data2)
#column1 = "Algorithm".ljust(15)
#column2 = "Difficulty"
#text = json.dumps(json_data2, sort_keys=True, indent = 4)
#print(text)
#print('\n')
#print(column1, column2)
#print('\n')
#for s in range(len(json_data2['miningAlgorithms'])):
#    algorithm = json_data2['miningAlgorithms'][s]['algorithm']
#    algorithm = algorithm.ljust(15)
#    difficutly = json_data2['miningAlgorithms'][s]['minimalPoolDifficulty']
#    print(algorithm, "  ", difficutly)  


#get current date/time from nicehash server for verification
datetime = requests.get('https://api2.nicehash.com/api/v2/time')
date = datetime.json()
date = date['serverTime']
#print(date)

host = 'https://api2.nicehash.com'
org_id = '4ecfcf59-c3af-4923-b402-dc710e500934'
key = 'ecfdf1d7-db0e-436b-aaa4-408d7cbc4774'
secret = api_key
rigId = '125-02'
walletId = '33EkwcdMqbgtPGZFB4xWt6ouXj88UDqMXy'
walletId2 = '16piavZXVy7wK6acf8NArk1wwxvHjEff56'
walletId3 = '3Ce89tcD5aePECvE1RxSyRY3p2YNoEGxqY'

private_api = nicehash.private_api(host, org_id, key, secret, True)
public_api = nicehash.public_api(host)

respond2 = public_api.get_current_global_stats()
text2 = json.dumps(respond2, sort_keys=True, indent = 4)
#print(text2)

mainStats = requests.get('https://api2.nicehash.com/main/api/v2/mining/external/' + walletId + '/rigs2')
mainStats = mainStats.json()
mainStats = json.dumps(mainStats,sort_keys=True, indent = 4)
print(mainStats)

mainStats = requests.get('https://api2.nicehash.com/main/api/v2/mining/external/' + walletId + '/rigs2')
mainStats = mainStats.json()
print('\n')

totalHash = 0

for s in range(len(mainStats['miningRigs'])):
    rig = mainStats['miningRigs'][s]['rigId']
    rig = rig.ljust(15)
    hashrate = mainStats['miningRigs'][s]['stats'][0]['speedAccepted']
    print(rig, hashrate)
    totalHash = totalHash + hashrate

print('\n')

print(round(totalHash,2)," Current total MH/s")
print('\n')

profitCurrent = mainStats['totalProfitability']
print(round(profitCurrent,8)," BTC profitability / 24H")
print('\n')
profitCurrent = round(profitCurrent,8)


respond3 = requests.get('https://api2.nicehash.com/exchange/api/v2/info/prices')
currency = respond3.json()
currencyPrint = json.dumps(currency,sort_keys=True, indent = 4)
#print(currencyPrint)

btcCurrent = currency['BTCUSDC']
print("Current BTC Price:    $",btcCurrent)

ethCurrent = currency['ETHUSDC']
print("Current ETH Price:    $",ethCurrent)

ethbtcRatio = ethCurrent / btcCurrent * 100
print("ETH-BTC Percentage:  ",round(ethbtcRatio,2),"%")

profitUSD = btcCurrent * profitCurrent
print('\n')

print("Current Daily Profitability:    $",(round(profitUSD,2)))
print('\n')

perHash = profitUSD / totalHash *100
print(round(perHash,2),"¢/day/MH")

print('\n')

currencies = public_api.get_currencies()
currencies = json.dumps(currencies,sort_keys=True, indent = 4)
#print(currencies)

my_accounts = private_api.get_accounts()
my_accounts2 = json.dumps(my_accounts,sort_keys=True, indent = 4)
#print(my_accounts2)

print("Current Wallet value:  ", my_accounts['total']['totalBalance'])

print('\n')

#withdraw = requests.get('https://api2.nicehash.com/main/api/v2/mining/external/' + walletId2 + '/rigs/withdrawals')
#withdraw2 = withdraw.json()
#withdraw = json.dumps(withdraw2,sort_keys=True, indent = 4)
#print(withdraw)
#print('\n')


#withdraw = requests.get('https://api2.nicehash.com/main/api/v2/mining/external/' + walletId2 + '/rigs/withdrawals')
#withdraw = json.loads(withdraw.content)

#withdrawal_Total = 0
#timeInt = 0

#for s in range(len(withdraw['list'])):
#    withdrawalAMT = float(withdraw['list'][s]['amount'])
#    dateComplete = withdraw['list'][s]['created']
#    print(dateComplete)
#    timeInt = dateComplete
#    dateComplete = tz_from_utc_ms_ts(dateComplete, pytz.timezone('America/Los_Angeles'))
#    print("              ",withdrawalAMT," BTC")
#    print("Date paid:    ",dateComplete)
#    withdrawal_Total = withdrawal_Total + withdrawalAMT

#print('\n')

#timeInt = ("%d" % timeInt)
#print(timeInt)
#print('\n')

#print("Total BTC paid out:    ",round(withdrawal_Total,8))
#print('\n')

myDB = MySQLdb.connect(host="database-2.cf9iiadrwdnt.us-west-2.rds.amazonaws.com",port=3306,user="sstraughen",passwd="S3r3n1ty83",db="completeserve_database_2")
cHandler = myDB.cursor()
cHandler.execute('use base_inventory')

results = cHandler.fetchall()

#insert_statement = ("""insert into sas_btc_data (wallet_add, event_time, btc_price, eth_price, cents_per_mh, total_hash_rate, btc_profit) values ('33EkwcdMqbgtPGZFB4xWt6ouXj88UDqMXy','1614200379484', '56170.55', '1990.71', '8.07', '1145.45', '0.0016416')""")
#cursor.execute(insert_statement)

insert_statement2 = "insert into sas_btc_data (wallet_add,event_time, btc_price, eth_price, cents_per_mh, total_hash_rate, btc_profit) \
values ('%s', '%d', '%f', '%f', '%f', '%f', '%f')" % (walletId, milli_sec, btcCurrent, ethCurrent, perHash, totalHash, profitCurrent)

cHandler.execute(insert_statement2)
myDB.commit()

#try:
#   # Execute the SQL command
#   cHandler.execute(insert_statement)
#   # Commit your changes in the database
#   print("success")
#   myDB.commit()
#except:
#   # Rollback in case there is any error
#   myDB.rollback()
#   print("failure")













