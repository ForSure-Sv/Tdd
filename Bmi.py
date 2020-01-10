

def bmiCalc(height,weight):
    bmi = weight/(height**2)
    # ** is the power of operator i.e height*height in this case
    print("Your BMI is: {0} and you are: ".format(bmi), end='')
    #conditions
    if (bmi < 16):
        return "severely underweight"
    elif ( bmi >= 16 and bmi < 18.5):
        return "underweight"
    elif ( bmi >= 18.5 and bmi < 25):
        return "Healthy"
    elif ( bmi >= 25 and bmi < 30):
        return "overweight"
    elif ( bmi >=30):
        return "severely overweight"



import unittest

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
        result1 = bmiCalc(height,weight)
        result2 = bmiCalc(height2,weight2)
        result3 = bmiCalc(height3,weight3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

if __name__ == '__main__':
    unittest.main()
