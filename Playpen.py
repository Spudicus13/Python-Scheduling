from time import time
import requests
import json
import time
import uuid


api_key = "at_yOsYY61Z4NcyjabnUuXW2u007aj5X"
outputFormat = "JSON"
website = input("Enter website here:")

url1 = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey="
url2 = "&domainName="
url3 = "&outputFormat="

finalURL = url1 + api_key + url2 + website + url3 + outputFormat


response = requests.request("GET", finalURL)


data = response.json()
node = data['WhoisRecord']['technicalContact']['name']
print(node)

#print(response.text)

milliseconds = int(round(time.time()*1000))
nonce = uuid.uuid4().hex

key = 'b042fb79-e881-480d-ae76-72b49d41cb5f'
secret = 'f788b8c9-9717-4e29-bb94-6e785379cac5dca3a020-ae0d-4474-9ce7-b1d0eb954c1f'
org_id = '4ecfcf59-c3af-4923-b402-dc710e500934'




sortParam = 'RIG_NAME'
sortDir = 'ASC'


url = 'https://api2.nicehash.com/main/api/v2/mining/rigs/activeWorkers'

headers = {
    'X-Time': milliseconds,
    'X-Nonce': nonce,
    'X-Organization-Id': '4ecfcf59-c3af-4923-b402-dc710e500934',
    'X-Auth': 'b042fb79-e881-480d-ae76-72b49d41cb5f:3f79da8733180fc28758fade6f6ada4dce8d225f65b46e607a9f610161f6d499',
    'X-Request-Id': 'wjdh0x1tlmri4i8nr73p74jqrrc5rmgl',
    'X-User-Agent': '',
    'X-User-Lang': 'en',
    '': '',
    '': '',

}






rigStats = requests.get('https://api2.nicehash.com/main/api/v2/mining/rigs/activeWorkers')









