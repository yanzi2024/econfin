#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yfinance as yf

ticker = "TSLA"

STOCK_NEWS = yf.Ticker(ticker).news;
for i in STOCK_NEWS:
    print(i['title']);
    print(i['link']);
    print("\n");
    
# @Yan, I don't have any ChatXXX API. Get a free API and we
# Can test feed these things into API and get evaluations.
# I can experiment with customized training etc but I don't
# have free API from my side and I am too low-income to afford
# a video card...
