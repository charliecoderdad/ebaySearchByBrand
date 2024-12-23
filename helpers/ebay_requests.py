import logging
from bs4 import BeautifulSoup
import requests
import urllib, re

def extractPriceFromText(text):
  match = re.search(r"\$?(\d{1,3}(,\d{3})*(\.\d+)?)", text)
  if match:
    return float(match.group(1).replace(',', ''))
  return 0

def getAverageSoldPrice(url, numSold):
  logging.debug("average sold price URL recieved: " + url)
  if (numSold > 60):
    numSold = 60
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    divs = soup.find_all('li', class_="s-item", id=lambda x: x is not None and x.strip() != "")
    prices_sum = 0
    prices_count = 0    
    for i in range(0, numSold):
      price = divs[i].find('span', class_="s-item__price")
      shipping = divs[i].find('span', class_="s-item__shipping")
      logging.debug("-----> price (" + str(i) + "): " + str(price.text))
      if (" to " not in price.text):
        prices_count += 1
        price = extractPriceFromText(price.text)
        if (shipping is not None):
          shipping = extractPriceFromText(shipping.text)
        else:
          shipping = 0
        # logging.debug("-----> price: " + str(price))
        logging.debug("-----> shipping: " + str(shipping))
        logging.debug("")
        prices_sum += price + shipping
    logging.debug("prices_sum: " + str(prices_sum))
    logging.debug("prices_count: " + str(prices_count))
  if (prices_count != 0):
    return prices_sum / prices_count
  else:
    return 0

def getListingsAmountFromUrl(url):
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    amount = soup.find('h1', class_='srp-controls__count-heading').find('span')
    amount = int(amount.text.replace(",", ""))
    return amount
  else:
    logging.error("Failed to retrieve amount of listings: " + url)
