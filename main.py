import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import chromedriver_binary
import string

pd.options.display.float_format = '{:.2f}'.format

def generate_url():
    symbol = str(input('Enter Stock Symbol : '))
    url = f'https://finance.yahoo.com/quote/{symbol}'
    return url

def get_html(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        return response.text
    else:
        return None
    
def parse_data(html):
    '''
    
    previous_close
    open
    '''

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1',{'class': 'D(ib) Fz(18px)'}).text
    price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
    change_price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
    change_percent = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    previous_close = soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)'} and {'data-test':'PREV_CLOSE-value'}).text
    open_price = soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)'} and {'data-test':'OPEN-value'}).text

    print(f'Stock Name : {title}')
    print(f'Stock Price : {price}')
    print(f'Change in Price : {change_price}')
    print(f'Change in Percentage : {change_percent}')
    print(f'Previous Close Price : {previous_close}')
    print(f'Open Price : {open_price}')


def main(): 
    # Get User Input
    url = generate_url()

    # Get HTML
    html = get_html(url)

    #Processing Data
    parse_data(html)
    

if __name__ == '__main__':
    main()






#is_link = 'https://finance.yahoo.com/quote/AAPL/financials?p=AAPL'
# driver = webdriver.Chrome()
# driver.get(is_link)
# html = driver.execute_script('return document.body.innerHTML;')
# soup = BeautifulSoup(html, 'lxml')

# close_price = [entry]



