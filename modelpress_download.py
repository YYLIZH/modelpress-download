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
    local = os.path.join('D:\\modelpress\\'+title+'\\%s.jpg' % x)  #檔案儲存位置
    x+=1
    urlretrieve(websiteURL,local)
    print('第',x-1,'張下載完成!')

try:
    banner_x=0
    for picture in soup.find_all(class_="l-appImageList"):
        appImageList = picture.find(class_="m-appImageList")
        for imgURL in appImageList.find_all(class_="outputthumb"):
            websiteURL=imgURL.get('src')
            place = websiteURL.index('.jpg')
            websiteURL = websiteURL[0:place+4]
            local = os.path.join('D:\\modelpress\\'+title+'\\banner%s.jpg' % banner_x)  #檔案儲存位置
            banner_x+=1
            urlretrieve(websiteURL,local)
            print('第',banner_x-1,'張下載完成!')
except:
    print('No Banner!')