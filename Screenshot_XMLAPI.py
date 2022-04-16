import requests

api_key = "at_yOsYY61Z4NcyjabnUuXW2u007aj5X"
outputFormat = "jpg"
website = input("Enter website here:")

url1 = "https://website-screenshot.whoisxmlapi.com/api/v1?apiKey="
url2 = "&url="
url3 = "&imageOutputFormat="

finalURL = url1 + api_key + url2 + website + url3 + outputFormat

payload={}
headers = {
  'Cookie': 'XSRF-TOKEN=eyJpdiI6InJWU3lCSm1ESzRtXC9MRHd5dWFGTkFBPT0iLCJ2YWx1ZSI6InUzYkF3Z1FHelVDaGRVNjFLY3JuNGR0QXF0Y1pMQUdhUGtEZG1tOWFob0ZJaytwK2JSSk1tVVA0QVhcL0R2UU5iIiwibWFjIjoiYjFlZmFkZGVmZTU2NWY1MTYwYWEwODliNzg0YmQwZjg2YThjOGRkNWRkODcwNTEwYzBhZTc4MjgzOTY5M2Q0NSJ9; emailverification_session=eyJpdiI6IkhVTHpZTmZKQU5LUXF6QU9jYXE0ZGc9PSIsInZhbHVlIjoiMklpMjJlXC9SM3FLOWRYOCsrck5CQktGNWU0Tm5HQ1Naa0NxNVdFMklMd2N5SGs1c1o4elFDK25oNnllU3pcL3cwMG9UWVpzUXVFRjhVSk5TVnFlSjB4b0tkcjNpbVVyK1pBd1Uya2g4bzcyOW13OTk3N3VLSUJXT3VFN0pucTNtdSIsIm1hYyI6IjAzMThkNTQ3MTgzODVjMzQ1ZjNiYzYwNjM4YTc3NDAxNjE3NDA4ZWJkNzQ2MGU2ZDcyZTI0MmY5OWI0NzhhNzcifQ%3D%3D'
}

response = requests.request("GET", finalURL, headers=headers, data=payload)

file = open("xmlsample.jpg", "wb")
file.write(response.content)
file.close

print("Request complete.")