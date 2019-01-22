import requests

url = 'http://www.66ip.cn/mo.php?sxb=&tqsl=9999&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea='

with open('cookie.txt', 'r') as rf:
    cookie = rf.readline().strip()
    user_agent = rf.readline().strip()

headers = {
    'Cookie': cookie,
    'User-Agent': user_agent,
}


sess = requests.Session()
req = sess.get(url, headers=headers)
print(req.text)
