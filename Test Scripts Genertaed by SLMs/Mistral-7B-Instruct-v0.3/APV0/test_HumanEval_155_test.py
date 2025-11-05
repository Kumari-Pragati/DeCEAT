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

 Here is a unittest test script for the `even_odd_count` function:


import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):
    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(1), (0, 1))
        self.assertEqual(even_odd_count(2), (1, 1))
        self.assertEqual(even_odd_count(3), (0, 1))
        self.assertEqual(even_odd_count(10), (2, 2))
        self.assertEqual(even_odd_count(12), (1, 2))
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-123), (0, 3))
        self.assertEqual(even_odd_count(-1000), (3, 0))

if __name__ == '__main__':
    unittest.main()


This script includes a test case class `TestEvenOddCount` that tests the `even_odd_count` function with various inputs. The test cases cover positive and negative numbers, as well as numbers with different amounts of even and odd digits. The test cases use the `assertEqual` method to check if the output of the `even_odd_count` function matches the expected output.

The script starts with `import unittest`, includes the `even_odd_count` function from the provided code, and ends with `if __name__ == '__main__': unittest.main()`. When run, this script will execute the test cases and print the results.