# README
## "imv" package
### Overview
"imv" is a package that provides functions to price an option based on given parameters and long-short portfolio, graph the distribution and display higher order moments of option returns distribution. "imv" combines two class, `Option()` and `interp_pricing()`. `Option()` helps to replace underlying asset price S0 with a theoretical price, then calculate option price with theoretical asset price. `interp_pricing()` applies cubic spline method to price an option, and derive higher order moments of option return.

* bin_choose() calculates the number of combinations given number of trials and success
* bin_probability() calculates the probaility of getting k success out of n trials, given probability per trial
* bin_distribution() generates a table with all the possible success and corresponding overall probability, given the number of trials and probability of success per trial

### Motivation
This package has been developed to illustrate the mechanism of pricing an option by long-short portfolio.

### Usage


##"bsm_binomial_montecarlo" package
### Overview

### Motivation

### Usage
