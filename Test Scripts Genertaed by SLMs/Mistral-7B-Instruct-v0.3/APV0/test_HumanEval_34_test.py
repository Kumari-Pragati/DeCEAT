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

 Here is a simple unittest test script for the `unique` function. I've added some test cases to cover various scenarios, including an empty list, a list with duplicate elements, and a list with unique elements in a different order.


import unittest
from HumanEval_34_code import unique

class TestUniqueFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_single_element(self):
        self.assertEqual(unique([1]), [1])

    def test_duplicates(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_unique_elements_different_order(self):
        self.assertEqual(unique([123, 5, 3, 5, 2, 3, 9, 0]), [0, 2, 3, 5, 123, 9])

if __name__ == '__main__':
    unittest.main()


Save this script as `test_unique.py` and run it using the command `python test_unique.py`. The test cases will be executed, and you should see a summary of the test results at the end. If all tests pass, it means the `unique` function is working correctly.