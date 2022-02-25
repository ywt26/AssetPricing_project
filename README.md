"imv" package
============
## Overview

["imv"](https://github.com/ywt26/AssetPricing_project/blob/main/imv.py) is a package that provides functions to price an option based on given parameters and long-short portfolio, graph the distribution and display higher order moments of option returns distribution. "imv" combines two classes, `Option()` and `interp_pricing()`. `Option()` helps to replace underlying asset price S0 with a theoretical price, then calculate option price with theoretical asset price. `interp_pricing()` applies cubic spline method to price an option, and derive higher order moments of option return.

* `Option.putcallparity()` calculates the mean of theoretical underlying asset price
* `Option.imv_bisection(callornot = 0, price_est = 0, top = .8, floor = .01)` calculates the implied volatility using bisection method; if it's a call option, set variable `callornot = 0`, if it's a put, `callornot = 1`
* `Option.bsmvalue()` calculates call/put prices using BSM model, whose output is used in calculating the implied volatility  
* `interp_pricing.interp_imv()` conducts cubic spline interpolation on implied volatility  
* `interp_pricing.moments()` calculates higher order moments of implied volatility calculated from `interp_imv()`
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

Input option dataset and enter one-dimension array(float) for each parameter, then call functions.

```
# Class

Option(self, K, bid, ask, price, r, T)
interp_pricing(self, S0, K, imv, r, T)
```
```
# Functions

theo_S0 = Option(self, K, bid, ask, price, r, T).putcallparity(c = False, p = False) 
# Parameters: the default setting is to use bid-ask prices to replace call-put prices if they're not available
# Returns: theoretical underlying asset pricing

Option(self, K, bid, ask, price, r, T).imv_bisection(theo_S0, callornot = 0, price_est = 0, top = .8, floor = .01) # if it's a call option, set variable `callornot = 0`, if it's a put, `callornot = 1`

```   

see [imv_test.py](https://github.com/ywt26/AssetPricing_project/blob/main/imv_test.py).

 "bsm_binomial_montecarlo" package
============
## Overview

## Motivation

## Usage
