from bs4 import BeautifulSoup
import re

with open("D:\\python\\beautifulsoup\\doc.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    #print(soup.head.title)
    #print(soup.body.a.text)
    #print(soup.body.p.b)
    #print(soup.find("a"))
    #print(soup.find_all("a",class_="element"))
    #print(soup.find_all("a",class_="avatar"))
    #print(soup.find("a", href=True)["href"])
    #for tag in soup.find_all(re.compile("^b")):
    #    print(tag)
    #print(soup.get_text)
    print(soup.get_text())    
