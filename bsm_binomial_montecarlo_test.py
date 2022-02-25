# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:55:39 2022

@author: YWT
"""
import os
import sys
import pandas as pd
sys.path.append('Your Path')

from bsm_binomial_montecarlo import bbm

strike = [2.85,2.90,2.95,3.00,3.10,3.20,3.30,3.40,3.50,3.60,3.70]
c_imv = [0,0,0,0,0,0.1514,0.1592,0.1646,0.1709,0.1914,0.2188]
c_bids = [0.4772,0.4248,0.3773,0.3276,0.2285,0.1368,0.0608,0.0189,0.0043,0.0012,0.0006]
c_asks = [0.4729,0.4227,0.3734,0.3270,0.2284,0.1365,0.0607,0.0188,0.0042,0.0011,0.0005]
c_price = [0.4750,0.4248,0.3765,0.3276,0.2284,0.1365,0.0607,0.0188,0.0042,0.0012,0.0005] # latest prices
p_imv = [0.3203,0.2891,0.2695,0.2578,0.2090,0.1914,0.1792,0.1807,0.2026,0.2676,0.3164]
p_bids = [0.0006,0.0006,0.0009,0.0014,0.0028,0.0098,0.0337,0.0905,0.1755,0.2740,0.3777]
p_asks = [0.0005,0.0005,0.0008,0.0011,0.0025,0.0097,0.0336,0.0902,0.1753,0.2716,0.3707]
p_price = [0.0005,0.0005,0.0008,0.0014,0.0025,0.0097,0.0336,0.0902,0.1755,0.2740,0.3722]

df = pd.DataFrame(strike, columns =['strike'])
df['S0'] = 3.312
df['r'] = 0.0177
df['T'] = 14/256
df['c_imv'] = c_imv
df['c_bids'] = c_bids
df['c_asks'] = c_asks
df['c_price'] = c_price
df['p_imv'] = p_imv
df['p_bids'] = p_bids
df['p_asks'] = p_asks
df['p_price'] = p_price

        
bsm = df.apply(lambda x: bbm('call', x['S0'], x['strike'],x['T'], x['r'],x['c_imv']).bsmvalue(), axis =1)
bi = df.apply(lambda x: bbm('put', x['S0'], x['strike'],x['T'], x['r'],x['p_imv']).bivalue(1, 8), axis =1)
mc = bbm('call', 3.312,3.3,14/256,0.0177, 0.1592).mcvalue()

