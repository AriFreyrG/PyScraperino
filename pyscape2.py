from lxml  import html
import requests


def main():
    page = requests.get('https://www.mbl.is/fasteignir/')
    tree = html.fromstring(page.content)
    openhouse = tree.xpath('//div[@class="fs-openhouse-cube"]')
    houses = []
    for house in openhouse:
        openhouseval = house.xpath('div[@class="openhouse"]/text()')
        addressval = house.xpath('//div[@class="fs-openhouse-address"]/text()')
        verdval = house.xpath('//strong[@class="fs-openhouse-cube-info-answer"]/text()')

        
        print  "Openhouse", str(openhouseval).strip(" "), "\n"
        print "Address",  str(addressval).strip(" "), "\n"
        print "Verð",  str(verdval).strip(" ") , "\n"
    




if __name__ =="__main__":
    main()






















if __name__ =="__main__":
    main()
