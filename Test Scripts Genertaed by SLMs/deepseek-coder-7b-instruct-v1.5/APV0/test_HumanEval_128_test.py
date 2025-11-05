You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_128_code import prod_signs
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)
        self.assertEqual(prod_signs([-1, -2, -3]), -6)
        self.assertEqual(prod_signs([1, -2, 3]), 6)
        self.assertEqual(prod_signs([0, -1, 2]), 2)
        self.assertEqual(prod_signs([-1, 0, 2]), 2)
        self.assertEqual(prod_signs([1, 2, 3, 4, 5]), 30)
        self.assertEqual(prod_signs([-1, -2, -3, -4, -5]), -30)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestProdSigns` that inherits from `unittest.TestCase`. It includes a method `test_prod_signs` that tests the `prod_signs` function with various inputs. The `unittest.main()` at the end makes this script runnable directly.

Please note that you need to replace `HumanEval_128_code` with the actual Python file where the `prod_signs` function is defined.