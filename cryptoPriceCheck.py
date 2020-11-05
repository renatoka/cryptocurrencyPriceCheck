import requests
import bs4
from bs4 import BeautifulSoup
import time


def checkPrice():
    while True:
        r = requests.Session()
        #Change this url to cryptocurrency you want to check
        #URL must be from livecoinwatch.com
        r.get('https://www.livecoinwatch.com/price/Bitcoin-BTC')
        soup = bs4.BeautifulSoup(r.get('https://www.livecoinwatch.com/price/Bitcoin-BTC').text, "html.parser")

        coin_name = soup.find('h1', {'class':'coin-name'})
        coin_price = soup.find('span',{'class':'price'})
        coin_marketcap = soup.find('span',{'class':'price no-grow'})
        coin_24hChange = soup.find('div',{'class':'cion-item col-md-4 col-xl-3 px-1 py-1 py-md-0 text-left text-sm-center text-md-right'}).find('span').contents[0]
        print(coin_name.text)
        print("Current price is",coin_price.text)
        print("Market cap is",coin_marketcap.text)
        print("Current 24h change is",coin_24hChange + "%")
        print(" ")
        time.sleep(1)

        a = requests.Session()
        a.get('https://www.livecoinwatch.com/price/Ethereum-ETH')
        new_soup = bs4.BeautifulSoup(a.get('https://www.livecoinwatch.com/price/Ethereum-ETH').text,"html.parser")

        coin_name = new_soup.find('h1', {'class':'coin-name'})
        coin_price = new_soup.find('span',{'class':'price'})
        coin_marketcap = new_soup.find('span',{'class':'price no-grow'})
        coin_24hChange = new_soup.find('div',{'class':'cion-item col-md-4 col-xl-3 px-1 py-1 py-md-0 text-left text-sm-center text-md-right'}).find('span').contents[0]
        print(coin_name.text)
        print("Current price is",coin_price.text)
        print("Market cap is",coin_marketcap.text)
        print("Current 24h change is",coin_24hChange + "%")
        print(" ")
        time.sleep(1)


checkPrice()
