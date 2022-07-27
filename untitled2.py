# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:21:32 2022

@author: user
"""

import re
ptn = re.compile('[a-zA-Z]+')
print(ptn.findall('jfoais1234uh331u1'))

print(re.search('(?<![@])+[0-9]+','823891@nctu.edu.tw'))
print(re.search('(?<![@])+[0-9]+','xxx@nctu.edu.tw'))

print(re.search('(?<=[@])+[0-9]+','xxx@163.com'))
print(re.search('(?<=[@])+[0-9]+','xxx@nctu.edu.tw'))


def check(m):
    pattern = "^(?=.*\d{4,20})(?=.*[a-z]{4,20})(?=.*[A-Z]{4,20})"
    password =m
    result = re.findall(pattern,password)
    if (result):
        print("Valid password")
    else:
        print("password not valid")
check("1234AAAAaaaa")
check("1234AAAAaaAA")