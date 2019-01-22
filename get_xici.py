import requests

# url = 'https://www.xicidaili.com/wn/'
# headers = {'user-agent': 'thank-you-xici'}
# req = requests.get(url, headers=headers)
# print(req.text)
# with open('xici.html', 'w') as wf:
#     wf.write(req.text)

from lxml import etree

def replaceKeys(dict_in):
    keys = [
        ['国家',      'country'],
        ['IP地址',    'ip'],
        ['端口',      'port'],
        ['服务器地址', 'server_ip'],
        ['是否匿名',   'is_anony'],
        ['类型',      'type'],
        ['速度',      'speed'],
        ['连接时间',   'connect_time'],
        ['存活时间',  'alive_time'],
        ['验证时间',  'verify_time'],
    ]
    for key in keys:
        dict_in[key[1]] = dict_in[key[0]]
        del dict_in[key[0]]
    return dict_in

with open('xici.html', 'r') as rf:
    doc = rf.read()

table = etree.HTML(doc).find('.//*[@id="ip_list"]')

ip_list = []
rows = iter(table)
keys = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    # print(dict(zip(keys, values)))
    dict_old = dict(zip(keys, values))
    ip_list.append(replaceKeys(dict_old))

url = 'https://pv.sohu.com/cityjson?ie=utf-8'

for tr in ip_list:
    # print(tr['ip'], tr['port'], tr['type'])
    proxies = {
        'https': 'https://'+ tr['ip'] + ':' + tr['port']
    }
    try:
        req = requests.get(url, proxies=proxies, timeout=4.0)
        print(req.text)
    except:
        print('--- Failed ip: ' + tr['ip'])