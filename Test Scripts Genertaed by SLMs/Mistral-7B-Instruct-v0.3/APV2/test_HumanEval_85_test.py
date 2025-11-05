You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the given Python function `add()`. I've included test cases that cover various scenarios, including an empty list, an odd number of elements, and negative numbers.


import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(add([]), 0)

    def test_single_even_element(self):
        self.assertEqual(add([2]), 2)

    def test_multiple_even_elements(self):
        self.assertEqual(add([2, 4, 6]), 6)

    def test_single_odd_element(self):
        self.assertEqual(add([1]), 0)

    def test_multiple_odd_elements(self):
        self.assertEqual(add([1, 3, 5]), 0)

    def test_mixed_even_and_odd_elements(self):
        self.assertEqual(add([2, 4, 6, 1, 3, 5]), 6)

    def test_negative_numbers(self):
        self.assertEqual(add([-2, -4, -6]), 0)

    def test_long_list(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for various scenarios, including an empty list, single even and odd elements, multiple even and odd elements, mixed even and odd elements, negative numbers, and a long list. It uses the `unittest.TestCase` class to define test methods, and the `unittest.main()` function to run the tests.