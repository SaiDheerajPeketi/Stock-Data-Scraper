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
    proxies = ['lajbfhob:lv8hi53mqepo@2.56.119.93:5074', 'lajbfhob:lv8hi53mqepo@185.199.229.156:7492', 'lajbfhob:lv8hi53mqepo@185.199.228.220:7300', 'lajbfhob:lv8hi53mqepo@185.199.231.45:8382', 'lajbfhob:lv8hi53mqepo@188.74.210.207:6286', 'lajbfhob:lv8hi53mqepo@188.74.183.10:8279', 'lajbfhob:lv8hi53mqepo@188.74.210.21:6100', 'lajbfhob:lv8hi53mqepo@45.155.68.129:8133', 'lajbfhob:lv8hi53mqepo@154.95.36.199:6893', 'lajbfhob:lv8hi53mqepo@45.94.47.66:8110']
    # Get User Input
    #proxies = get_free_proxies
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



