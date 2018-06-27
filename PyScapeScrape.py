from lxml  import html
import requests
import csv
from unidecode import unidecode
import urllib2
import json

def main():
    url1 = 'https://www.mbl.is/fasteignir/leit/?q=80f323c5382397611e72800316f250d1'
    url2 = 'https://www.mbl.is/fasteignir/leit/?page=2&q=9e2d9c3b99e4349d300c226db2e36ab8'
    url3 = 'https://www.mbl.is/fasteignir/leit/?page=3&q=9e2d9c3b99e4349d300c226db2e36ab8'
    SearchWars(url1)
    SearchWars(url2)
    SearchWars(url3)


def SearchWars(urlboi):
    page = requests.get(urlboi)
    tree = html.fromstring(page.content)
    openhouse = tree.xpath('//div[@class="single-realestate openhouse "]')
    houses = []
    housesCleaned = []
    for house in openhouse:
        address = house.xpath('.//div[@class="realestate-info"]/div[@class="realestate-head"]/a/h4//text()')
        properties = house.xpath('.//div[@class="realestate-info"]/div[@class="realestate-properties"]/span/strong/text()')
        href = house.xpath('.//div[@class="realestate-info"]/div[@class="realestate-head"]/a/@href')
               
        
    
        urlstring = "https://www.mbl.is" + href[0]

        address = address[0].encode('utf-8')
        price = properties[0].encode('utf-8')
        size = properties[1].encode('utf-8')
        urlstring = ''.join(urlstring)
        
        
        megastring = ''.join(replaceSvigar(str(address))), str(fixpricestring(price)), str(size),urlstring 
       
        houses.append(megastring)

    printToExcel(houses)

def printToExcel(houses):
    with open('houses.csv', 'a+') as f:
            writer = csv.writer(f, delimiter=';')
           
            writer.writerows(houses)   


def replaceSvigar(takethem):
    return ''.join(takethem).replace(',','')

def graveyard():
   
    return 1

def getVal(junk):
    try:
        unicode(junk, "ascii")
    except UnicodeError:
        junk = unicode(junk, "utf-8")
    else:
        # value was valid ASCII data
        pass

        
def fixpricestring(rawprice):
    return rawprice.replace('kr.', '').replace(' ','').replace('\n','').replace('.','').replace('m','').replace('"', '').replace(';', '; ')



def replacer(data):
    return str(data)

if __name__ =="__main__":
    main()
   




















