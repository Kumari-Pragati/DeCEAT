You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_34_code import unique
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):

    def test_unique_elements(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_single_element_list(self):
        self.assertEqual(unique([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(unique([1, 1, 1, 1]), [1])

    def test_sorted_list(self):
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(unique([5, 3, 2, 9, 0]), [0, 2, 3, 5, 9])

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure that the `unique` function is working as expected. It tests with a list of unique elements, an empty list, a list with a single element, a list with all the same elements, a sorted list, and an unsorted list.

Please note that you need to have the `HumanEval_34_code` module available in your environment, and the `unique` function should be defined in that module. If the `unique` function is defined in a different module, you should replace `HumanEval_34_code` with the correct module name.