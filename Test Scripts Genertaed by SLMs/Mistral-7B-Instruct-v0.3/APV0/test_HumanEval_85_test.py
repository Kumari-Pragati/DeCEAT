Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the given Python function:


import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([2, 4, 6, 8]), 4)
        self.assertEqual(add([1, 3, 5, 7]), 0)
        self.assertEqual(add([0, 2, 4, 6]), 2)
        self.assertEqual(add([-2, -4, -6, -8]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10]), 6)
        self.assertEqual(add([]), 0)
        self.assertEqual(add([1]), 0)
        self.assertEqual(add([2, 2]), 2)

if __name__ == '__main__':
    unittest.main()


This test script includes multiple test cases for the `add` function, covering various scenarios such as empty lists, lists with only even or odd numbers, and lists with a mix of even and odd numbers. The test cases use the `assertEqual` method to verify the expected and actual outputs.