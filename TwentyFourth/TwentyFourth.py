from bs4 import BeautifulSoup
import requests
import re

keyboardsList = list()
res = requests.get("https://exo.ir/category/%DA%A9%DB%8C%D8%A8%D9%88%D8%B1%D8%AF-%DA%AF%DB%8C%D9%85%DB%8C%D9%86%DA%AF?sort=p.price&order=ASC&fq=1&limit=100")
soup = BeautifulSoup(res.text, "html.parser")
values = soup.find_all("div",{"class":"caption"})
for value in values:
    newValue = re.sub(r"\n"," ",value.text)
    brand = re.findall(r"تولیدکننده: (\w*-*\w+)",newValue)
    model = re.findall(r"کد محصول: (.+?(?=[کیبورد پد]))",newValue)
    price = re.findall(r"\d+,\d+,*\d+",newValue)
    keyboardsList.append({"brand": brand,"model":model,"price":price})
for i in range(0,len(keyboardsList)):
    print(keyboardsList[i])
