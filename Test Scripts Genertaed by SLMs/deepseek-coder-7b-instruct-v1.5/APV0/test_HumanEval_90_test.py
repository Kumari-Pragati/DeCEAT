You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_90_code import next_smallest
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_90_code import next_smallest

class TestNextSmallest(unittest.TestCase):
    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertIsNone(next_smallest([]))
        self.assertIsNone(next_smallest([1, 1]))
        self.assertEqual(next_smallest([1, 2, 2, 3]), 2)
        self.assertEqual(next_smallest([10, 20, 30, 40, 50]), 20)
        self.assertIsNone(next_smallest([10, 10, 10, 10]))
        self.assertEqual(next_smallest([1, 2, 3, 4, 5, 6]), 2)
        self.assertIsNone(next_smallest([1, 1, 1, 1, 1]))

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestNextSmallest` that inherits from `unittest.TestCase`. Inside this class, we define a method `test_next_smallest` that tests the `next_smallest` function with different inputs. Each `self.assertEqual` call checks if the output of `next_smallest` is as expected, and each `self.assertIsNone` call checks if `next_smallest` returns `None` as expected.

Finally, the script ends with `unittest.main()`, which runs all the tests when the script is run directly.