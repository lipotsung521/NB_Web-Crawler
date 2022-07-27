# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 14:11:25 2021

@author: panda
"""
# TODO：import all modules
import db
import nb_website
import fund

# TODO：connect DB
db.constructor_article()
#nb_website.show_article_df()
article_df = nb_website.return_article_df()


#%%
db.insert_article(article_df)

networthin_df = fund.return_networthin_df()
db.insert_networthin(networthin_df)

networthoff_df = fund.return_networthoff_df()
db.insert_networthoff(networthoff_df)



#%%
# Part 1 ： 基金圖卡

# TODO：爬每日淨值(呼叫function，return DataFrame)

# TODO：將本日淨值insert到DB

# TODO：

    
