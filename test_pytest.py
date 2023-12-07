from main import stats #importing a function to test
import pytest
from prettytable import PrettyTable


# I need to convert this test the PrettyTable result into a dictionary for easier comparison


# works well when it has one input and one output
@pytest.mark.parametrize( 
        ('input_vec', 'expected_output'),
        (
            ([1, 2, 3, 4, 5, 6], PrettyTable([
    """+--------------------------+---------------------+
    |   Statistical feature    |        Value        |
    +--------------------------+---------------------+
    |           mean           |         3.5         |
    |    standard deviation    |  1.707825127659933  |
    | coefficient of variation |       48.80 %       | #change this prettytable into a dictionary 
    |         minimum          |          1          |
    |       10 precentil       |         1.5         |
    |        1 quartile        |         2.25        |
    |         mediana          |         3.5         |
    |        3 quartile        |         4.75        |
    |      90 precentile       |         5.5         |
    |         maximum          |          6          |
    |        data range        |          5          |
    |   interquartile range    |         2.5         |
    |         skewness         |         0.0         |
    |         kurtosis         | -1.2685714285714282 |
    +--------------------------+---------------------+"""
           ])),
        )
)



def test_vector(input_vec, expected_output):
    result = stats(input_vec) 
    assert result == expected_output # function.test_name

a = stats([1, 2, 3, 4, 5, 6])
print(a)