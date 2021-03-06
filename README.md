Contents
============
* [imv package](https://github.com/ywt26/AssetPricing_project/blob/main/imv.py)
  * Overview
  * Motivation
  * Usage
* [bsm_binomial_montecarlo package](https://github.com/ywt26/AssetPricing_project/blob/main/bsm_binomial_montecarlo.py)
  * Overview
  * Motivation
  * Usage

imv package
============
## Overview

[imv](https://github.com/ywt26/AssetPricing_project/blob/main/imv.py) is a package that provides functions to price an option based on given parameters and long-short portfolio, graph the distribution and display higher order moments of option value distribution. "imv" combines two classes, `Option()` and `interp_pricing()`. `Option()` helps to replace underlying asset price S0 with a theoretical price, then calculate option price with theoretical asset price. `interp_pricing()` applies cubic spline method to price an option, and derive higher order moments of option return.

* `Option.putcallparity()` calculates the mean of theoretical underlying asset price
* `Option.imv_bisection(self, callornot = 0, price_est = 0, top = .8, floor = .01)` calculates the implied volatility using bisection method; if it's a call option, set variable `callornot = 0`, if it's a put, `callornot = 1`
* `Option.bsmvalue()` calculates call/put prices using BSM model, whose output is used in calculating the implied volatility  
* `interp_pricing.interp_imv()` conducts cubic spline interpolation on implied volatility  
* `interp_pricing.moments()` calculates higher order moments of option value calculated by BSM
* `interp_pricing.plots()` generates a plot with biosection imv, cubic spline imv, and Gross return distribution (CDF).

## Motivation

This package has been developed to illustrate the mechanism of calculating implied volatility, and pricing an option using long-short portfolios and interpolation method, through decomposing cost into multiple "bricks".

## Usage

Add the “imv” package to system path, and import two classes.

```
import os
import sys
sys.path.append('Your Path')
from imv import optionpricing, interp_pricing
```

Input option dataset and enter one-dimension array(float) for each parameter, then call functions. see [imv_test.py](https://github.com/ywt26/AssetPricing_project/blob/main/imv_test.py).

```
# Class
Option(self, K, bid, ask, price, r, T)
interp_pricing(self, S0, K, imv, r, T)
```
```
theo_S0 = Option(self, K, bid, ask, price, r, T).putcallparity(c = False, p = False) 
# Parameters: the default setting is to use bid-ask prices to replace call-put prices if they're not available
# Results: theoretical underlying asset pricing

Option(self, K, bid, ask, price, r, T).imv_bisection(theo_S0, callornot = 0, price_est = 0, top = .8, floor = .01) 
# Parameters: callornot: if it's a call option, set variable `callornot = 0`, if it's a put, `callornot = 1`
#             price_est: original price estimation
#             top/floor: range of bisection method
# Results: implied volatility

interp_pricing(self, S0, K, imv, r, T).interp_imv(callornot = 0, times=1000, kind = 3)
# Parameters: callornot: if it's a call option, set variable `callornot = 0`, if it's a put, `callornot = 1`
#             kind = 3: cubic spline method for calculate more imv
# Results: dataframe with more implied volatility

interp_pricing(self, S0, K, imv, r, T).moments(moment)
# Parameters: moment: enter 'mean/sigma/skew/kurto'
# Results: higher order moments of option value

interp_pricing(self, S0, K, imv, r, T).plots(plttype)
# Parameters: plttype:'imv', generating two options implied volatility, both bisetion method and cubic spline method
#                     'dist', generating gross return distribution (CDF)
```  
<div align=center>
<img src="https://github.com/ywt26/AssetPricing_project/blob/main/plots_imv.png" width="360"><img src="https://github.com/ywt26/AssetPricing_project/blob/main/plots_dist.png" width="360">
</div>

bsm_binomial_montecarlo package
============
## Overview
[bsm_binomial_montecarlo](https://github.com/ywt26/AssetPricing_project/blob/main/imv.py)('bbm') is a package that provides three ways to price an option, including Black-Scholes-Merton Model `bsmvalue()`, Binomial Tree No-arbitrage Model `bivalue()` and Monte Carlo Simulation `mcvalue()`. Parameters can be flexibly set to price a __call/ put/ digital call/ digital put option__ in `bivalue()` .

* `bbm.bsmvalue()` calculates the option value using Black-Scholes-Merton Model
* `bbm.bivalue(self, digital_type = 0, step = 1)` calculates the option value using Binomial Tree No-arbitrage Model. If the option is digital type, set variable `digital_type = 1`, otherwise, `digital_type = 1`; variable `step` decides the braches of binomial tree.
* `bbm.bivalue(self, path = 10000, wholeyear = 256)`calculates the option value using Monte Carlo Simulation, variable `wholeyear` is the total number of trading days in a year, it usually takes __360__ or __256__ for simplicity.

## Motivation
This package has been developed to summarize three typical models/methods for option pricing. 

## Usage
Add the “bsm_binomial_montecarlo” package to system path, and import two classes.

```
import os
import sys
sys.path.append('Your Path')
from bsm_binomial_montecarlo import bbm
```
Input option dataset and enter one-dimension array(float) for each parameter, then call functions. see [bsm_binomial_montecarlo_test.py](https://github.com/ywt26/AssetPricing_project/blob/main/bsm_binomial_montecarlo_test.py).
```
# Class
bbm(self, option_type, S0, K ,T ,r , sigma)
```
```
bbm(self, option_type, S0, K ,T ,r , sigma).bsmvalue()
bbm(self, option_type, S0, K ,T ,r , sigma).bivalue(digital_type = 0, step = 1)
bbm(self, option_type, S0, K ,T ,r , sigma).mcvalue(path = 10000,wholeyear = 256)
```

