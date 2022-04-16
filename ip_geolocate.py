import requests

api_key = "at_yOsYY61Z4NcyjabnUuXW2u007aj5X"
ipAddress = input("Enter IP address here:")
outputFormat = "JSON"

url1 = "https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey="
url2 = "&domainName="
url3 = "&outputFormat="

finalURL = url1 + api_key + url2 + ipAddress + url3 + outputFormat


url = "https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_yOsYY61Z4NcyjabnUuXW2u007aj5X&ipAddress=76.178.151.27"

payload={}
headers = {
  'Cookie': 'XSRF-TOKEN=eyJpdiI6IkFIcDVib3l6VTJBcWE4NVRkenhJekE9PSIsInZhbHVlIjoiQmIzVmp1QWhIbEVNNTJvT2Rpb2xEclhNUEx2RzVVQmVZbVFHZ1Q5b1BNQnFmNGN2S3lGdlFTQ1UzUUV0V0g1WSIsIm1hYyI6ImNkNmM1YmU5OTU4NWQzZDdlMjlhMDBlODBhYmJkODE5YWM0ZmMxZGI2ODhkNWZiNDA3NTg5ZGY0NzgyMDIwNTkifQ%3D%3D; emailverification_session=eyJpdiI6Ill1U2FsRVVYWWdQa2xZclU2ckxKRnc9PSIsInZhbHVlIjoiQjJzXC91OUpONE5wdmtiY2J2Z3BWbUs2V05GTVpXdlFlQkVsTlB0VWkwQWx3WTJmeDBTRDlSXC9VS2Z0RlNiZlBhQVVrOGR4dWlwcjQ5T2Vmc01mbEtoMnJGSUhqOHF4MCtIZUtXRG1uNWxxS25ka0NEZGNXVVNLZGIwTXd5XC8zNlgiLCJtYWMiOiI0ZTJhY2YwYjhlMjNjNGRiMWMzMDg4ZjAxNTcwOGQ0NDFiYzE2NjU5Zjk3MzE4MjRlZmEzNTc0MWQ4MmJhOWJhIn0%3D'
}

response = requests.request("GET", finalURL, headers=headers, data=payload)

print(response.text)