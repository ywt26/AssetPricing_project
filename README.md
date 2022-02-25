Contents  
============
- ["imv" package](#"imv"-package)  
  - [Overview](#overview)  
  - [Motivation](#motivation)  
  - [Usage](#usage) 
- ["bsm_binomial_montecarlo" package](#"bsm_binomial_montecarlo"-package)  
  - [Overview](#overview)  
  - [Motivation](#motivation)  
  - [Usage](#usage) 


"imv" package
============
### Overview

"imv" is a package that provides functions to price an option based on given parameters and long-short portfolio, graph the distribution and display higher order moments of option returns distribution. "imv" combines two classes, `Option()` and `interp_pricing()`. `Option()` helps to replace underlying asset price S0 with a theoretical price, then calculate option price with theoretical asset price. `interp_pricing()` applies cubic spline method to price an option, and derive higher order moments of option return.

* `Option.putcallparity()` calculates the mean of theoretical underlying asset price
* `Option.imv_bisection(callornot = 0, price_est = 0, top = .8, floor = .01)` calculates the implied volatility using bisection method; if it's a call option, set variable `callornot = 0`, if it's a put, `callornot = 1`
* `Option.bsmvalue()` calculates call/put prices using BSM model, whose output is used in calculating the implied volatility  
* `interp_pricing.interp_imv()` conducts cubic spline interpolation on implied volatility  
* `interp_pricing.moments()` calculates higher order moments of implied volatility calculated from `interp_imv()`
* `interp_pricing.plots()` generates a plot with biosection imv, cubic spline imv, and Gross return distribution (CDF).

### Motivation

This package has been developed to illustrate the mechanism of calculating implied volatility, and pricing an option using long-short portfolios and interpolation method, through decomposing cost into multiple "bricks".

### Usage
```
import os
import sys
sys.path.append('Your Path')
from imv import optionpricing, interp_pricing
```

 "bsm_binomial_montecarlo" package
============
### Overview

### Motivation

### Usage
