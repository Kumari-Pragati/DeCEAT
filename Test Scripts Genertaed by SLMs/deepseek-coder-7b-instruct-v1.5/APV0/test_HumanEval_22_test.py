You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_22_code import filter_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any Python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
        self.assertEqual(filter_integers([1, 'two', 3, 'four', 5]), [1, 3, 5])
        self.assertEqual(filter_integers([1, 2.0, 3, 4.5, 5]), [1, 3, 5])
        self.assertEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(filter_integers([]), [])

if __name__ == '__main__':
    unittest.main()


This script creates a unittest test case class `TestFilterIntegers` with a single test method `test_filter_integers`. This method tests the `filter_integers` function with various input lists and checks if the output matches the expected result.

The `unittest.main()` at the end is used to run the test case. If you run this script, it will execute the test and print the result.

Please note that you need to replace `from HumanEval_22_code import filter_integers` with the actual location of your `filter_integers` function if it's not in the same file.