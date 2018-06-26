from lxml  import html
import requests
import csv
from unidecode import unidecode


def main():
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
    return unidecode(u,data)

if __name__ =="__main__":
    main()






















if __name__ =="__main__":
    main()
