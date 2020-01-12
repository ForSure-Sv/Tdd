import unittest

from src.BubbleSort import BubbleSort

class BubbleSortCalcTesting(unittest.TestCase):
    def test_bubbleSort(self):
        # stub
        arr1 = [4,3,2,1]
        arr2 = [1]
        arr3 = [0, 3, 5,-5,-2]
        arr4 = []

        # assume
        expected1 = [1, 2, 3, 4]
        expected2 = [1]
        expected3 = [-5, -2, 0, 3, 5]
        expected4 = []


        # action
        result1 = BubbleSort.bubbleSort(arr1)
        result2 = BubbleSort.bubbleSort(arr2)
        result3 = BubbleSort.bubbleSort(arr3)
        result4 = BubbleSort.bubbleSort(arr4)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)


if __name__ == '__main__':
    unittest.main()