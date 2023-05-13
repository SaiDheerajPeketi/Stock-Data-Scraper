#Server End Code
from flask import Flask
from flask import request
from flask import make_response
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re
import random
import pytz

ip = ""

def generate_url(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'
    return url

def get_html(url,proxy_list):
    ind = random.randint(0,len(proxy_list)-1)
    global ip
    proxy = proxy_list[ind]
    ip = proxy
    httpProxy = "http://"+ proxy
    response = requests.get(url, proxies = {"http":httpProxy})
    if response.status_code == 200:
        return response.text
    else:
        return None
    #header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    # while True:
    #     ind = random.randint(0,len(proxy_list)-1)
    #     global ip
    #     proxy = proxy_list[ind]
    #     ip = proxy
    #     httpProxy = "http://"+ proxy
    #     try:
    #         #response = requests.get(url, headers=header)
    #         response = requests.get(url, proxies = {"http":httpProxy})
    #         if response.status_code == 200:
    #             return response.text
    #         else:
    #             continue
    #     except:
    #         pass


def parse_data(html):
    if html != None:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1',{'class': 'D(ib) Fz(18px)'}).text
        price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
        change_price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
        change_percent = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
        previous_close = soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)'} and {'data-test':'PREV_CLOSE-value'}).text
        open_price = soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)'} and {'data-test':'OPEN-value'}).text
        now = datetime.now(pytz.timezone('Asia/Kolkata'))
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        price = re.sub(",","",price)

        stock_data = {
            'name':title,
            'price':price,
            'change_price':change_price,
            'change_percent':change_percent,
            'previous_close':previous_close,
            'open_price':open_price,
            'time':dt_string,
            'ip':ip
        }
        return stock_data
    else:
        return None



