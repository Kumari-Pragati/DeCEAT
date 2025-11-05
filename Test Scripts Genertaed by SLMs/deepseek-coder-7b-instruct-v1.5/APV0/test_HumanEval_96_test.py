You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_96_code import count_up_to
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    For example:
    count_up_to(5) => [2, 3]
    count_up_to(11) => [2, 3, 5, 7]
    count_up_to(0) => []
    count_up_to(20) => [2, 3, 5, 7, 11, 13, 17, 19]
    count_up_to(1) => []
    count_up_to(18) => [2, 3, 5, 7, 11, 13, 17]
    """

    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_96_code import count_up_to

class TestCountUpTo(unittest.TestCase):
    def test_count_up_to(self):
        self.assertEqual(count_up_to(5), [2, 3])
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])
        self.assertEqual(count_up_to(0), [])
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(count_up_to(1), [])
        self.assertEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])

if __name__ == '__main__':
    unittest.main()


This script creates a test case class `TestCountUpTo` that inherits from `unittest.TestCase`. It defines a method `test_count_up_to` that checks if the `count_up_to` function returns the expected output for each input. The `unittest.main()` at the end is used to run the tests when the script is run directly.

Please note that the `count_up_to` function can be optimized by checking divisibility up to the square root of `i` instead of `i` itself, as a larger factor of the number would be a multiple of smaller factor that has already been checked. However, this optimization is not included in the test script.