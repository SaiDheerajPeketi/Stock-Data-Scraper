import requests
import random
from bs4 import BeautifulSoup as bs
import traceback

import main

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    #request and grab content
    soup = bs(requests.get(url).content, 'html.parser')
    #to store proxies
    proxies = []
    for row in soup.find("table",attrs={"class": "table-striped"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue

    return proxies


proxies = get_free_proxies()
url = "http://httpbin.org/ip"

count = 0

while True:
    random_int = random.randint(0,len(proxies)-1)
    proxy = proxies[random_int]

    print(str(count) + " " + proxy)
    print(type(proxy))

    try:
        response = requests.get(url, proxies={"http":proxy, "https":proxy})
        print(response.json())
    except:
        # if proxy is pre-occupied
        print("Not Available")
    
    count+=1


# def get_html():
#     header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
#     url = "https://free-proxy-list.net/"
#     response = requests.get(url, headers=header)
#     print(response.text)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None
    
# def parse_proxies(html):
#     soup = bs(html,'html.parser')
#     table = soup.find("span",{"class":"block"} and {"style":"width: 126px; max-width: 126px;"})
#     print(table)
#     rows = table.find_all("tr")
#     proxies = []
#     for i in rows:
#         ip = i.find_all("span")[0].text
#         port = i.find_all("span")[1].text
#         proxies.append(str(ip) + ":" + str(port))
#     return proxies



# def main():
    
#     print(proxies)

# if __name__ == '__main__':
#     main()