import requests

url = 'https://pv.sohu.com/cityjson?ie=utf-8'


proxies = {
    'https':'https://119.101.112.64:9999',
    'http':'http://119.101.112.152:9999',
}

req = requests.get(url, proxies=proxies, timeout=4.0)
# req = requests.get(url)
# req.encoding = None
print(req.text)

