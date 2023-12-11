from main import stats #importing a function to the test
import pytest
import numpy as np

def test_data():
    vector = [1, 2, 3, 4, 5, 6]
    output = (
        "+--------------------------+---------------------+\n"
        "|   Statistical feature    |        Value        |\n"
        "+--------------------------+---------------------+\n"
        "|           mean           |         3.5         |\n"
        "|    standard deviation    |  1.707825127659933  |\n"
        "| coefficient of variation |       48.80 %       |\n"
        "|         minimum          |          1          |\n"
        "|       10 precentil       |         1.5         |\n"
        "|        1 quartile        |         2.25        |\n"
        "|         mediana          |         3.5         |\n"
        "|        3 quartile        |         4.75        |\n"
        "|      90 precentile       |         5.5         |\n"
        "|         maximum          |          6          |\n"
        "|        data range        |          5          |\n"
        "|   interquartile range    |         2.5         |\n"
        "|         skewness         |         0.0         |\n"
        "|         kurtosis         | -1.2685714285714282 |\n"
        "+--------------------------+---------------------+"
    )
    
    result = str(stats(vector))
    assert result == output
    
def test_reversed_data():
    vector = [6, 5, 4, 3, 2, 1]
    output = (
        "+--------------------------+---------------------+\n"
        "|   Statistical feature    |        Value        |\n"
        "+--------------------------+---------------------+\n"
        "|           mean           |         3.5         |\n"
        "|    standard deviation    |  1.707825127659933  |\n"
        "| coefficient of variation |       48.80 %       |\n"
        "|         minimum          |          1          |\n"
        "|       10 precentil       |         1.5         |\n"
        "|        1 quartile        |         2.25        |\n"
        "|         mediana          |         3.5         |\n"
        "|        3 quartile        |         4.75        |\n"
        "|      90 precentile       |         5.5         |\n"
        "|         maximum          |          6          |\n"
        "|        data range        |          5          |\n"
        "|   interquartile range    |         2.5         |\n"
        "|         skewness         |         0.0         |\n"
        "|         kurtosis         | -1.2685714285714282 |\n"
        "+--------------------------+---------------------+"
    )
    
    result = str(stats(vector))
    assert result == output

def test_mixed_data():
    vector = [4, 6, 2, 1, 3, 5]
    output = (
        "+--------------------------+---------------------+\n"
        "|   Statistical feature    |        Value        |\n"
        "+--------------------------+---------------------+\n"
        "|           mean           |         3.5         |\n"
        "|    standard deviation    |  1.707825127659933  |\n"
        "| coefficient of variation |       48.80 %       |\n"
        "|         minimum          |          1          |\n"
        "|       10 precentil       |         1.5         |\n"
        "|        1 quartile        |         2.25        |\n"
        "|         mediana          |         3.5         |\n"
        "|        3 quartile        |         4.75        |\n"
        "|      90 precentile       |         5.5         |\n"
        "|         maximum          |          6          |\n"
        "|        data range        |          5          |\n"
        "|   interquartile range    |         2.5         |\n"
        "|         skewness         |         0.0         |\n"
        "|         kurtosis         | -1.2685714285714282 |\n"
        "+--------------------------+---------------------+"
    )
    
    result = str(stats(vector))
    assert result == output

def test_empty():
    vector = []
    output = "Vector cannot be empty!"

    result = stats(vector)
    assert result == output

def test_data_2():
    vector = np.array([99, 98, 100, 12, 45, 36, 88, 10, -23, 32, 2, 0, -18, -2])
    output = (
    "+--------------------------+--------------------+\n"
    "|   Statistical feature    |       Value        |\n"
    "+--------------------------+--------------------+\n"
    "|           mean           | 34.214285714285715 |\n"
    "|    standard deviation    |  43.2685609576623  |\n"
    "| coefficient of variation |      126.46 %      |\n"
    "|         minimum          |        -23         |\n"
    "|       10 precentil       |       -13.2        |\n"
    "|        1 quartile        |        0.5         |\n"
    "|         mediana          |        22.0        |\n"
    "|        3 quartile        |       77.25        |\n"
    "|      90 precentile       |        98.7        |\n"
    "|         maximum          |        100         |\n"
    "|        data range        |        123         |\n"
    "|   interquartile range    |       76.75        |\n"
    "|         skewness         | 0.4384235699403917 |\n"
    "|         kurtosis         | -1.284395016367453 |\n"
    "+--------------------------+--------------------+"
)
    
    result = str(stats(vector)).strip()
    assert result == output

def test_reversed_data_2():
    vector = np.array([-2, -18, 0, 2, 32, -23, 10, 88, 36, 45, 12, 100, 98, 99])
    output = (
        "+--------------------------+---------------------+\n"
        "|   Statistical feature    |        Value        |\n"
        "+--------------------------+---------------------+\n"
        "|           mean           |  34.214285714285715 |\n"
        "|    standard deviation    |   43.2685609576623  |\n"
        "| coefficient of variation |       126.46 %      |\n"
        "|         minimum          |         -23         |\n"
        "|       10 precentil       |        -13.2        |\n"
        "|        1 quartile        |         0.5         |\n"
        "|         mediana          |         22.0        |\n"
        "|        3 quartile        |        77.25        |\n"
        "|      90 precentile       |         98.7        |\n"
        "|         maximum          |         100         |\n"
        "|        data range        |         123         |\n"
        "|   interquartile range    |        76.75        |\n"
        "|         skewness         |  0.4384235699403915 |\n"
        "|         kurtosis         | -1.2843950163674527 |\n"
        "+--------------------------+---------------------+"
    )

    
    result = str(stats(vector))
    assert result == output

def test_mixed_data_2():
    vector = np.array([98, 45, 10, -23, 36, 32, 99, 2, 0, 100, -18, 88, -2, 12])
    output = (
    '+--------------------------+---------------------+\n'
    '|   Statistical feature    |        Value        |\n'
    '+--------------------------+---------------------+\n'
    '|           mean           |  34.214285714285715 |\n'
    '|    standard deviation    |   43.2685609576623  |\n'
    '| coefficient of variation |       126.46 %      |\n'
    '|         minimum          |         -23         |\n'
    '|       10 precentil       |        -13.2        |\n'
    '|        1 quartile        |         0.5         |\n'
    '|         mediana          |         22.0        |\n'
    '|        3 quartile        |        77.25        |\n'
    '|      90 precentile       |         98.7        |\n'
    '|         maximum          |         100         |\n'
    '|        data range        |         123         |\n'
    '|   interquartile range    |        76.75        |\n'
    '|         skewness         | 0.43842356994039167 |\n'
    '|         kurtosis         | -1.2843950163674522 |\n'
    '+--------------------------+---------------------+'
    )
    
    result = str(stats(vector))
    assert result == output

def test_empty_2():
    vector = np.array([])
    output = "Vector cannot be empty!"

    result = stats(vector)
    assert result == output

def test_dimensions():
    vector = np.array([[1, 2, 3], [3, 2, 1], [4, 7, 0]])
    output = "Vector must be 1D!"

    result = stats(vector)
    assert result == output