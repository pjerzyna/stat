import numpy as np
from scipy.stats import skew 
from scipy.stats import kurtosis
from typing import Union 

#pozostało sprawdzić błędy, dodać podowiedzi typów itp

def stats(vector: Union[np.ndarray, list]):
    mean = np.mean(vector) #średnia
    s = np. std(vector) #odchylenie standardowe
    v = s / mean #współczynnik zmienności (można razy 100% dać, wtedy będzie w wart. procentowych)
    x_min = min(vector) #minimum
    #precentyle inaczej centyle dzielą zbiorowość na 100 części, czyli co 1% 
    p10 = np.percentile(vector, 10) # 10 precentyl - 10% zbioru ma mniejszą wart a 90% zbioru ma wartość większą/równą 
    k1 = np.quantile(vector, 0.25) #1 kwartyl, kwartyl dolny - 25% zbioru ma wartości niższe, a 75% wartości zbioru ma wartości wyższe
    mediana = np.median(vector) #mediana 
    k3 = np.quantile(vector, 0.75) #3 kwartyl - 75% zbioru ma wart niższe, a 25% zbioru ma wartości wyższe/równe 
    p90 = np.percentile(vector, 90) # 90 precentyl - 90% zbioru ma mniejszą wart a 10% zbioru ma wartość większą/równą
    x_max = max(vector) #maksimum
    r = x_max - x_min #rozstęp - różnica pomiędzy wartością największą a najmniejszą w zbiorze
    rkk = k3 - k1 #rozstę międzykwartylowy - różnica pomiędzy trzecim (k3) a pierwszym (k1) kwartylem
    skewness = skew(vector) #skośność - miara asymetrii rozkładu  [taki wzór był na wikipedii: 3 * (mean - mediana) / s)]
    kurt = kurtosis(vector) #kurtoza - miara kształtu rozkładu wartości cechy, jak bardzo spłaszczony ogony i podobny do normalnego
    return skewness


v1 = [1, 2, 3, 4, 5, 6]
m = stats(v1) 
print(m)