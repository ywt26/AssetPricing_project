# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:19:31 2021

@author: YWT
"""
import os
import sys
import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.stats import norm
import matplotlib.pyplot as plt


class Option():
    
    def __init__(self, K, bid, ask, price, r, T):
        self.K = K
        self.bid = bid
        self.ask = ask
        self.price = price
        self.r = r
        self.T = T
        
    # 由于ETF的现货价格不能直接用S0=3.231，因此用Put-call parity计算得到S0的平均作为现货理论价格
    def putcallparity(self, c = False, p = False):
        if c&p :
            self.S0 = c - p + self.K*np.exp(-self.r*self.T)
        else: 
            self.S0 = self.bid - self.ask + self.K*np.exp(-self.r*self.T)
        return self.S0

    # 二分法计算隐含波动率. 如果是call, callornot =0;如果是put ,callornot = 1
    def imv_bisection(self, theo_S0, callornot = 0, price_est = 0, top = .8, floor = .01):
        self.sigma = (top+floor)/2
        while abs(self.price - price_est)>1e-6:
            price_est = self.bsmvalue(theo_S0)[callornot]
            if self.price-price_est >0:
                floor = self.sigma
                self.sigma = (self.sigma+top)/2
            else:
                top = self.sigma
                self.sigma = (self.sigma+floor)/2
        return self.sigma
    
    # 用BSM计算出在理论现货价格下的call, put value
    def bsmvalue(self, theo_S0 = False): 
        if theo_S0:
            S0 = theo_S0
        else:
            S0 = self.putcallparity() 
        self.d1 = (np.log(S0/self.K)+(self.r+0.5*self.sigma**2)*self.T)/(self.sigma*np.sqrt(self.T))
        self.d2 = self.d1-self.sigma*np.sqrt(self.T)
        self.c = S0*norm.cdf(self.d1)-self.K*np.exp(-self.r*self.T)*norm.cdf(self.d2)
        self.p = self.K*np.exp(-self.r*self.T)*norm.cdf(-self.d2) - S0*norm.cdf(-self.d1)
        return self.c, self.p
        
class interp_pricing():

    def __init__(self, S0, K, imv, r, T):
        self.S0 = S0
        self.r = r
        self.T = T
        self.K = K
        self.sigma = imv
        self.new_df = pd.DataFrame()
    
    # 对imv进行三次样条插值
    def interp_imv(self, callornot = 0, times=1000, kind = 3):
        
        start = self.K[0]
        end = self.K[len(self.K)-1]
        length = int((end-start)*times+1)
        
        new_df = pd.DataFrame()
        new_df['K'] = np.linspace(start, end, length)
        new_df['imv'] = interpolate.interp1d(self.K, self.sigma, kind)(new_df['K'])
        new_df['r'] = np.tile(self.r.values[0],length)
        new_df['T'] = np.tile(self.T.values[0],length)
        new_df['S0'] = np.tile(self.S0.values[0],length)
        new_df['price'] = interp_pricing.bsmvalue(new_df['S0'], new_df['K'], new_df['imv'], new_df['r'], new_df['T'])[callornot]
        new_df['cost_brick'] = times*(new_df['price'].shift(-1) + new_df['price'].shift(1) -2*new_df['price'])
        new_df.loc[new_df[new_df['cost_brick']<0].index, 'cost_brick'] = 0
        new_df['modified_cdf'] = new_df['cost_brick'].cumsum() * 1/new_df['cost_brick'].cumsum().max()
        new_df['modified_pdf'] = new_df['modified_cdf'].diff()
        self.new_df = new_df
        
        return self.new_df
    
    def bsmvalue(S0, K ,sigma, r, T):
        d1 = (np.log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
        d2 = d1-sigma*np.sqrt(T)
        c = S0*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
        p = K*np.exp(-r*T)*norm.cdf(-d2) - S0*norm.cdf(-d1)
        return c, p
    
    def moments(self,moment):
        
        new_df = self.interp_imv()
        mean = (new_df['K']/new_df['S0']*new_df['modified_pdf']).sum()
        sigma = np.sqrt((((new_df['K']/new_df['S0']-mean)**2)*new_df['modified_pdf']).sum())
        skew = ((((new_df['K']/new_df['S0']-mean)/ sigma)**3)*new_df['modified_pdf']).sum()
        kurto = ((((new_df['K']/new_df['S0']-mean)/ sigma)**4)*new_df['modified_pdf']).sum()
        
        if moment == 'mean':
            return mean
        elif moment == 'sigma':
            return sigma
        elif moment == 'skew':
            return skew
        elif moment == 'kurto':
            return kurto

    def plots(self,plttype):
                
        if plttype == 'imv':
            fig, ax1 = plt.subplots(figsize = (12,8))
            title = ('Options implied volatility')
            plt.title(title, fontsize = 20)
            plt.grid(color = 'grey', linestyle = '--', lw =0.5, alpha = 0.5)
            plt.tick_params(axis = 'both',labelsize = 12)   
            ax1.plot(self.K, self.sigma, color = 'C0', label = 'biosection imv')
            ax1.plot(self.interp_imv().K, self.interp_imv().imv, color = 'r', label = 'cubic spline imv')
            plt.legend(fontsize = 12)
        elif plttype == 'dist':
            fig, ax2 = plt.subplots(figsize = (12,8))
            title = ('Gross return distribution (CDF)')
            plt.title(title, fontsize = 20)
            plt.grid(color = 'grey', linestyle = '--', lw =0.5, alpha = 0.5)
            plt.tick_params(axis = 'both',labelsize = 12)   
            ax2.plot(new_df['K'], new_df['modified_cdf'], color = 'r', label = 'modified CDF')
            plt.legend(fontsize = 12)

            




    



