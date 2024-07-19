#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Simple dashboard for monitored tickers

import yfinance as yf;

# Import the list of favorite tickers

with open('favorite.txt', 'r') as f:
    fav_tickers = [line.strip() for line in f];

fav_tickers = [i for i in fav_tickers if len(i)>0 & len(i)<6];

print("Ticker    Last    Prev  Chg(%)    High     Low");
print("----------------------------------------------");
#      12345:1234567812345678123456781234567812345678

for i in fav_tickers:
    getStock = yf.Ticker(i).info;
    p = getStock['currentPrice'];
    p0 = getStock['previousClose'];
    chg = (p/p0-1)*100;
    h = getStock['dayHigh'];
    l = getStock['dayLow'];
    if p<p0:
        print("\033[91m%5s:%8.2f%8.2f%+8.2f%8.2f%8.2f\033[00m" %
          (i, p, p0, chg, h, l));
    elif p>p0:
        print("\033[92m%5s:%8.2f%8.2f%+8.2f%8.2f%8.2f\033[00m" %
          (i, p, p0, chg, h, l));        
    else:
        print("%5s:%8.2f%8.2f%+8.2f%8.2f%8.2f\033" %
          (i, p, p0, chg, h, l));           
        
print("----------------------------------------------");

