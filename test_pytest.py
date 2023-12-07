from main import stats #importing a function to the test
import pytest
from prettytable import PrettyTable

@pytest.mark.parametrize(
)









def test_data(vector, output):
   # vector = [1, 2, 3, 4, 5, 6]
   # output = (
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

