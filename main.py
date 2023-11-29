import numpy as np
from scipy.stats import skew 
from scipy.stats import kurtosis
from typing import Union 
from prettytable import PrettyTable

#dodac bledy i wyjatki

def stats(vector: Union[np.ndarray, list]):
    
    mean = np.mean(vector) # the average of the set
    s = np. std(vector) # standard deviation - a measure of the amount of variation or dispersion of a set of values
    v = s / mean # coefficient of variation - the ratio of the standard deviation to the mean
    v_precentage = f"{v*100:.2f}" # % format
    x_min = min(vector) # the miniumim value
    #precentile devide the population into 100 parts, every 1% 
    p10 = np.percentile(vector, 10) # 10 percentile - 10% of the scorers is lower than you, 90% is higher 
    q1 = np.quantile(vector, 0.25) # 1 quartile, bottom quartile - 25% zbioru ma wartości niższe, a 75% wartości zbioru ma wartości wyższe
    mediana = np.median(vector) #the middle value of a given set of numbers 
    q3 = np.quantile(vector, 0.75) # 3 quartile - 75% zbioru ma wart niższe, a 25% zbioru ma wartości wyższe/równe 
    p90 = np.percentile(vector, 90) # 90 percentile - 90% of the scores is lower than you, 10% is higher
    x_max = max(vector)
    r = x_max - x_min # rozstęp?? - the difference between the largest and the smallest value in the set
    rkk = q3 - q1 # rozstę międzykwartylowy - różnica pomiędzy trzecim (k3) a pierwszym (k1) kwartylem
    skewness = skew(vector) # skewness - miara asymetrii rozkładu  [taki wzór był na wikipedii: 3 * (mean - mediana) / s)]
    kurt = kurtosis(vector) # kurtosis - miara kształtu rozkładu wartości cechy, jak bardzo spłaszczony ogony i podobny do normalnego
    
    # w zależności od kaprysu, można coś jeszcze dodać

    info = {
        'mean' : mean,
        'standard deviation' : s,
        'coefficient of variation' : f"{v_precentage} %",
        'minimum' : x_min,
        '10 precentyl' : p10,
        '1 kwartyl' : q1,
        'mediana' : mediana,
        '3 kwartyl' : q3,
        '90 precentyl' : p90,
        'maksimnum' : x_max,
        'rozstep danych' : r,
        'rozstep miedzykwartylowy' : rkk,
        'skewness' : skewness,
        'kurtosis' : kurt
    }

    table = PrettyTable(["Cecha", "Wartosc"])
    for key, value in info.items():
        table.add_row([key, value])
    
    return table

#pogoda Krakow listopad
v = [15, 13, 15, 13, 11, 11, 12, 11, 11, 9, 10, 10 ,11, 10, 12, 10, 8, 8, 7, 6, 8, 6, 6, 7, 1, 0, 0, -1, -2, -1]
m = stats(v)
print(m)