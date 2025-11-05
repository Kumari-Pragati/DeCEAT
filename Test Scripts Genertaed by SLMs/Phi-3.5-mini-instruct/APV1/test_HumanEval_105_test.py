You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_105_code import by_length

class TestByLength(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(by_length([]), [])

    def test_single_digit_numbers(self):
        self.assertEqual(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]), ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"])

    def test_single_digit_number_with_negatives(self):
        self.assertEqual(by_length([1, -1, 55]), ["One"])

    def test_multiple_same_digit_numbers(self):
        self.assertEqual(by_length([2, 2, 2, 2]), ["Two", "Two", "Two", "Two"])

    def test_mixed_numbers(self):
        self.assertEqual(by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]), ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"])

    def test_numbers_outside_1_to_9(self):
        self.assertEqual(by_length([0, 10, 11, 12]), [])

    def test_mixed_integers(self):
        self.assertEqual(by_length([2, 3, 4, 5, 6, 7, 8, 9, 0, -1, 11]), ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"])

    def test_empty_string(self):
        self.assertEqual(by_length(""), [])

    def test_non_integer_values(self):
        self.assertEqual(by_length(["a", "b", "c"]), [])

if __name__ == '__main__':
    unittest.main()