You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_105_code import by_length
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """

    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arr

 Here is a complete unittest test suite for the `by_length` function:


import unittest
from HumanEval_105_code import by_length

class TestByLength(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(by_length([]), [])

    def test_normal_array(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "One", "One", "Two", "Two", "Three", "Four", "Five"])

    def test_array_with_negative_numbers(self):
        self.assertEqual(by_length([1, -1, 55]), ["One", "-One", "Fifty-five"])

    def test_array_with_zero(self):
        self.assertEqual(by_length([0]), ["Zero"])

    def test_array_with_strange_numbers(self):
        self.assertEqual(by_length([1, "a", 55]), ["One", "", "Fifty-five"])

    def test_array_with_large_numbers(self):
        self.assertEqual(by_length([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"])

    def test_array_with_large_numbers_and_small_numbers(self):
        self.assertEqual(by_length([1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3]), ["One", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Two", "Three"])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty array, a normal array, an array with negative numbers, an array with zero, an array with strange numbers (non-integer values), an array with large numbers, and an array with a mix of large and small numbers.