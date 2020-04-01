import requests
from bs4 import BeautifulSoup
from IPython.display import Image,display
from urllib.request import urlretrieve
import os

website = 'https://mdpr.jp/news/detail/2018375'

res = requests.get(website)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')

title=soup.find('title')
title=str(title)
title=title[7:-17]


path='D:\\modelpress\\'+title
os.mkdir(path)


print(path)

x=0
for picture in soup.find_all(class_="figure"):
    websiteURL=picture.find("img").get("src")
    place = websiteURL.index('.jpg')
    websiteURL = websiteURL[0:place+4]
    local = os.path.join('D:\\modelpress\\'+title+'\\%s.jpg' % x)  #�ɮ��x�s��m
    x+=1
    urlretrieve(websiteURL,local)
    print('��',x-1,'�i�U������!')

try:
    banner_x=0
    for picture in soup.find_all(class_="l-appImageList"):
        appImageList = picture.find(class_="m-appImageList")
        for imgURL in appImageList.find_all(class_="outputthumb"):
            websiteURL=imgURL.get('src')
            place = websiteURL.index('.jpg')
            websiteURL = websiteURL[0:place+4]
            local = os.path.join('D:\\modelpress\\'+title+'\\banner%s.jpg' % banner_x)  #�ɮ��x�s��m
            banner_x+=1
            urlretrieve(websiteURL,local)
            print('��',banner_x-1,'�i�U������!')
except:
    print('No Banner!')