def thegraveyard():
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
     #for house in houses:
            #    writer.writerow(house)
             #jason = json.dumps(megastring)
        #print jason
                #combostring = "Address;", replacer(str(address)), "Verð;", replacer(str(priceval)), "Stærð;", replacer(str(sizeval))
        #print replacer(address[0])


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
