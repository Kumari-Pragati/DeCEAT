You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_136_code import largest_smallest_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_136_code import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(largest_smallest_integers([]), (None, None))

    def test_zero_list(self):
        self.assertEqual(largest_smallest_integers([0]), (None, None))

    def test_positive_list(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_negative_list(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (None, None))

    def test_mixed_list(self):
        self.assertEqual(largest_smallest_integers([-2, 4, -1, 3, 5, -7]), (-1, 3))

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestLargestSmallestIntegers` that tests the `largest_smallest_integers` function with different types of inputs. Each test method corresponds to a specific scenario.

The `unittest.main()` at the end makes the script runnable directly, which will execute all test methods in the class.

Please note that you need to have the `HumanEval_136_code` module and its `largest_smallest_integers` function available in your environment for this script to work.