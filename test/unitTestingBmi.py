

import unittest
from src.Bmi import BmiCalculator

class BmiCalcTesting(unittest.TestCase):
    def test_Bmi_calculation(self):
        # stub
        height,weight = 1.80,50
        height2, weight2 = 1.50,41
        height3,weight3 = 2,200
        # assume
        expected1 = "severely underweight"
        expected2 = "underweight"
        expected3 = "severely overweight"

        # action
        result1 = BmiCalculator.bmiCalc(height,weight)
        result2 = BmiCalculator.bmiCalc(height2,weight2)
        result3 = BmiCalculator.bmiCalc(height3,weight3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

if __name__ == '__main__':
    unittest.main()
