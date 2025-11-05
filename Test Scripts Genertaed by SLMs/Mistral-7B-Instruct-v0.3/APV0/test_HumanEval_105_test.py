Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the provided function `by_length`. The script tests various edge cases and ensures the function behaves as expected.


import unittest
from HumanEval_105_code import by_length

class TestByLength(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(by_length([]), [])

    def test_array_with_only_strange_numbers(self):
        self.assertEqual(by_length([1, -1, 55]), ['One'])

    def test_array_with_only_valid_numbers(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])

    def test_array_with_mixed_valid_and_strange_numbers(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3, 100]), ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

1. An empty array
2. An array with only strange numbers
3. An array with only valid numbers
4. An array with mixed valid and strange numbers

You can run this script directly by saving it as a .py file and running it from the command line using the command `python filename.py`.