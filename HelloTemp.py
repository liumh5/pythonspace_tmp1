# -*- coding: utf-8 -*-
import random
import time
import datetime

t = time.time()

print (t)                       #原始时间数据
print (int(t))                  #秒级时间戳
print (int(round(t * 1000)))    #毫秒级时间戳

nowTime = lambda:int(round(t * 1000))
print (nowTime());              #毫秒级时间戳，基于lambda

print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化
print("HelloTemp")
proxies = ["222.85.28.130:52590","117.191.11.80:80","117.127.16.205:8080","118.24.128.46:1080","120.78.225.5:3128","113.124.92.200:9999","183.185.1.47:9797","115.29.3.37:80","36.248.129.158:9999","222.89.32.182:9999","117.191.11.111:80","182.35.84.182:9999","47.100.103.71:80","121.63.209.92:9999","124.193.37.5:8888","39.135.24.11:8080","14.146.95.4:9797","182.35.83.244:9999","113.120.36.179:9999","1.199.31.90:9999","58.17.125.215:53281","212.64.51.13:8888","182.35.84.135:9999","163.204.247.60:9999","39.106.35.21:3128","202.39.222.32:80","120.83.111.42:9999","63.220.1.43:80","42.238.85.70:9999","117.191.11.107:80"]

print(random.choices(proxies)[0])