from bs4 import BeautifulSoup
import os
import codecs

directory = "beautifulsoup\html"
for filename in os.listdir(directory):
    if filename.endswith(".html"): 
        #print(os.path.join(directory, filename))
        with codecs.open((os.path.join(directory, filename)),"r", encoding="utf8") as fp: 
            soup = BeautifulSoup(fp, "html.parser") 
            #print(soup.select("#tmmSwatches > ul > li:nth-of-type(1) > span"))
            price = soup.select("#priceblock_saleprice")
            print(price)
            #print(dom.xpath('//*[@id="a-autoid-1-announce"]/span[1]'))
            #//*[@id="tmmSwatches"]/ul/li[1]