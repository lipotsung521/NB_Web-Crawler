import requests
import json
from bs4 import BeautifulSoup
import db



header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Host': 'www.nb.com',
    'Accept':'*/*',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie':'ASP.NET_SessionId=mo02f02tb1tue4m1zedpw3tq; SC_ANALYTICS_GLOBAL_COOKIE=875d6e41b05246749eabe089ef097676|False; DCID=0; Login=unknown; AMCVS_E9B80FC0539AE5990A490D45%40AdobeOrg=1; s_cc=true; www.nb.com=audience={15378176-F28A-4A5F-B94A-A88329A1AAFC}; lang=zh-TW; dslv_s=Less%20than%201%20day; s_sq=%5B%5BB%5D%5D; AMCV_E9B80FC0539AE5990A490D45%40AdobeOrg=793872103%7CMCIDTS%7C18718%7CMCMID%7C12691045439929672971691969589756508388%7CMCAAMLH-1617784823%7C11%7CMCAAMB-1617784823%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1617179963.4%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; _sdsat_1_S_Audience=; mbox=check#true#1617180135|session#1617180024408-757709#1617181935|PC#1617180024408-757709.38_0#1618389675; s_pvpg=insights; gpv_pn=insights; dslv=1617180376948'
}



def tag():
    
    # ESG
    
    # 每次在文章篩選器中增減篩選條件 就會產生新的filterresults(在network中的xhr的headers) -> filterresults在network中的xhr中的response
    # requests.post("request url", data="form data", headers=header)
    r = requests.post("https://www.nb.com/api/Sitecore/Article/FilterResults", data="filtertwo%5B%5D=3c2db9fe-e346-4f71-a4fa-17b9e65c29b7&keywords=&language=zh-TW&sortOrder=new", headers=header)
    # r.text是utf編碼形式(我們要的是html)
    payload = json.loads(r.text)
    bs = BeautifulSoup(payload['filteredResults'],'html')
    article_list = bs.findAll('h6')
    
    # TODO: 連DB Query
    
    # 5G 
    
    # TODO:連DB Query
    
    
    
    
    

