# 從db抓資料 用matplotlib畫歷史淨值圖

# 在要執行的code前面打#%% -> 按run cell -> 以cell為單位執行程式(像jupyter notebook一樣)
# plt.show()

# 用pyplot畫歷史淨值圖
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
import matplotlib.ticker as ticker
from pandas import DataFrame

def plot(df):
    # 日期反轉
    data_reverse = df.iloc[::-1]
    fig, ax=plt.subplots()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # 設定x軸主刻度顯示格式（日期）
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=5))
    plt.plot(pd.to_datetime(data_reverse['日期']),data_reverse['淨值'],color='#123a5f' )

    # 將畫好的歷史淨值圖存到此code所在的資料夾
    plt.savefig('plot1.png')

    return 'plot1.png'
