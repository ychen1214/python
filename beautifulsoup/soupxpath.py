#import requests

from bs4 import BeautifulSoup
import os
from lxml import etree

directory = "beautifulsoup\html"
for filename in os.listdir(directory):
    if filename.endswith(".html"): 
        #print(os.path.join(directory, filename))
        with open((os.path.join(directory, filename)),"r", encoding="utf8") as fp: 
            soup = BeautifulSoup(fp, "html.parser")   
            dom = etree.HTML(str(soup))
            print(dom.xpath('//*[@id="a-autoid-1-announce"]/span[1]'))
            
            #print(soup.find_all("div",id="merchant-info"))
            #print(soup.find("span",id="productTitle").text) #Title
            #print(soup.find("div",id="tmmSwatches"))
            #print(soup.find_all("span",{"class":"a-size-base a-color-secondary"}))
            #t = (soup.find("div",id="tmmSwatches"))    
            #for i in t.find_all('ul',{"class":"a-unordered-list a-nostyle a-button-list a-horizontal"}):
                # for x in i.find_all("span",{"class":"a-size-base a-color-price a-color-price"}):                    
                #     print(x.text)        
                # for x in i.find_all("span",{"class":"a-size-base a-color-secondary"}):                    
                #     print(x.text)     
                # for x in i.find_all("span",{"class":"audible_mm_price"}):                    
                #     print(x.text)
                #for x in i.find_all("span",{"class":"a-button a-spacing-mini a-button-toggle format"}):                    
            #for j in t.find_all('a[href'):                    
            #    print(j.text)                         
            #print(soup.find_all("span", attrs={'class':"a-button a-button-selected a-spacing-mini a-button-toggle format"}))
            #print(soup.find_all("span", attrs={'class':"a-button a-spacing-mini a-button-toggle format"}))
            print(soup.find_all("a", attrs={'class':"title-text"}))
                # for x in i.find_all("span",{"class":"a-button-inner"}):
                #     for j in x.find_all("a", href=True):
                #         print(j)

            #print(soup.find_all("a",id="sellerProfileTriggerId"))    
            #print(os.path.join(directory, filename))
            #print(soup.find_all(["a","data-is-ubb","class"],id="sellerProfileTriggerId"))
            #print(soup.find('div', {'id': 'shipsFromSoldByInsideBuyBox_feature_div'}))#.find('div',  {'class':"a-section a-spacing-none"}).find('span'))
            #print(soup.select("div.celwidget > div > span"))
            
    else:
        continue

""" 
with open(("D:\\python\\beautifulsoup\\html\\17666368_20211020_00454335.html"),"r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    #print(soup.head.title)
    #print(soup.body.a.text)
    #print(soup.body.p.b)
    #print(soup.find("a"))
    #print(soup.find_all("a"))
    #print(soup.find_all("a",class_="element"))
    #print(soup.find_all("a",class_="avatar"))
    print(soup.find_all("div",id="merchant-info"))
    print(soup.find_all("div",id="sfsb_accordion_head"))
    print(soup.find_all("a",id="sellerProfileTriggerId"))
    #print(soup.find("a", href=True)["href"])
    #for tag in soup.find_all(re.compile("^b")):
    #    print(tag)
    #print(soup.get_text)
    #print(soup.get_text())    
 """
