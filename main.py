import numpy as np
from scipy.stats import skew 
from scipy.stats import kurtosis
from typing import Union 
from prettytable import PrettyTable

#exeptions and errors

def stats(vector: Union[np.ndarray, list]):
    
    mean = np.mean(vector) # the average of the set
    s = np. std(vector) # standard deviation - a measure of the amount of variation or dispersion of a set of values
    v = s / mean # coefficient of variation - the ratio of the standard deviation to the mean
    v_precentage = f"{v*100:.2f}" # format with %
    x_min = min(vector) # the miniumim value
    #precentile devide the population into 100 parts, every 1% 
    p10 = np.percentile(vector, 10) # 10 percentile - 10% of the data is lower, 90% is higher 
    q1 = np.quantile(vector, 0.25) # 1 quartile, bottom quartile - 25% of the data has lower values, 75% has higher values
    mediana = np.median(vector) #the middle value of a given set of numbers 
    q3 = np.quantile(vector, 0.75) # 3 quartile - 75% of the data has higher values, 25% has lower values 
    p90 = np.percentile(vector, 90) # 90 percentile - 90% of the data is lower, 10% is higher
    x_max = max(vector) # the maximum value
    r = x_max - x_min # the range - the difference between the largest and the smallest value in the set
    ir = q3 - q1 # interquartile range - the difference between the first (q1) and third (q3) quartile
    skewness = skew(vector) # skewness - a measure of the asymetry of a distribution
    kurt = kurtosis(vector) # kurtosis - a measure used to describe the distribution of data and assess the shape of tails relative to a normal distribution.
    
    #(optional) - add new attributes 

    info = {
        'mean' : mean,
        'standard deviation' : s,
        'coefficient of variation' : f"{v_precentage} %",
        'minimum' : x_min,
        '10 precentil' : p10,
        '1 quartile' : q1,
        'mediana' : mediana,
        '3 quartile' : q3,
        '90 precentile' : p90,
        'maximum' : x_max,
        'data range' : r,
        'interquartile range' : ir,
        'skewness' : skewness,
        'kurtosis' : kurt
    }

    table = PrettyTable(["Statistical feature", "Value"])
    for key, value in info.items():
        table.add_row([key, value])
    
    return table
