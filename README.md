# Week 2 Assignment: Testing Go for Statistics

## Project Summary

### This project tests statistical packages across Go, Python and R languages. The goal is to ensure similar results are obtained for estimating linear regression coefficients for the Anscombe Quartet dataset. The Anscombe Quartet, developed by Anscombe (1973), is a set of four data sets with one independent variable x and one dependent variable y. Simple linear regression of y on x yields identical estimates of regression coefficients despite the fact that these are very different data sets.

### The results show that all 3 stats packages yield expected results. In addition to running the statistics, we also ran benchmarking for each program to determine the runtime. Go produced the fastest results by far. For this, I ran the programs in my MacOS terminal window with the following results:
- Go: 1054 nanoseconds
- Python: 0.027 seconds
- R: 0.019 seconds

### This project helped alleviate some of the concerns that the data science team has with transitioning to Go as the main programming language for the company. However, while this statistical package worked for this project to produce simple linear regression models over the Anscombe Quartet, we are uncertain of the capabilities Go has for more complex AI/ML models.

## Files

### *anscombe.go*
### Main function loads Anscombe Quartet data and calls RegressCoef function to calculate regression coefficients. This code uses the LinearRegression function from the [montanaflynn/stats](https://github.com/montanaflynn/stats) package. To replicate results:

> go run anscombe.go

### *anscombe_test.go*
### Unit test for RegressCoef function ensures that the calculated coefficients match the output for Python and R (0.5, 3). Also includes a benchmarking test of runtime. To replicate results:

> go test
> go test -bench=.

### *anscombe_python.py*
### Main function run the runRegression function which loads the Anscombe Quartet data and calculates regression coefficients using the statsmodel package. The main function also starts the benchmarking test using the timeit package. We specified the test to run 500 times. To replicate results:

> python anscombe_python.py

### *anscombe_r.R*
### Program loads the Anscombe Quartet data and runs the built-in lm function to return regression analysis. We used the Sys.time() funtion to benchmarking test. To replicate results:

> Rscript anscombe_r.R