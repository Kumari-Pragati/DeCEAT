Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_110_code import exchange
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    odd = 0
    even = 0
    for i in lst1:
        if i % 2 == 1:
            odd += 1
    for i in lst2:
        if i % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"

 Here is a unittest test script for the `exchange` function:


import unittest
from HumanEval_110_code import exchange

class TestExchangeFunction(unittest.TestCase):

    def test_exchange_same_lists(self):
        self.assertEqual(exchange([2, 4, 6, 8], [2, 4, 6, 8]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "NO")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 6]), "YES")

    def test_exchange_different_lists(self):
        self.assertEqual(exchange([1, 2, 3, 4], [5, 6, 7, 8]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [5, 6, 7, 9]), "NO")
        self.assertEqual(exchange([1, 2, 3, 4], [5, 6, 7, 0]), "YES")

if __name__ == '__main__':
    unittest.main()


This test script includes two test cases: `test_exchange_same_lists` and `test_exchange_different_lists`. The first test case checks the function behavior when the two input lists are the same, and the second test case checks the function behavior when the two input lists are different. Each test case includes several examples to ensure that the function works correctly for various inputs.