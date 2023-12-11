from main import stats
import unittest
import numpy as np


class StatTest(unittest.TestCase):
    
#     def setUP(self):
#         #arrange
#         self.v = [15, 13, 15, 13, 11, 11, 12, 11, 11, 9, 10, 10 ,11, 10, 12, 10, 8, 8, 7, 6, 8, 6, 6, 7, 6, 0, 0, -1, -2, -1]
#         self.data = (
#     "+--------------------------+----------------------+\n"
#     "|   Statistical feature    |        Value         |\n"
#     "+--------------------------+----------------------+\n"
#     "|           mean           |  8.066666666666666   |\n"
#     "|    standard deviation    |  4.6542692468552165  |\n"
#     "| coefficient of variation |       57.70 %        |\n"
#     "|         minimum          |          -2          |\n"
#     "|       10 precentil       | -0.09999999999999964 |\n"
#     "|        1 quartile        |         6.0          |\n"
#     "|         mediana          |         9.5          |\n"
#     "|        3 quartile        |         11.0         |\n"
#     "|      90 precentile       |         13.0         |\n"
#     "|         maximum          |          15          |\n"
#     "|        data range        |          17          |\n"
#     "|   interquartile range    |         5.0          |\n"
#     "|         skewness         | -0.7981018225824705  |\n"
#     "|         kurtosis         | -0.2267630964229661  |\n"
#     "+--------------------------+----------------------+"
# )

    def test_data(self):
        v = [15, 13, 15, 13, 11, 11, 12, 11, 11, 9, 10, 10 ,11, 10, 12, 10, 8, 8, 7, 6, 8, 6, 6, 7, 6, 0, 0, -1, -2, -1]
        data = (
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
        
        #act
        result = str(stats(v))
        #assert
        self.assertEqual(result, data)



if __name__ == "__main__":
    unittest.main()