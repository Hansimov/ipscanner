import requests

# url = 'http://www.66ip.cn/mo.php?sxb=&tqsl=10000&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea='

# with open('cookie.txt', 'r') as rf:
#     cookie = rf.readline().strip()
#     user_agent = rf.readline().strip()

# headers = {
#     'Cookie': cookie,
#     'User-Agent': user_agent,
# }

# sess = requests.Session()
# req = sess.get(url, headers=headers)
# req.encoding = None
# # print(req.text)

# with open('66.html', mode='w') as wf:
#     wf.write(req.text)


import re

with open('66.html', mode='r') as rf:
    doc = rf.read()
    # print(doc)

link = 'http://pv.sohu.com/cityjson?ie=utf-8'
ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', doc)
# print(ip_list)

valid_count = 0
used_count = 0
total_count = len(ip_list)

for ip in ip_list:
    proxies = {
        'http': 'http://'+ ip
    }
    print('>>> Trying ip: ' + ip)
    used_count += 1
    try:
        req = requests.get(link, proxies=proxies, timeout=4.0)
        # print(req.text)
        valid_count += 1
        print('{:0>5}/{:0>5}'.format(valid_count, used_count))
        print(re.findall(r'{.*}',req.text)[0])
    except:
        print('--- Failed ip: ' + ip)

# print(re.findall(r'{.*}','var returnCitySN = {"cip": "139.5.71.17", "cid": "CN", "cname": "CHINA"};')[0])