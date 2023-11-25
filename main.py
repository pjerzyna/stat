import numpy as np
from scipy.stats import skew 
from scipy.stats import kurtosis
from typing import Union 
from prettytable import PrettyTable

#dodac bledy i wyjatki

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
    # w zależności od kaprysu, można coś jeszcze dodać
    entropy = 2 #entropia - miara nieuporządkowania

    info = {
        'srednia' : mean,
        'odchylenie standardowe' : s,
        'wspolczynnik zmiennosci' : v,
        'minimum' : x_min,
        '10 precentyl' : p10,
        '1 kwartyl' : k1,
        'mediana' : mediana,
        '3 kwartyl' : k3,
        '90 precentyl' : p90,
        'maksimnum' : x_max,
        'rozstep danych' : r,
        'rozstep miedzykwartylowy' : rkk,
        'skosnosc' : skewness,
        'kurtoza' : kurt
    }

    table = PrettyTable(["Cecha", "Wartosc"])
    for key, value in info.items():
        table.add_row([key, value])
    
    return table

#pogoda Krakow listopad
v = [15, 13, 15, 13, 11, 11, 12, 11, 11, 9, 10, 10 ,11, 10, 12, 10, 8, 8, 7, 6, 8, 6, 6, 7, 1, 0, 0, -1, -2, -1]
m = stats(v)
print(m)