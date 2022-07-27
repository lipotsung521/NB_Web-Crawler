# 上傳圖片(歷史淨值圖、投資觀點圖片)到 imgur 圖床
# https://ithelp.ithome.com.tw/articles/10241006

# 用pyimgur上傳存在主機內的圖片
# 優：只需要CLIENT_ID就可以上傳圖片、取得圖床連結，操作較imgurpython簡單
# 缺：傳送的結果不會出現在 Imgur 的 Images 裡面，也不會出現在相簿裡
import pyimgur

# path：圖片在本機的檔案路徑
# 若跟code在同一資料夾，則path = "圖片檔名"(ex. image_path = "test2.png")
def upload(path):
    # 從 auth.ini 取 client id
    import configparser
    config = configparser.ConfigParser()
    config.read('auth.ini')
    client_id = config.get('credentials', 'client_id')
    im = pyimgur.Imgur(client_id)
    # # 測試能否讀取圖床圖片
    # image = im.get_image('f1WHMuW')
    # print(image.title)
    # print(image.link)
    # print(image.size)
    # print(image.type)
    # !!無法指定相簿!!
    image = im.upload_image(path, title='pyimgur_test')
    # print(image.link)

    return image.link










# return 全部投資觀點圖片的連結 + 投資觀點title (dataframe)
# 傳入的參數：投資觀點table
import requests
from PIL import Image
from pandas import DataFrame
from upload import upload
from plot import plot

def articleImg_all(table):
    # table(category, title, date, image_links, website_links, describe, FiveG, ESG, CIO)
    # 所有投資觀點的title跟對應的url(dataframe)
    df = DataFrame([ [j['title'], j['image_links']] for j in table ], columns=['title', 'imgur_links']) # list comprehensions
    # 先從網址下載投資觀點圖片 -> 再壓縮投資觀點圖片
    # https://yungyuc.github.io/oldtech/python/python_imaging.html
    for i in range(len(df.index)):
        img = requests.get(df.iloc[i]['imgur_links'])
        # 前提：code所在的資料夾裡要先有一個"article1.jpg"
        with open("article1.jpg", "wb") as f:
            f.write(img.content)
        im = Image.open("article1.jpg")
        # png是4通道(RGBA)(A(alpha):透明度)，jpg是3通道(RGB) -> 將png轉換成3通道在保存成jpg
        im = im.convert("RGB")
        im.save("article1.jpg")
        df.iloc[i]['imgur_links'] = upload("article1.jpg")
    
    return df




# return 一個投資觀點圖片的連結(只回傳新增的投資觀點圖片的連結) + 投資觀點title (dataframe)
# 傳入的參數：新增的投資觀點相關資料(一次一篇)
# 同1.




# return 全部基金淨值圖圖片的連結 + 淨值日期(最新日期) + 基金名稱 (dataframe)
# 傳入的參數：基金淨值table
# 境外基金沒有淨值日期 -> 目前先用爬蟲程式執行的日期代替(尚未實作)
def nav_img(table):
    # table(基金名稱、日期、淨值)
    # name: 存所有基金名稱的list
    name = list(set([i['基金名稱'] for i in table]))    # list comprehensions
    imgurlist = []
    for i in range(len(name)):
        # 一個基金一個df
        df = DataFrame([ [j['日期'], j['淨值']] for j in table if j['基金名稱']==name[i] ], columns=['日期', '淨值'])        
        # 畫此基金的歷史淨值圖 -> 回傳該圖在本機的路徑
        path = plot(df)
        # 用path上傳歷史淨值圖到imgur -> 回傳url
        url = upload(path)
        imgurlist.append([name[i], max(df['日期']), url])
    imgurdf = DataFrame(imgurlist, columns=['name', 'date', 'img_url'])
    
    return imgurdf
