user

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
    return "NO"assistant

Here is the unittest test script for the `exchange` function:

import unittest
from HumanEval_110_code import exchange

class TestExchange(unittest.TestCase):
    def test_exchange_yes(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_exchange_no(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_exchange_empty_lists(self):
        with self.assertRaises(IndexError):
            exchange([], [])

    def test_exchange_single_element_lists(self):
        self.assertEqual(exchange([2], [2]), "YES")
        self.assertEqual(exchange([1], [2]), "NO")

    def test_exchange_all_odd(self):
        self.assertEqual(exchange([1, 1, 1, 1], [1, 1, 1, 1]), "NO")

    def test_exchange_all_even(self):
        self.assertEqual(exchange([2, 2, 2, 2], [2, 2, 2, 2]), "YES")

    def test_exchange_mixed_lists(self):
        self.assertEqual(exchange([1, 2, 3, 4], [2, 4, 6, 8]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 3, 5, 7]), "NO")

if __name__ == '__main__':
    unittest.main()

This test script covers a variety of scenarios, including:

* Successful exchanges where all elements in `lst1` become even
* Unsuccessful exchanges where not all elements in `lst1` can become even
* Edge cases where one or both input lists are empty
* Single-element lists
* Lists with all odd or all even elements
* Mixed lists with a mix of odd and even elements

Each test method uses the `assertEqual` method to check that the output of the `exchange` function matches the expected result. The `with self.assertRaises` block is used to test that the function raises an `IndexError` when given empty input lists.