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
               
        
        #combostring = "Address;", replacer(str(address)), "Verð;", replacer(str(priceval)), "Stærð;", replacer(str(sizeval))
        #print replacer(address[0])
        urlstring = "https://www.mbl.is" + href[0]

        address = address[0].encode('utf-8')
        price = properties[0].encode('utf-8')
        size = properties[1].encode('utf-8')
        urlstring = ''.join(urlstring)
        
        
        megastring = ''.join(replaceSvigar(str(address))), str(fixpricestring(price)), str(size),urlstring 
        #jason = json.dumps(megastring)
        #print jason
        houses.append(megastring)

    printToExcel(houses)

def printToExcel(houses):
    with open('houses.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';')
            #for house in houses:
            #    writer.writerow(house)
            writer.writerows(houses)   


def replaceSvigar(takethem):
    return ''.join(takethem).replace(',','')

def graveyard():
    #megastring = [address.encode('utf-8'), 'Price;',fixpricestring(properties[0]).encode('utf-8'), 'Url;',urlstring.encode('utf-8')]
    #for h in houses:
    #    place = ""
    #    place = h[0].decode('utf-8').replace(',','')
    #    price = ""
    #    price = fixpricestring(properties[0])
    #    linkz = ""
    #    linkz = urlstring
    #    freshprince =  place.encode('utf-8') , price.encode('utf-8') , linkz.encode('utf-8')
    #    #fresherprince = freshprince.encode("utf-8")
    #    print freshprince
    #    housesCleaned.append(freshprince)
        
    #csv.register_dialect('unixpwd', delimiter=';', quoting=csv.QUOTE_NONE)
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

def abstractor():
    page = requests.get('https://www.mbl.is/fasteignir/')
    tree = html.fromstring(page.content)
    openhouse = tree.xpath('//div[@class="fs-estate-cube"]')
    houses = []
    for house in openhouse:
        address = house.xpath('div[@class="fs-estate-cube-headline"]/a[@class="fs-white-link"]/span/strong/text()')
        priceval = house.xpath('div[@class="fs-estate-cube-info"]/div[@class="fs-estate-cube-info-line"]/div[@class="pull-left"]/strong[@class="fs-estate-cube-info-answer"]/text()')
        sizeval = house.xpath('div[@class="fs-estate-cube-info"]/div[@class="fs-estate-cube-info-line"]/div[@class="pull-right"]/strong[@class="fs-estate-cube-info-answer"]/text()')
        #verdval = house.xpath('//strong[@class="fs-openhouse-cube-info-answer"]/text()')

        
        
        combostring = "Address;", replacer(str(address)), "Verð;", replacer(str(priceval)), "Stærð;", replacer(str(sizeval))
        print  combostring
        houses.append(combostring);
        #print "Verð",  str(verdval).strip(" ") , "\n"

        with open('houses.csv', 'wb') as f:
            writer = csv.writer(f, delimiter=';')
            
            #writer = csv.write(csvfile)
            writer.writerows(houses)


def replacer(data):
    return str(data)

if __name__ =="__main__":
    main()
   




















