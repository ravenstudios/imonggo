import requests



TOKEN = "64e6377749b831ed4fa8202e8daf31bb51ce8a43:X"
URL = "https://ravenstudiosrob.imonggo.com/api/products.xml"

headers = {
    'Accept': 'application/xml',
    'Content-Type': 'application/xml',
}


auth = (TOKEN, 'X')
response = requests.get(URL, headers=headers, auth=auth)






print(response.text)
