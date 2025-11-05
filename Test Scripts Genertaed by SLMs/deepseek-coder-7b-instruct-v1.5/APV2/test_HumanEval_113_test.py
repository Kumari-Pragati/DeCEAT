You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_113_code import odd_count

class TestOddCount(unittest.TestCase):

    def test_odd_count(self):
        self.assertEqual(odd_count(['1234567']), ["the number of odd elements 4n the str4ng 4 of the 4nput."])
        self.assertEqual(odd_count(['3', "11111111"]), ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."])
        self.assertEqual(odd_count(['12345678901234567890']), ["the number of odd elements 10n the str10ng 10 of the 10nput."])
        self.assertEqual(odd_count(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']), ["the number of odd elements 5n the str5ng 5 of the 5nput."])
        self.assertEqual(odd_count(['10101010101010101010']), ["the number of odd elements 10n the str10ng 10 of the 10nput."])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios. It tests the function with a list containing a single string, a list containing multiple strings, and a list containing strings of different lengths.