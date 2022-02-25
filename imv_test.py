# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:55:39 2022

@author: ywt26
"""
import os
import sys
import pandas as pd
sys.path.append('Your Path')

from imv import Option, interp_pricing

# realimv = [.2773,.2852, .2314, .2217, .2061, .1938, .1912, .1924, .1973, .2139, .2266]
df = pd.DataFrame()
df['strike'] = [2.85,2.90,2.95,3.00,3.10,3.20,3.30,3.40,3.50,3.60,3.70]
df['bids'] = [.3900,.3426,.2941,.2455,.1595,.0882,.0416,.0168,.0063,.0029,.0013]
df['asks'] = [.3864,.3396,.2920,.2452,.1592,.0881,.0415,.0167,.0062,.0026,.0011]
df['price'] = [.3900,.3444,.2920,.2455,.1592,.0882,.0416,.0168,.0062,.0029,.0013] 
df['T'] = 27/252
df['r'] = 0 

theo_S0 = df.apply(lambda x: Option(x['strike'], x['bids'], x['asks'], x['price'], x['r'], x['T']).putcallparity(), axis =1).mean()   
df['imv'] = df.apply(lambda x:Option(x['strike'], x['bids'], x['asks'], x['price'], x['r'], x['T']).imv_bisection(theo_S0), axis = 1)
df['theo_S0'] = theo_S0
new_df = interp_pricing(df['theo_S0'], df['strike'], df['imv'], df['r'], df['T']).interp_imv()
interp_pricing(df['theo_S0'], df['strike'], df['imv'], df['r'], df['T']).plots('imv')