app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def handle_request():
    stock_symbol = str(request.args.get('stock_symbol')) #Request the ?stock_symbol = a
    proxy_list = ['lajbfhob:lv8hi53mqepo@2.56.119.93:5074', 'lajbfhob:lv8hi53mqepo@185.199.229.156:7492', 'lajbfhob:lv8hi53mqepo@185.199.228.220:7300', 'lajbfhob:lv8hi53mqepo@185.199.231.45:8382', 'lajbfhob:lv8hi53mqepo@188.74.210.207:6286', 'lajbfhob:lv8hi53mqepo@188.74.183.10:8279', 'lajbfhob:lv8hi53mqepo@188.74.210.21:6100', 'lajbfhob:lv8hi53mqepo@45.155.68.129:8133', 'lajbfhob:lv8hi53mqepo@154.95.36.199:6893', 'lajbfhob:lv8hi53mqepo@45.94.47.66:8110', 'ttdbrnet:c7g848hyg3pl@2.56.119.93:5074', 'ttdbrnet:c7g848hyg3pl@185.199.229.156:7492', 'ttdbrnet:c7g848hyg3pl@185.199.228.220:7300', 'ttdbrnet:c7g848hyg3pl@185.199.231.45:8382', 'ttdbrnet:c7g848hyg3pl@188.74.210.207:6286', 'ttdbrnet:c7g848hyg3pl@188.74.183.10:8279', 'ttdbrnet:c7g848hyg3pl@188.74.210.21:6100', 'ttdbrnet:c7g848hyg3pl@45.155.68.129:8133', 'ttdbrnet:c7g848hyg3pl@154.95.36.199:6893', 'ttdbrnet:c7g848hyg3pl@45.94.47.66:8110', 'ihfqarwo:2qz7hb8xfuw9@2.56.119.93:5074', 'ihfqarwo:2qz7hb8xfuw9@185.199.229.156:7492', 'ihfqarwo:2qz7hb8xfuw9@185.199.228.220:7300', 'ihfqarwo:2qz7hb8xfuw9@185.199.231.45:8382', 'ihfqarwo:2qz7hb8xfuw9@188.74.210.207:6286', 'ihfqarwo:2qz7hb8xfuw9@188.74.183.10:8279', 'ihfqarwo:2qz7hb8xfuw9@188.74.210.21:6100', 'ihfqarwo:2qz7hb8xfuw9@45.155.68.129:8133', 'ihfqarwo:2qz7hb8xfuw9@154.95.36.199:6893', 'ihfqarwo:2qz7hb8xfuw9@45.94.47.66:8110', 'mdtvpudr:mn00jhz8vp8i@2.56.119.93:5074', 'mdtvpudr:mn00jhz8vp8i@185.199.229.156:7492', 'mdtvpudr:mn00jhz8vp8i@185.199.228.220:7300', 'mdtvpudr:mn00jhz8vp8i@185.199.231.45:8382', 'mdtvpudr:mn00jhz8vp8i@188.74.210.207:6286', 'mdtvpudr:mn00jhz8vp8i@188.74.183.10:8279', 'mdtvpudr:mn00jhz8vp8i@188.74.210.21:6100', 'mdtvpudr:mn00jhz8vp8i@45.155.68.129:8133', 'mdtvpudr:mn00jhz8vp8i@154.95.36.199:6893', 'mdtvpudr:mn00jhz8vp8i@45.94.47.66:8110', 'mtgfloqx:a80uts13euty@2.56.119.93:5074', 'mtgfloqx:a80uts13euty@185.199.229.156:7492', 'mtgfloqx:a80uts13euty@185.199.228.220:7300', 'mtgfloqx:a80uts13euty@185.199.231.45:8382', 'mtgfloqx:a80uts13euty@188.74.210.207:6286', 'mtgfloqx:a80uts13euty@188.74.183.10:8279', 'mtgfloqx:a80uts13euty@188.74.210.21:6100', 'mtgfloqx:a80uts13euty@45.155.68.129:8133', 'mtgfloqx:a80uts13euty@154.95.36.199:6893', 'mtgfloqx:a80uts13euty@45.94.47.66:8110', 'rsklpaqj:9kjpmrs88quy@2.56.119.93:5074', 'rsklpaqj:9kjpmrs88quy@185.199.229.156:7492', 'rsklpaqj:9kjpmrs88quy@185.199.228.220:7300', 'rsklpaqj:9kjpmrs88quy@185.199.231.45:8382', 'rsklpaqj:9kjpmrs88quy@188.74.210.207:6286', 'rsklpaqj:9kjpmrs88quy@188.74.183.10:8279', 'rsklpaqj:9kjpmrs88quy@188.74.210.21:6100', 'rsklpaqj:9kjpmrs88quy@45.155.68.129:8133', 'rsklpaqj:9kjpmrs88quy@154.95.36.199:6893', 'rsklpaqj:9kjpmrs88quy@45.94.47.66:8110', 'xwhxtqnh:0j5v8844zi9n@2.56.119.93:5074', 'xwhxtqnh:0j5v8844zi9n@185.199.229.156:7492', 'xwhxtqnh:0j5v8844zi9n@185.199.228.220:7300', 'xwhxtqnh:0j5v8844zi9n@185.199.231.45:8382', 'xwhxtqnh:0j5v8844zi9n@188.74.210.207:6286', 'xwhxtqnh:0j5v8844zi9n@188.74.183.10:8279',
'xwhxtqnh:0j5v8844zi9n@188.74.210.21:6100', 'xwhxtqnh:0j5v8844zi9n@45.155.68.129:8133', 'xwhxtqnh:0j5v8844zi9n@154.95.36.199:6893', 'xwhxtqnh:0j5v8844zi9n@45.94.47.66:8110', 'ibrsxsea:lldoy5fifqf4@2.56.119.93:5074', 'ibrsxsea:lldoy5fifqf4@185.199.229.156:7492', 'ibrsxsea:lldoy5fifqf4@185.199.228.220:7300', 'ibrsxsea:lldoy5fifqf4@185.199.231.45:8382', 'ibrsxsea:lldoy5fifqf4@188.74.210.207:6286', 'ibrsxsea:lldoy5fifqf4@188.74.183.10:8279', 'ibrsxsea:lldoy5fifqf4@188.74.210.21:6100', 'ibrsxsea:lldoy5fifqf4@45.155.68.129:8133', 'ibrsxsea:lldoy5fifqf4@154.95.36.199:6893', 'ibrsxsea:lldoy5fifqf4@45.94.47.66:8110', 'fqpxmvcr:by7vhi41f05t@2.56.119.93:5074', 'fqpxmvcr:by7vhi41f05t@185.199.229.156:7492', 'fqpxmvcr:by7vhi41f05t@185.199.228.220:7300', 'fqpxmvcr:by7vhi41f05t@185.199.231.45:8382', 'fqpxmvcr:by7vhi41f05t@188.74.210.207:6286', 'fqpxmvcr:by7vhi41f05t@188.74.183.10:8279', 'fqpxmvcr:by7vhi41f05t@188.74.210.21:6100', 'fqpxmvcr:by7vhi41f05t@45.155.68.129:8133', 'fqpxmvcr:by7vhi41f05t@154.95.36.199:6893',
'fqpxmvcr:by7vhi41f05t@45.94.47.66:8110', 'cadtqxht:zoqxzzeseyrh@2.56.119.93:5074', 'cadtqxht:zoqxzzeseyrh@185.199.229.156:7492', 'cadtqxht:zoqxzzeseyrh@185.199.228.220:7300', 'cadtqxht:zoqxzzeseyrh@185.199.231.45:8382', 'cadtqxht:zoqxzzeseyrh@188.74.210.207:6286', 'cadtqxht:zoqxzzeseyrh@188.74.183.10:8279', 'cadtqxht:zoqxzzeseyrh@188.74.210.21:6100', 'cadtqxht:zoqxzzeseyrh@45.155.68.129:8133', 'cadtqxht:zoqxzzeseyrh@154.95.36.199:6893', 'cadtqxht:zoqxzzeseyrh@45.94.47.66:8110']
    url = generate_url(stock_symbol)
    html = None
    while html==None:
        html = get_html(url,proxy_list)
    data_set = parse_data(html)
    # data_set = {"stock_received": stock_symbol, "timestamp": time.time()}
    json_dump = json.dumps(data_set)
    return make_response(json_dump,200)