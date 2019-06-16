# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:14:03 2019

@author: aksha
"""

import requests
import pprint
from bs4 import BeautifulSoup


url='https://www.panerabread.com/en-us/menu-categories/sandwiches-panini.html'

paneera_r=requests.get(url)
#print(paneera_r.status_code)

paneera_soup=BeautifulSoup(paneera_r.text,'html.parser')
#print(paneera_soup.prettify())

dict1={}

list1=[]
list2=[]

main_menu=(paneera_soup.findAll('div',{'class','main-content'}))


for dat in main_menu:
	for menu in dat.findAll('div',{'class','item-name'}):
		list1.append(menu.text)
	for cal in dat.findAll('span',{'class','calories'}):
		list2.append(cal.text)

for item_a, item_b in zip(list1,list2):
    print(item_a," : ", item_b)
