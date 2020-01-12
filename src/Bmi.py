class BmiCalculator:

    @staticmethod
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

