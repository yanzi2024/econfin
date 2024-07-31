#!/usr/bin/python3
# -*- coding: utf-8 -*-


import requests as rq;
import re;

https_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Referer': 'https://finance.sina.com.cn'
        };

url_api = 'https://hq.sinajs.cn/etag.php?list=';

regex_string = r'"(.*?)"';

with open('favorite.txt', 'r') as f:
    fav_tickers = [line.strip() for line in f];


api_feed = ','.join(['gb_'+x.lower() for x in fav_tickers]);

api_resp = rq.get(url_api + api_feed,
                  headers = https_headers);

if api_resp.status_code == 200:
    api_results = api_resp.text.split(";");
    results = [];
    for x in api_results:
        match = re.search(regex_string, x);
        results.append( match.group(1).split(',') if match else [] );

print("%-10s\t%10s" %("名字", "现价"));
print("---------------------------------")
for i in results:
    if len(i)>30:
        print("%-10s\t%10s" %( i[0][:10], i[1]));


        
        
        
