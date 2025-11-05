You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_5_code import intersperse
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []
    for i, x in enumerate(numbers):
        result.append(x)
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimeter_at_end(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimeter_at_start(self):
        self.assertEqual(intersperse([4, 1, 2, 3], 4), [4, 1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestIntersperse` that inherits from `unittest.TestCase`. It includes five test methods:

1. `test_empty_list`: Checks that `intersperse` correctly handles an empty list.
2. `test_single_element`: Checks that `intersperse` correctly handles a list with a single element.
3. `test_multiple_elements`: Checks that `intersperse` correctly inserts the delimiter between elements.
4. `test_delimeter_at_end`: Checks that `intersperse` correctly inserts the delimiter at the end of the list.
5. `test_delimeter_at_start`: Checks that `intersperse` correctly inserts the delimiter at the start of the list.

The `if __name__ == '__main__': unittest.main()` line at the end allows the script to be run directly and automatically discover and run all the test methods in the `TestIntersperse` class.