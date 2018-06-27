#import libraries
import urllib2
import json
from bs4 import BeautifulSoup

# Specify working ulr


def listEstates(estateList):
    for h in estateList:
        print(h)

def findEstates(boxes):
    houses = []
    for counter, box in enumerate(boxes):
        container_box  = box.findAll('div' , attrs={'class', 'fs-estate-cube-info-line'})
        downer = BeautifulSoup(container_box, 'html.parser')
        price_box_question = downer.find('span', attrs={'class', 'fs-estate-cube-info-question'});   
        #price_box_answer = downer.find('span', attrs={'class', 'fs-estate-cube-info-answer'});   


        
        #address = house.text

        #stringdata = "Price"+":"+ price +","+ "Address"+":" + house +"}"
        
        
        
        houses.append("Question:", price_box_question, "Answer:", price_box_answer )
        
    return houses


def main():
    quote_page = 'https://www.mbl.is/fasteignir/'

    # query webpage
    ## Get page

    page = urllib2.urlopen(quote_page)

    #parse page 

    soup = BeautifulSoup(page, 'html.parser')

    #openBoxes = soup.find_all('div', attrs={'class': 'fs-openhouse-cube'})

    closedBoxes = soup.find_all('div', attrs={'class': 'fs-estate-cube'})

    #scraped1 =findEstates(openBoxes)
    scraped2 = findEstates(closedBoxes)
    
    #listEstates(scraped1)
    listEstates(scraped2)




if __name__ =="__main__":
    main()







##stripper = houses.text.strip()

##print (stripper)

