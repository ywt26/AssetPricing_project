# README
## Overview
"imv" is a package that provides functions to price an option based on based on given parameters and cubic spline method, graph the distribution and display higher order moments of option returns distribution. "imv" combines two class, `Option()` and `interp_pricing()`. `Option()` helps to replace underlying asset price S0 with a theoretical price, then calculate option price with theoretical asset price. `interp_pricing()` applies cubic spline method to price an option and derive higher order moments of option return.

bin_choose() calculates the number of combinations given number of trials and success
bin_probability() calculates the probaility of getting k success out of n trials, given probability per trial
bin_distribution() generates a table with all the possible success and corresponding overall probability, given the number of trials and probability of success per trial
bin_cum() calculates cumulative probability based on the table with success and probability derived
plot() gives graphs of data frames derived
bin_variable() creates a binomial variable
bin_summary() generates a summary of the binomial variable
bin_mean() calculates the mean of the binomial distribution
bin_variance() calculates the variance of the binomial distribution
bin_mode() calculates the mode of the binomial distribution
bin_skewness() calculates the skewness the given binomial distribution
bin_kurtosis() calculates the kurtosis the given binomial distribution
## Motivation
## Usage
