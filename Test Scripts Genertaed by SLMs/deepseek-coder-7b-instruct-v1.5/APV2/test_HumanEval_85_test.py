You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_85_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_add_negative(self):
        self.assertEqual(add([4, 3, 6, 7]), 6)

    def test_add_empty(self):
        self.assertEqual(add([]), 0)

    def test_add_single_element(self):
        self.assertEqual(add([1]), 0)

    def test_add_all_even(self):
        self.assertEqual(add([2, 4, 6, 8]), 4)

    def test_add_all_odd(self):
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_add_mixed(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios, including positive numbers, negative numbers, empty list, single element list, all even numbers, all odd numbers, and a mixed list of numbers. The tests check if the function returns the correct sum of even numbers at odd indices.