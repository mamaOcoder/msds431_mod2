# Code adapted from 
# Miller, Thomas W. 2015. Modeling Techniques in Predictive Analytics with Python and R: A Guide to Data Science. Upper Saddle River, NJ: Pearson Education. [ISBN-13: 978-0-13-389206-2]
# 
# The Anscombe Quartet (Python)

# demonstration data from
# Anscombe, F. J. 1973, February. Graphs in statistical analysis. 
#  The American Statistician 27: 17–21.

# prepare for Python version 3x features and functions
from __future__ import division, print_function

# import packages for Anscombe Quartet demonstration
import pandas as pd  # data frame operations
import numpy as np  # arrays and math functions
import statsmodels.api as sm  # statistical models (including regression)

def runRegression ():
    # define the anscombe data frame using dictionary of equal-length lists
    anscombe = pd.DataFrame({'x1' : [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'x2' : [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'x3' : [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'x4' : [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
        'y1' : [8.04, 6.95,  7.58, 8.81, 8.33, 9.96, 7.24, 4.26,10.84, 4.82, 5.68],
        'y2' : [9.14, 8.14,  8.74, 8.77, 9.26, 8.1, 6.13, 3.1,  9.13, 7.26, 4.74],
        'y3' : [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
        'y4' : [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]})

    # fit linear regression models by ordinary least squares
    set_I_design_matrix = sm.add_constant(anscombe['x1'])
    set_I_model = sm.OLS(anscombe['y1'], set_I_design_matrix)
    print(set_I_model.fit().summary())

    set_II_design_matrix = sm.add_constant(anscombe['x2'])
    set_II_model = sm.OLS(anscombe['y2'], set_II_design_matrix)
    print(set_II_model.fit().summary())

    set_III_design_matrix = sm.add_constant(anscombe['x3'])
    set_III_model = sm.OLS(anscombe['y3'], set_III_design_matrix)
    print(set_III_model.fit().summary())

    set_IV_design_matrix = sm.add_constant(anscombe['x4'])
    set_IV_model = sm.OLS(anscombe['y4'], set_IV_design_matrix)
    print(set_IV_model.fit().summary())
    
if __name__ == "__main__":
    import timeit
    setup = "from __main__ import runRegression"
    # run function 500 times and divide by 500 to get average time of each run
    print(timeit.timeit("runRegression()", setup=setup, number=500)/500)