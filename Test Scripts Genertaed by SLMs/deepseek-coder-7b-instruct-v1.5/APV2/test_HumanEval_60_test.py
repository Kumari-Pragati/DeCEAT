You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_60_code import sum_to_n
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n + 1))


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case, `test_sum_to_n`, which tests the `sum_to_n` function with a variety of inputs. Each test case checks that the output of `sum_to_n` matches the expected result.

The `unittest.main()` call at the end of the script will run all the test cases when the script is executed.

Please note that the `HumanEval_60_code` module should contain the `sum_to_n` function for this test suite to work. If the function is defined in a different module, you should replace `HumanEval_60_code` with the correct module name.