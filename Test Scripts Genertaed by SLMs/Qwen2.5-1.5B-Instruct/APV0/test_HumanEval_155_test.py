system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Test cases to verify the correctness of the even_odd_count function
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

        # Test case 5: Multiple digits positive number
        self.assertEqual(even_odd_count(88690), (3, 2))

        # Test case 6: Large negative number
        self.assertEqual(even_odd_count(-123456789), (5, 4))

        # Test case 7: Mixed numbers
        self.assertEqual(even_odd_count(1234567890), (5, 4))

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` module and defines a class `TestEvenOddCount` which inherits from `unittest.TestCase`. It contains multiple test methods (`test_even_odd_count`) to ensure the `even_odd_count` function behaves as expected across various scenarios including negative numbers, zero, single-digit numbers, large numbers, mixed numbers, etc. The `assertEqual` method is used to compare the output of the function against the expected results. Finally, the `unittest.main()` call runs all the defined tests when executed.