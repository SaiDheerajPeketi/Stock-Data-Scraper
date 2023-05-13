import requests
# import pandas as pd
from bs4 import BeautifulSoup
import re
#from rotating_proxies import get_free_proxies
import random
#from requests.auth import HTTPProxyAuth
import os
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
# from selenium import webdriver
# import chromedriver_binary
# import string
# import time
# from emailer import fun

# pd.options.display.float_format = '{:.2f}'.format

def readList():
    fr = open('entire_list_modified.txt','r')
    extracted_list = []
    i=0
    while True:
        line = fr.readline()
        if i==0:
            i = i+1
            continue
        if line=="":
            break
        extracted_list.append(line.replace("\n",""))
    fr.close()
    #print(extracted_list)
    return extracted_list



def generate_url():
    symbol = str(input('Enter Stock Symbol : '))
    url = f'https://finance.yahoo.com/quote/{symbol}'
    return url

def get_html(url,proxies):
    #header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    #response = requests.get(url, headers=header)
    i = 0
    while True:
        ind = random.randint(0,len(proxies)-1)
        proxy = proxies[ind]
        httpProxy = "http://"+proxy
        #httpsProxy = "https://"+"lajbfhob:lv8hi53mqepo@"+proxy
        #os.environ["http_proxy"] = httpProxy
        #os.environ["https_proxy"] = httpsProxy
        
        #auth = HTTPProxyAuth("lajbfhob","lv8hi53mqepo")
        #session = requests.Session()
        #retry = Retry(connect=3, backoff_factor=0.5)
        #adapter = HTTPAdapter(max_retries=retry)
        try:
            i=i+1
            response = requests.get(url, proxies={"http":httpProxy})
            if response.status_code == 200:
                print(response.text)
                return response.text
            else:
                continue
        except:
            if i==100:
                return None
            print("No Connection")
            pass
        
    
def parse_data(html):


    if html!=None:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1',{'class': 'D(ib) Fz(18px)'}).text
        price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
        change_price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
        change_percent = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
        previous_close = soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)'} and {'data-test':'PREV_CLOSE-value'}).text
        open_price = soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)'} and {'data-test':'OPEN-value'}).text

        # print(f'Stock Name : {title}')
        # print(f'Stock Price : {price}')
        # print(f'Change in Price : {change_price}')
        # print(f'Change in Percentage : {change_percent}')
        # print(f'Previous Close Price : {previous_close}')
        # print(f'Open Price : {open_price}')

        stock_data = {
            'name':title,
            'price':price,
            'change_price':change_price,
            'change_percent':change_percent,
            'previous_close':previous_close,
            'open_price':open_price
        }

        return stock_data


def main(url,proxies): 
    # Get HTML
    html = get_html(url,proxies)
    #html = get_html(url)

    #Processing Data
    data = parse_data(html)
    # fun(str(data))
    print(data)
    

