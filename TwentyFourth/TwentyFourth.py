from bs4 import BeautifulSoup
import requests
import re

res = requests.get("https://exo.ir/category/%DA%A9%DB%8C%D8%A8%D9%88%D8%B1%D8%AF-%DA%AF%DB%8C%D9%85%DB%8C%D9%86%DA%AF?sort=p.price&order=ASC&fq=1")
soup = BeautifulSoup(res.text, "html.parser")
values = soup.find_all("div",{"class":"caption"})
for value in values: 
    print(value.text)






















#for i in range(4,len(value)):
#   print(value[i].text)
#for i in range(4,len(value2)):
#    print(value2[i].text)