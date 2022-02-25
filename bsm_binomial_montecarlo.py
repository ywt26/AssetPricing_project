# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:55:39 2022

@author: YWT
"""

import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.stats import norm
import matplotlib.pyplot as plt


class bbm():
    
    
    def __init__(self, option_type, S0, K ,T ,r , sigma):
        
        self.type = 'call' if option_type == 'call' else 'put'
        self.type_num = 1 if option_type == 'call' else -1
        self.s0 = S0
        self.k = K
        self.t = T
        self.sigma = sigma
        self.r = r
    
    
    def bsmvalue(self):
        
        self.d1 = (np.log(self.s0/self.k)+(self.r+0.5*self.sigma**2)*self.t)/(self.sigma*np.sqrt(self.t))
        self.d2 = self.d1-self.sigma*np.sqrt(self.t)
        self.bsmvalue = self.type_num *(self.s0*norm.cdf( self.type_num*self.d1)-self.k*np.exp(-self.r*self.t)*norm.cdf( self.type_num*self.d2))
        return self.bsmvalue
    
    
    def bivalue(self, digital_type = 0, step = 1):
        
        # if the option is a digital call/put, set digital_type = 1 ; otherwise, set digital_type = 0
        self.tau = self.t /step
        self.u = np.exp(self.sigma*np.sqrt(self.tau))
        self.d = 1/self.u
        self.q = (np.exp(self.r*self.tau)-self.d)/(self.u-self.d)
        
        ST = np.zeros(step + 1)    # assuming the last step of underlying prices are all zeros
        value = np.zeros(step + 1)  # assuming the last step of call prices are all zeros
        ST[0] = self.s0*self.d**step   
        
        if digital_type == 1: 
            value[0] = (np.maximum(self.type_num*(ST[0] - self.k),0))/ (self.type_num*(ST[0]-self.k))   
            for i in range(1,step+1):
                ST[i] = ST[i-1]*(self.u**2)
                value[i] = (np.maximum(self.type_num * (ST[i]-self.k),0))/(self.type_num*(ST[i]-self.k))
            for j in range(step, 0 ,-1):
                for i in range(0,j):
                    ST[i] = ST[i+1]*self.d
                    value[i] = np.maximum((self.q*value[i+1]+(1-self.q)*value[i])*np.exp(-self.r*self.tau/step), 
                                          self.type_num * (ST[i]-self.k))
        elif digital_type == 0:
            value[0] = (np.maximum(self.type_num*(ST[0] - self.k),0))
            for i in range(1,step+1):
                ST[i] = ST[i-1]*(self.u**2)
                value[i] = (np.maximum(self.type_num * (ST[i]-self.k),0))
            for j in range(step, 0 ,-1):
                for i in range(0,j):
                    ST[i] = ST[i+1]*self.d
                    value[i] = np.maximum((self.q*value[i+1]+(1-self.q)*value[i])*np.exp(-self.r*self.tau/step), 
                                          self.type_num * (ST[i]-self.k))
                    # for european option:
                    # value[i] = (self.q*value[i+1]+(1-self.q)*value[i])*np.exp(-self.r*self.tau/step)
        else:
            print("Please input the digital type of the option.")
                
        return value[0]
        
    
    def mcvalue(self, path = 10000,wholeyear = 256):
        
        days = int(self.t*wholeyear)
        tau = self.t/ days
        eps = np.random.normal(0,1,(days,path))
        St = self.s0 *np.exp(np.cumsum((self.r- 0.5 * self.sigma**2)*tau + self.sigma*np.sqrt(tau)*eps, axis=0))   
        St = np.vstack([(np.ones(path)*self.s0).T, St])
        
        return np.mean(St[-1])*np.exp(-self.r*self.t)
        
        
        

