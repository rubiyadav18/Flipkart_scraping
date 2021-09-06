
import requests,os,pprint
import json
from bs4 import BeautifulSoup
url="https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")
details={}

dict1={}
details3={}

mobile_name=soup.find("div",class_="_4rR01T").text[:5]
print(mobile_name)



img="https://reliancedigital.in/medias/Apple-iPhone12-Smartphone-Set4561-20?context=bWFzdGVyfGltYWdlc3wxNTA1N3xpbWFnZS9qcGVnfGltYWdlcy9oZWIvaGI4Lzk0MDc2Mjc0OTM0MDYuanBnfDRlNmUxNWEzYzk3NzIyNGM4OWUzMTI2ZTcxZGUwZWY0ZjlhOWU2MWM1ZDg5ZjZhNWMwZTg3YzExM2YzM2E3NDg"
img1=soup.find("img",class_="_396cs4 _2amPTt _3qGmMb  _3exPp9")
print(img1)



price=soup.find("div",class_="_30jeq3 _1_WHN1").text
print(price)


colour=soup.find("div",class_="_4rR01T").get_text()[12:-8]
print(colour)

model_number=soup.find("a",class_="_1fQZEK")['href']


r = requests.get("https://www.flipkart.com"+model_number)
s= BeautifulSoup(r.text,"html.parser")

m=s.find("div",class_="_1UhVsV _3AsE0T")


k=m.find_all("table",class_="_14cfVK")
for h in k:

    l=h.find_all("tr")
    
    for i in l:

        if "Model Number" in i.text:
            z=i.text.split('Model Number')

            z1=z[1]

            print(z[1])






# print(model_number)


details={"mobile_name":mobile_name}
details1={"price":price}
details2={"colour":colour}
details3={"img":img}
details4={"Model number":z1}

dict1.update(details)
dict1.update(details1)
dict1.update(details2)
dict1.update(details3)
dict1.update(details4)

print(dict1)
with open("flipcart.json","w") as f:
    json.dump(dict1,f,indent=4)













