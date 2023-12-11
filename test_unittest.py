from main import stats
import unittest
import numpy as np


class TestList(unittest.TestCase):
    
    def setUp(self):
        #arrange
        self.v1 = [15, 13, 15, 13, 11, 11, 12, 11, 11, 9, 10, 10 ,11, 10, 12, 10, 8, 8, 7, 6, 8, 6, 6, 7, 6, 0, 0, -1, -2, -1]
        self.v2 = [15, 13, 15, 13, 11, 11, 12, 11, 11, 9, 10, 10 ,11, 10, 12, 10, 8, 8, 7, 6, 8, 6, 6, 7, 6, 0, 0, -1, -2, -1] #reverse it
        self.v3 = [15, 13, 15, 13, 11, 11, 12, 11, 11, 9, 10, 10 ,11, 10, 12, 10, 8, 8, 7, 6, 8, 6, 6, 7, 6, 0, 0, -1, -2, -1] #mixed it
        self.data123 = (
    "+--------------------------+----------------------+\n"
    "|   Statistical feature    |        Value         |\n"
    "+--------------------------+----------------------+\n"
    "|           mean           |  8.066666666666666   |\n"
    "|    standard deviation    |  4.6542692468552165  |\n"
    "| coefficient of variation |       57.70 %        |\n"
    "|         minimum          |          -2          |\n"
    "|       10 precentil       | -0.09999999999999964 |\n"
    "|        1 quartile        |         6.0          |\n"
    "|         mediana          |         9.5          |\n"
    "|        3 quartile        |         11.0         |\n"
    "|      90 precentile       |         13.0         |\n"
    "|         maximum          |          15          |\n"
    "|        data range        |          17          |\n"
    "|   interquartile range    |         5.0          |\n"
    "|         skewness         | -0.7981018225824705  |\n"
    "|         kurtosis         | -0.2267630964229661  |\n"
    "+--------------------------+----------------------+"
)


    def test_data(self):
        #act
        result1 = str(stats(self.v1))
        #assert
        self.assertEqual(result1, self.data123)

    def test_reversed_data(self):
        #act
        result2 = str(stats(self.v2))
        #assert
        self.assertEqual(result2, self.data123)

    def test_mixed_data(self):
        #act
        result3 = str(stats(self.v3))
        #assert
        self.assertEqual(result3, self.data123)

class TestVector(unittest.TestCase):

    def setUp(self):
        # arange
        self.vec = np.array([11, 17, 18, 19, 15, 17 ,20])
        self.data = (
    "+--------------------------+-----------------------+\n"
    "|   Statistical feature    |         Value         |\n"
    "+--------------------------+-----------------------+\n"
    "|           mean           |   16.714285714285715  |\n"
    "|    standard deviation    |   2.7627256579733883  |\n"
    "| coefficient of variation |        16.53 %        |\n"
    "|         minimum          |           11          |\n"
    "|       10 precentil       |          13.4         |\n"
    "|        1 quartile        |          16.0         |\n"
    "|         mediana          |          17.0         |\n"
    "|        3 quartile        |          18.5         |\n"
    "|      90 precentile       |          19.4         |\n"
    "|         maximum          |           20          |\n"
    "|        data range        |           9           |\n"
    "|   interquartile range    |          2.5          |\n"
    "|         skewness         |   -0.962280834857042  |\n"
    "|         kurtosis         | -0.004789956818897156 |\n"
    "+--------------------------+-----------------------+\n"
)


    def test_data(self):
        #act
        result = stats(self.vec)
        #assert
        self.assertEqual(result, self.data)


if __name__ == "__main__":
    unittest.main() #what does this mean
