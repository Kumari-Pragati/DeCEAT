You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_26_code import remove_duplicates
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


### Response:
Here is the unittest script for the given Python function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestRemoveDuplicates` that inherits from `unittest.TestCase`. It includes a method `test_remove_duplicates` that tests the `remove_duplicates` function with various inputs and expected outputs. The `unittest.main()` at the end runs these tests when the script is run directly.

Please note that this script assumes that the `remove_duplicates` function is defined in a file named `HumanEval_26_code.py` in the same directory as the unittest script. If the function is defined in a different file, you will need to adjust the import statement accordingly.