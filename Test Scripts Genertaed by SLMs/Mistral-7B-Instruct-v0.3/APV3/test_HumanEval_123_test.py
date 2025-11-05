### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_123_code import get_odd_collatz
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
2. Include: from HumanEval_123_code import get_odd_collatz
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(int(n))
    return sorted(odd_collatz)

 import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_even_number(self):
        self.assertEqual(get_odd_collatz(2), [1])

    def test_simple_sequence(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_complex_sequence(self):
        self.assertEqual(get_odd_collatz(9), [1, 9, 28, 14, 7])

    def test_edge_case_small(self):
        self.assertEqual(get_odd_collatz(0), [])

    def test_edge_case_large(self):
        self.assertEqual(get_odd_collatz(1000000), [1, 9, 28, 14, 7, 22, 69, 194, 97, 193, 572, 289, 866, 433, 1300, 6501, 32503, 162514, 812571, 4062854, 20314273, 101571366, 507856831, 2539284158, 12696420793, 63482103966, 317410519831, 1587052599158, 7935262995794, 39676314978971, 198381574894855, 991907874474277, 4959539372371389, 24797696861856945, 123988484309284723, 619942421546422365, 3099712107732111827, 15498560538660559413, 77492802693302797066, 387464013466513985331, 1937320067332569926656, 9686600336662844633280, 48433001683314223166400, 242165008416571115832000, 1210825042082855579160000, 6054125210414277895840000, 30270626052071389479200000, 151353130260356947396000000, 756765651301784736980000000, 3783828256508923684900000000, 18919141282544618424500000000, 94595706412723092122500000000, 47297853206361546061250