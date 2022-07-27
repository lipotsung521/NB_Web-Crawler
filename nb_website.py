import pandas as pd
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
           'Host': 'www.nb.com',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Language': 'zh-TW,zh;q=0.9',
           'Accept-Encoding': 'gzip, deflate, br',
           'Content-Type': 'text/html',
           'cookie':'ASP.NET_SessionId=cx1tnsotlll3t4dim15ltq4y; DCID=0; Login=unknown; AMCV_E9B80FC0539AE5990A490D45%40AdobeOrg=793872103%7CMCIDTS%7C18700%7CMCMID%7C07113774344859212670987415684326193470%7CMCAAMLH-1616223356%7C11%7CMCAAMB-1616223356%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCAID%7CNONE; dslv_s=More%20than%207%20days; s_cc=true; NBHomePage=N; www.nb.com=audience={15378176-F28A-4A5F-B94A-A88329A1AAFC}; lang=zh-TW; _sdsat_1_S_Audience=retail; s_sq=%5B%5BB%5D%5D; s_pvpg=Recoveries%20Are%20Rarely%20Straight%20Lines; gpv_pn=Recoveries%20Are%20Rarely%20Straight%20Lines; mbox=PC#1615002431062-642481.38_0#1616835425|session#1615618553509-160945#1615627685|check#true#1615625885; dslv=1615625824522; SC_ANALYTICS_GLOBAL_COOKIE=e74853aa61914d998f43c45a8fcdfd59|True' }
res = requests.get('https://www.nb.com/zh-tw/tw/insights/',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
#--------------------------------------------------------------------------------
category_tag = soup.findAll("div", class_ ="category-title")#類別
category = [i.get_text() for i in category_tag]
#--------------------------------------------------------------------------------
title_tag  = soup.findAll('h6')#標題
title = [i.get_text() for i in title_tag]
#--------------------------------------------------------------------------------
date_tag =soup.findAll("div",class_="publish-date")#日期
date = [i.get_text() for i in date_tag]
#--------------------------------------------------------------------------------  
website_tag = soup.select(".insights-copy-container")#網址
website_tags = soup.findAll("div",class_ ="insights-copy-container")
website_links = []
for website_tag in website_tags:
    website_links.append('http://nb.com'+website_tag.select_one("a").get("href"))#需增加nb.com
#--------------------------------------------------------------------------------
results = soup.findAll("img")#圖片
image_links = [i.get("src") for i in results]
for i in range(2):
    image_links.pop()
del image_links[0]
for i in range(len(image_links)):
    image_links[i] = 'http://nb.com'+image_links[i]
#--------------------------------------------------------------------------------    
describe_tag = soup.findAll("div",class_ ="insights-copy-container")#描述
describe = [i.contents[-1].strip() for i in describe_tag]
#--------------------------------------------------------------------------------    
df =pd.DataFrame([category,title,date,image_links,website_links,describe]).transpose()#產生dataframe
df.columns = ['category','title','date','mage_links','website_links','describe']

def show_article_df():
    print(df)
def return_article_df():
    return df


#%%



