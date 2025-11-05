Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_113_code import odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3', "11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """

    res = []
    for arr in lst:
        n = sum(int(d) % 2 == 1 for d in arr)
        res.append(
            "the number of odd elements "
            + str(n)
            + "n the str"
            + str(n)
            + "ng "
            + str(n)
            + " of the "
            + str(n)
            + "nput."
        )
    return res

 Here is a unittest test script for the `odd_count` function:


import unittest
from HumanEval_113_code import odd_count

class TestOddCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(odd_count([]), [])

    def test_single_element_list(self):
        self.assertEqual(
            odd_count(['1234567']),
            ["the number of odd elements 4n the str4ng 4 of the 4nput."]
        )

    def test_multiple_elements_list(self):
        self.assertEqual(
            odd_count(['3', "11111111"]),
            ["the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 8n the str8ng 8 of the 8nput."]
        )

    def test_mixed_odd_and_even_elements_list(self):
        self.assertEqual(
            odd_count(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']),
            ["the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 0n the str0ng 0 of the 0nput.",
             "the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 0n the str0ng 0 of the 0nput.",
             "the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 0n the str0ng 0 of the 0nput.",
             "the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 0n the str0ng 0 of the 0nput."]
        )

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, a single-element list, a list with multiple elements containing only odd or even numbers, and a list with mixed odd and even numbers. The test cases use the `assertEqual` method to compare the expected output with the actual output produced by the `odd_count` function.