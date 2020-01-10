import unittest

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



class BubbleSortCalcTesting(unittest.TestCase):
    def test_bubbleSort(self):
        # stub
        arr1 = [4,3,2,1]
        arr2 = [1]
        arr3 = [0, 3, 5,-5,-2]

        # assume
        expected1 = [1, 2, 3, 4]
        expected2 = [1]
        expected3 = [-5, -2, 0, 3, 5]

        # action
        result1 = bubbleSort(arr1)
        result2 = bubbleSort(arr2)
        result3 = bubbleSort(arr3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


if __name__ == '__main__':
    unittest.main()