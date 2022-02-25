# README
## "imv" package
### Overview
"imv" is a package that provides functions to price an option based on given parameters and long-short portfolio, graph the distribution and display higher order moments of option returns distribution. "imv" combines two classes, `Option()` and `interp_pricing()`. `Option()` helps to replace underlying asset price S0 with a theoretical price, then calculate option price with theoretical asset price. `interp_pricing()` applies cubic spline method to price an option, and derive higher order moments of option return.

* `Option.putcallparity()` calculates the mean of theoretical underlying asset price
* `Option.imv_bisection(callornot = 0, price_est = 0, top = .8, floor = .01)` calculates the implied volatility using bisection method; if it's a call option, set variable `callornot` = 0, if it's a put, `callornot` = 1
* `Option.bsmvalue()` calculates call/put prices using BSM model, whose output is used in calculating the implied volatility
* `interp_pricing.interp_imv()`
* `interp_pricing.bsmvalue()`
* `interp_pricing.moments()`
* `interp_pricing.plots()` generates a table with all the possible success and corresponding overall probability, given the number of trials and probability of success per trial

Calculate implied volatility by dichotomy. If it is call, callornot = 0; if it is put, callornot = 1

### Motivation
This package has been developed to illustrate the mechanism of pricing an option by long-short portfolio.

### Usage


## "bsm_binomial_montecarlo" package
### Overview

### Motivation

### Usage
