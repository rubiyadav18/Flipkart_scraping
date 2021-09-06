
import requests,os,pprint
import json
from bs4 import BeautifulSoup

url="https://www.flipkart.com/apple-iphone-12-white-128-gb/p/itm95393f4c6cc59?pid=MOBFWBYZBTZFGJF9&lid=LSTMOBFWBYZBTZFGJF9K5AZO1&marketplace=FLIPKART&q=apple+phone&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=37010cc3-f115-4470-97d2-5d0808f2456d.MOBFWBYZBTZFGJF9.SEARCH&ppt=sp&ppn=sp&ssid=cjnpodrvsg0000001630575702140&qH=900bc469862f62c0"
r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")

# print(soup)
dict1={}
dict6={}

# img=soup.find("div",class_="jEaykx")
# print(img)

company_name=soup.find("span",class_="B_NuCI").text[:5]
print(company_name)

model_name=soup.find("div",class_="")

colour=soup.find("span",class_="B_NuCI").text[17:-9]
print(colour)

price=soup.find("div",class_="_30jeq3 _16Jk6d").text
print(price)

ram=soup.find("span",class_="B_NuCI").text[23:]
print(ram)

rating=soup.find("div",class_="_3LWZlK").text
print(rating)

display=soup.find("div",class_="_1AtVbE col-12-12")
print(display)



cemra=soup.find("div",class_="_2a78PX").text
print(cemra)


storage=soup.find("div",class_="_1rcQuH")
print(storage)

display=soup.find_all("table",class_="_14cfVK")
for i in display:
    a=i.find_all('td')
    for j in a:
        print(j.text)

# print(display)




dict1={"company_name":company_name}
dict2={"colour":colour}
dict3={"price":price}
dict4={"ram":ram}
dict5={"rating":rating}
dict7={"cemra":cemra}

dict6.update(dict1)
dict6.update(dict2)
dict6.update(dict3)
dict6.update(dict4)
dict6.update(dict5)
dict6.update(dict7)


file1=open("amazone.json","w")
data=json.dump(dict6,file1,indent=5)





# "genral"
# "bank_offers
# storage
# size
# camera
# battery"