# 從NB(路博邁)官網抓取境內(domestic)&境外(offshore)基金的每日淨值

import requests
from bs4 import BeautifulSoup
import pandas

def nav(header, mode):
    # 境內基金
    if mode == 1:
        url = 'https://www.nb.com/zh-tw/tw/products/site/prices-and-performance'
        currency = "T 累積級別(新台幣)"
        column = ['基金名稱', '類股', '淨值', '每日變動', '日漲跌幅', '淨值日期']
    # 境外基金
    if mode == 2:
        url = 'https://www.nb.com/zh-tw/tw/products/ucits-funds/prices-and-performance'
        currency = "T 累積類股(美元)"
        column = ['基金名稱', '類股', '淨值', '每日變動', '日漲跌幅', '成立日期', 'ISIN']
    
    source = requests.get(url, headers=header)
    # print(source.text)
    data = BeautifulSoup(source.text,'html.parser')
    # 每個row由4個tr組成 同一個row會有同樣的data-nbmi
    # 1.篩選出所有tr標籤中data-share-class="T累積級別(新台幣)" / "T累積類股(美元)" 的基金
    # 2.把這些基金的data-nbmi存進一個list
    # 3.用for-loop跑所有基金 以data-nbmi當條件 印出每種基金的T累積級別(新台幣)的名稱、類股、淨值日期、淨值、每日變動、日漲跌幅
    datas = data.find_all("tr")
    id = []
    for d in datas:
        # print(d)
        # # 網頁上看到的標籤裡的data-share-classes與實際上不同 <- 此table為動態產生的table 有些地方被屏蔽
        # # ex.(網頁)data-share-classes="T 累積類股(美元)" (print結果)data-share-classes="T 累積級別(美元)"
        # print(d.get("data-share-classes"))
        if d.get("data-share-classes") == currency:
            id.append(d.get("data-nbmi"))
    # for i in id:
    #     print(i)
    dlists = []
    for d in datas:
        # # 網頁上看到的標籤裡的class與實際上不同 <- 此table為動態產生的table 有些地方被屏蔽
        # # ex.(網頁)class="fund-name-row odd" (print結果)class=["fund-name-row", "hide"]
        # print(d.get("class"))
        for i in id:
            if d.get("data-nbmi") == i:
                # print(d.text)
                # 基金名稱
                if d.get("class")[0] == "fund-name-row":
                    # # d.text.strip(): 去掉d.text頭尾的指定字符(此處為"空白")
                    # print(d.text.strip())
                    dlist = []
                    dlist.append(d.text.strip())
                # 類股、淨值($)、每日變動($)、日漲跌幅(%)
                if d.get("class")[0] == "hide" and d.find("span"):
                    # print(d.text.strip())
                    td = d.findChildren("td", recursive=False)
                    for t in td:
                        # print(t.text.strip().strip("類股 :  "))
                        dlist.append(t.text.strip().strip("類股 :  "))
                # 淨值日期(境內only)
                if d.get("class")[0] == "as-of-date" and mode == 1:
                    # print(d.text.strip().strip("淨值日期: "))
                    dlist.append(d.text.strip().strip("淨值日期: "))
                    dlists.append(dlist)
                # 成立日期(境外only)
                if d.get("class")[0] == "hide" and not(d.find("span")) and mode == 2:
                    # print(d.text.strip().strip("成立日期 : "))
                    dlist.append(d.text.strip().strip("成立日期 : "))
                # ISIN(境外only)
                if d.get("class")[0] == "isin" and mode == 2:
                    # print(d.text.strip().strip("ISIN: : "))
                    dlist.append(d.text.strip().strip("ISIN: "))
                    dlists.append(dlist)
    # for d in dlists:
    #     print(d)

    # 將dlists轉成datafram
    dfform = pandas.DataFrame(dlists, columns=column)
    with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
        print(dfform)

    return dfform

header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Host': 'www.nb.com',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'text/html; charset=utf-8',
    'cookie':'ASP.NET_SessionId=mo02f02tb1tue4m1zedpw3tq; SC_ANALYTICS_GLOBAL_COOKIE=875d6e41b05246749eabe089ef097676|False; DCID=0; Login=unknown; AMCVS_E9B80FC0539AE5990A490D45%40AdobeOrg=1; AMCV_E9B80FC0539AE5990A490D45%40AdobeOrg=-1124106680%7CMCIDTS%7C18718%7CMCMID%7C12691045439929672971691969589756508388%7CMCAAMLH-1617777556%7C11%7CMCAAMB-1617777556%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1617179956s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; s_cc=true; www.nb.com=audience={15378176-F28A-4A5F-B94A-A88329A1AAFC}; lang=zh-TW; s_pvpg=Prices%20and%20Performance; s_sq=%5B%5BB%5D%5D; gpv_pn=Prices%20and%20Performance; dslv=1617179044479; dslv_s=Less%20than%201%20day'
}
nav(header, 1)
nav(header, 2)