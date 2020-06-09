import requests
import bs4

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip()


price = getEbayPrice('https://www.ebay.com/itm/FunTime-8oz-Premium-Black-Popcorn-Popper-Machine-Maker-Cart-Vintage-FT860CB/172241474323?_trkparms=%26rpp_cid%3D5e84bc5e9b7fa809a7c89787%26rpp_icid%3D5e84bc5e9b7fa809a7c89786&_trkparms=pageci%3Ab75a4ddb-a939-11ea-86d1-74dbd18085c5%7Cparentrq%3A92035fe11720a9c42de7797dfffcb70a%7Ciid%3A1')
print('The price is ' + price)


