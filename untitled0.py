# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:18:34 2022

@author: user
"""

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("https://cnn.com")