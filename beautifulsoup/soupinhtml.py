import requests
import time
import csv 
from bs4 import BeautifulSoup
import re
import os

directory = "D:\\python\\beautifulsoup\\html"
for filename in os.listdir(directory):
    if filename.endswith(".html"): 
        #print(os.path.join(directory, filename))
        with open((os.path.join(directory, filename)),"r", encoding="utf8") as fp: 
            soup = BeautifulSoup(fp, "html.parser")   
            print(soup.find_all("div",id="merchant-info"))
            #print(soup.find_all("div",id="sfsb_accordion_head"))
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
