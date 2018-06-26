from lxml  import html
import requests
import csv
from unidecode import unidecode
import urllib2


def main():
    page = requests.get('https://www.mbl.is/fasteignir/leit/?q=80f323c5382397611e72800316f250d1')
    tree = html.fromstring(page.content)
    openhouse = tree.xpath('//div[@class="single-realestate openhouse "]')
    houses = []
    for house in openhouse:
        address = house.xpath('.//div[@class="realestate-info"]/div[@class="realestate-head"]/a/h4//text()')
        properties = house.xpath('.//div[@class="realestate-info"]/div[@class="realestate-properties"]/span/strong/text()')
        href = house.xpath('.//div[@class="realestate-info"]/div[@class="realestate-head"]/a/@href')
               
        
        #combostring = "Address;", replacer(str(address)), "Verð;", replacer(str(priceval)), "Stærð;", replacer(str(sizeval))
        #print replacer(address[0])
        urlstring = "https://www.mbl.is" + href[0]
        address[0].encode('utf8', 'ignore')
        megastring = stripNonAlphaNum(stripTags(address[0]).lower()), ";",fixpricestring(properties[0]),";",properties[1], ";", urlstring
            
        print megastring
        houses.append(megastring)
        with open('houses.csv', 'wb') as f:
            writer = csv.writer(f, delimiter=';')
            
            #writer = csv.write(csvfile)
            writer.writerows(houses)



def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)
        
def fixpricestring(rawprice):
    return rawprice.replace('kr.', '').replace(' ','').replace('\n','').replace('.','').replace('m','')

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






















if __name__ =="__main__":
    main()
