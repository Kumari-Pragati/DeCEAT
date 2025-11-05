### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_96_code import count_up_to
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()


### Immediate Task
Write the complete unittest test suite for the following Python function.

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

 import unittest
from HumanEval_96_code import count_up_to

class TestCountUpTo(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_up_to(5), [2, 3])
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])

    def test_zero(self):
        self.assertEqual(count_up_to(0), [])

    def test_negative_numbers(self):
        self.assertEqual(count_up_to(-1), [])

    def test_one(self):
        self.assertEqual(count_up_to(1), [])

    def test_edge_cases(self):
        self.assertEqual(count_up_to(2), [2])
        self.assertEqual(count_up_to(4), [2])
        self.assertEqual(count_up_to(6), [2, 3])
        self.assertEqual(count_up_to(8), [2, 3])
        self.assertEqual(count_up_to(9), [2, 3])
        self.assertEqual(count_up_to(10), [2, 3, 5])
        self.assertEqual(count_up_to(12), [2, 3, 5])
        self.assertEqual(count_up_to(13), [2, 3, 5])
        self.assertEqual(count_up_to(14), [2, 3, 5])
        self.assertEqual(count_up_to(15), [2, 3, 5])
        self.assertEqual(count_up_to(16), [2, 3, 5])
        self.assertEqual(count_up_to(17), [2, 3, 5, 7])
        self.assertEqual(count_up_to(18), [2, 3, 5, 7])
        self.assertEqual(count_up_to(19), [2, 3, 5, 7])
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11])
        self.assertEqual(count_up_to(21), [2, 3, 5, 7, 11])
        self.assertEqual(count_up_to(22), [2, 3, 5, 7, 11])
        self.assertEqual(count_up_to(23), [2, 3, 5, 7, 11])
        self.assertEqual(count_up_to(24), [2, 3, 5, 7, 11])
        self.assertEqual(count_up_to(25), [2, 3, 5, 7, 11, 13])
        self.assertEqual(count_up_to(26), [2, 3, 5, 7, 11, 13])
        self.assertEqual(count_up_to(27), [2, 3, 5, 7, 11, 13])
        self.assertEqual(count_up_to(28), [2, 3, 5, 7, 11, 13])
        self.assertEqual(count_up_to(29), [2, 3, 5, 7, 11, 13])
        self.assertEqual(count_up_to(30), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(count_up_to(31), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(count_up_to(32), [2, 3, 5, 7, 11,