system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_155_code import even_odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


assistant

import unittest

# Importing the function we want to test
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count(self):
        # Test case 1: Negative number
        self.assertEqual(even_odd_count(-12), (1, 1))
        
        # Test case 2: Positive number
        self.assertEqual(even_odd_count(123), (1, 2))

        # Test case 3: Zero
        self.assertEqual(even_odd_count(0), (1, 0))

        # Test case 4: Single digit positive number
        self.assertEqual(even_odd_count(7), (0, 1))

        # Test case 5: Multiple digits negative number
        self.assertEqual(even_odd_count(-987654), (3, 4))

        # Test case 6: Multiple digits positive number
        self.assertEqual(even_odd_count(987654), (5, 4))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestEvenOddCount` class within the `unittest` framework, which contains several test cases using the `assertEqual` method to verify the correctness of the `even_odd_count` function. The `test_*` methods correspond to different scenarios described in the docstring of the `even_odd_count` function. If all tests pass without raising any exceptions, it indicates that the function works as expected.