if __name__ == '__main__':
    # proxies = readList()
    # print(proxies)
    proxies = ['lajbfhob:lv8hi53mqepo@2.56.119.93:5074', 'lajbfhob:lv8hi53mqepo@185.199.229.156:7492', 'lajbfhob:lv8hi53mqepo@185.199.228.220:7300', 'lajbfhob:lv8hi53mqepo@185.199.231.45:8382', 'lajbfhob:lv8hi53mqepo@188.74.210.207:6286', 'lajbfhob:lv8hi53mqepo@188.74.183.10:8279', 'lajbfhob:lv8hi53mqepo@188.74.210.21:6100', 'lajbfhob:lv8hi53mqepo@45.155.68.129:8133', 'lajbfhob:lv8hi53mqepo@154.95.36.199:6893', 'lajbfhob:lv8hi53mqepo@45.94.47.66:8110', 'ttdbrnet:c7g848hyg3pl@2.56.119.93:5074', 'ttdbrnet:c7g848hyg3pl@185.199.229.156:7492', 'ttdbrnet:c7g848hyg3pl@185.199.228.220:7300', 'ttdbrnet:c7g848hyg3pl@185.199.231.45:8382', 'ttdbrnet:c7g848hyg3pl@188.74.210.207:6286', 'ttdbrnet:c7g848hyg3pl@188.74.183.10:8279', 'ttdbrnet:c7g848hyg3pl@188.74.210.21:6100', 'ttdbrnet:c7g848hyg3pl@45.155.68.129:8133', 'ttdbrnet:c7g848hyg3pl@154.95.36.199:6893', 'ttdbrnet:c7g848hyg3pl@45.94.47.66:8110', 'ihfqarwo:2qz7hb8xfuw9@2.56.119.93:5074', 'ihfqarwo:2qz7hb8xfuw9@185.199.229.156:7492', 'ihfqarwo:2qz7hb8xfuw9@185.199.228.220:7300', 'ihfqarwo:2qz7hb8xfuw9@185.199.231.45:8382', 'ihfqarwo:2qz7hb8xfuw9@188.74.210.207:6286', 'ihfqarwo:2qz7hb8xfuw9@188.74.183.10:8279', 'ihfqarwo:2qz7hb8xfuw9@188.74.210.21:6100', 'ihfqarwo:2qz7hb8xfuw9@45.155.68.129:8133', 'ihfqarwo:2qz7hb8xfuw9@154.95.36.199:6893', 'ihfqarwo:2qz7hb8xfuw9@45.94.47.66:8110', 'mdtvpudr:mn00jhz8vp8i@2.56.119.93:5074', 'mdtvpudr:mn00jhz8vp8i@185.199.229.156:7492', 'mdtvpudr:mn00jhz8vp8i@185.199.228.220:7300', 'mdtvpudr:mn00jhz8vp8i@185.199.231.45:8382', 'mdtvpudr:mn00jhz8vp8i@188.74.210.207:6286', 'mdtvpudr:mn00jhz8vp8i@188.74.183.10:8279', 'mdtvpudr:mn00jhz8vp8i@188.74.210.21:6100', 'mdtvpudr:mn00jhz8vp8i@45.155.68.129:8133', 'mdtvpudr:mn00jhz8vp8i@154.95.36.199:6893', 'mdtvpudr:mn00jhz8vp8i@45.94.47.66:8110', 'mtgfloqx:a80uts13euty@2.56.119.93:5074', 'mtgfloqx:a80uts13euty@185.199.229.156:7492', 'mtgfloqx:a80uts13euty@185.199.228.220:7300', 'mtgfloqx:a80uts13euty@185.199.231.45:8382', 'mtgfloqx:a80uts13euty@188.74.210.207:6286', 'mtgfloqx:a80uts13euty@188.74.183.10:8279', 'mtgfloqx:a80uts13euty@188.74.210.21:6100', 'mtgfloqx:a80uts13euty@45.155.68.129:8133', 'mtgfloqx:a80uts13euty@154.95.36.199:6893', 'mtgfloqx:a80uts13euty@45.94.47.66:8110', 'rsklpaqj:9kjpmrs88quy@2.56.119.93:5074', 'rsklpaqj:9kjpmrs88quy@185.199.229.156:7492', 'rsklpaqj:9kjpmrs88quy@185.199.228.220:7300', 'rsklpaqj:9kjpmrs88quy@185.199.231.45:8382', 'rsklpaqj:9kjpmrs88quy@188.74.210.207:6286', 'rsklpaqj:9kjpmrs88quy@188.74.183.10:8279', 'rsklpaqj:9kjpmrs88quy@188.74.210.21:6100', 'rsklpaqj:9kjpmrs88quy@45.155.68.129:8133', 'rsklpaqj:9kjpmrs88quy@154.95.36.199:6893', 'rsklpaqj:9kjpmrs88quy@45.94.47.66:8110', 'xwhxtqnh:0j5v8844zi9n@2.56.119.93:5074', 'xwhxtqnh:0j5v8844zi9n@185.199.229.156:7492', 'xwhxtqnh:0j5v8844zi9n@185.199.228.220:7300', 'xwhxtqnh:0j5v8844zi9n@185.199.231.45:8382', 'xwhxtqnh:0j5v8844zi9n@188.74.210.207:6286', 'xwhxtqnh:0j5v8844zi9n@188.74.183.10:8279', 
'xwhxtqnh:0j5v8844zi9n@188.74.210.21:6100', 'xwhxtqnh:0j5v8844zi9n@45.155.68.129:8133', 'xwhxtqnh:0j5v8844zi9n@154.95.36.199:6893', 'xwhxtqnh:0j5v8844zi9n@45.94.47.66:8110', 'ibrsxsea:lldoy5fifqf4@2.56.119.93:5074', 'ibrsxsea:lldoy5fifqf4@185.199.229.156:7492', 'ibrsxsea:lldoy5fifqf4@185.199.228.220:7300', 'ibrsxsea:lldoy5fifqf4@185.199.231.45:8382', 'ibrsxsea:lldoy5fifqf4@188.74.210.207:6286', 'ibrsxsea:lldoy5fifqf4@188.74.183.10:8279', 'ibrsxsea:lldoy5fifqf4@188.74.210.21:6100', 'ibrsxsea:lldoy5fifqf4@45.155.68.129:8133', 'ibrsxsea:lldoy5fifqf4@154.95.36.199:6893', 'ibrsxsea:lldoy5fifqf4@45.94.47.66:8110', 'fqpxmvcr:by7vhi41f05t@2.56.119.93:5074', 'fqpxmvcr:by7vhi41f05t@185.199.229.156:7492', 'fqpxmvcr:by7vhi41f05t@185.199.228.220:7300', 'fqpxmvcr:by7vhi41f05t@185.199.231.45:8382', 'fqpxmvcr:by7vhi41f05t@188.74.210.207:6286', 'fqpxmvcr:by7vhi41f05t@188.74.183.10:8279', 'fqpxmvcr:by7vhi41f05t@188.74.210.21:6100', 'fqpxmvcr:by7vhi41f05t@45.155.68.129:8133', 'fqpxmvcr:by7vhi41f05t@154.95.36.199:6893', 
'fqpxmvcr:by7vhi41f05t@45.94.47.66:8110', 'cadtqxht:zoqxzzeseyrh@2.56.119.93:5074', 'cadtqxht:zoqxzzeseyrh@185.199.229.156:7492', 'cadtqxht:zoqxzzeseyrh@185.199.228.220:7300', 'cadtqxht:zoqxzzeseyrh@185.199.231.45:8382', 'cadtqxht:zoqxzzeseyrh@188.74.210.207:6286', 'cadtqxht:zoqxzzeseyrh@188.74.183.10:8279', 'cadtqxht:zoqxzzeseyrh@188.74.210.21:6100', 'cadtqxht:zoqxzzeseyrh@45.155.68.129:8133', 'cadtqxht:zoqxzzeseyrh@154.95.36.199:6893', 'cadtqxht:zoqxzzeseyrh@45.94.47.66:8110']
    # proxies = ['lajbfhob:lv8hi53mqepo@2.56.119.93:5074', 'lajbfhob:lv8hi53mqepo@185.199.229.156:7492', 'lajbfhob:lv8hi53mqepo@185.199.228.220:7300', 'lajbfhob:lv8hi53mqepo@185.199.231.45:8382', 'lajbfhob:lv8hi53mqepo@188.74.210.207:6286', 'lajbfhob:lv8hi53mqepo@188.74.183.10:8279', 'lajbfhob:lv8hi53mqepo@188.74.210.21:6100', 'lajbfhob:lv8hi53mqepo@45.155.68.129:8133', 'lajbfhob:lv8hi53mqepo@154.95.36.199:6893', 'lajbfhob:lv8hi53mqepo@45.94.47.66:8110']
    # Get User Input
    #proxies = get_free_proxies
    print(len(proxies))
    url = generate_url()
    #main(url,proxies)
    main(url,proxies)

    
    # i=0;

    # while(i<20):
    #     main(url)
    #     time.sleep(30)
    #     i+=1




#is_link = 'https://finance.yahoo.com/quote/AAPL/financials?p=AAPL'
# driver = webdriver.Chrome()
# driver.get(is_link)
# html = driver.execute_script('return document.body.innerHTML;')
# soup = BeautifulSoup(html, 'lxml')

# close_price = [entry]



