# 將matplotlib產生的圖上傳到imgur 並取得圖片網址
# https://ithelp.ithome.com.tw/articles/10241006

# 在要執行的code前面打#%% -> 按run cell -> 以cell為單位執行程式(像jupyter notebook一樣)
# plt.show()

# 用pyplot畫歷史淨值圖
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
import matplotlib.ticker as ticker

df = pd.read_csv('5gfund.csv')
data_reverse = df.iloc[::-1] #日期反轉
fig, ax=plt.subplots()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))  #設定x軸主刻度顯示格式（日期）
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=5))
plt.plot(pd.to_datetime(data_reverse['日期']),data_reverse['淨值'],color='#123a5f' )


# (1) 將歷史淨值圖上傳 imgur 圖床
# (2) 壓縮投資觀點圖片(<1mb, ashx檔)後再上傳 imgur 圖床 <- https://blog.csdn.net/weixin_41010198/article/details/106544789
# https://github.com/Imgur/imgurpython
# https://github.com/Imgur/imgurpython/tree/master/examples
from imgurpython import ImgurClient

# # 連線到 imgur 圖床 + 測試連線成功與否
# client_id = 'fd12f4e36a8300a'
# client_secret = '6ca48f9294ca9d9fc74de0a31cffadc0c1188863'
# client = ImgurClient(client_id, client_secret)
# # 輸出近期上傳至 imgur 圖床的url
# items = client.gallery()
# for item in items:
#     print(item.link)


# TODO:接DB
# TODO:存DB query 圖片網址

"""
from PIL import Image

r = requests.get(image_links[0])
with open('test.jpg','wb') as f:
    f.write(r.content)
im = Image.open('test.jpg')
im = im.convert('RGB')
im.save('test.jpg')


"""







# 用imgurpython上傳圖片
from upload import upload_img
from auth import authenticate
# 相簿id <- https://ithelp.ithome.com.tw/articles/10241006
album = "pVOzoNI"
# A Filepath to an image on your computer"
image1_path = "test1.jpg"
client = authenticate()
image1 = upload_img(client, image1_path, album)
print("Image was posted!")
# print(f"You can find it here: {image1['link']}")
print("You can find it here: {0}".format(image1['link']))



# 用pyimgur上傳圖片
# 優：只需要CLIENT_ID，就可以上傳圖片、取得圖床連結，操作較imgurpython簡單
# 缺：傳送的結果不會出現在 Imgur 的 Images 裡面，也不會出現在相簿裡
import pyimgur

client_id = "fd12f4e36a8300a"
# A Filepath to an image on your computer"
image2_path = "test2.png"
im = pyimgur.Imgur(client_id)
# # 測試能否讀取圖床圖片
# image = im.get_image('f1WHMuW')
# print(image.title) 
# print(image.link)
image2 = im.upload_image(image2_path, title='pyimgur_test')
print(image2.title) 
print(image2.link)
print(image2.type)