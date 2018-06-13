#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:54:17 2018

@author: nakau
"""
#coding utf-8


import pandas as pd

#读取文件

data_url='http://donnees.ville.montreal.qc.ca/dataset/f170fecc-18db-44bc-b4fe-5b0b6d2c7297/resource/ee1e9541-939d-429e-919a-8ab94527773c/download/comptagevelo2009.csv'
df=pd.read_csv(data_url,encoding='utf-8',sep=',',index_col='Date',parse_dates=['Date'],dayfirst=True)
df.head()
df['Berri1'].plot()