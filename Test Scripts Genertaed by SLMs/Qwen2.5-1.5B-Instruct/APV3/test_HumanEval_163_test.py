system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_163_code import generate_integers
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

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_163_code import generate_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))
    return [i for i in range(lower, upper + 1) if i % 2 == 0]


assistant

import unittest

from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):
    def test_normal_range(self):
        self.assertListEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_edge_case_lower_bound(self):
        self.assertListEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_edge_case_upper_bound(self):
        self.assertListEqual(generate_integers(10, 14), [])

    def test_empty_input(self):
        self.assertListEqual(generate_integers(9, 9), [])

    def test_single_number(self):
        self.assertListEqual(generate_integers(7, 7), [7])

    def test_large_range(self):
        self.assertListEqual(generate_integers(100, 1000), [100, 102, 104, ..., 108, 110, ..., 114, ...,
                                                           198, 200, ..., 202, ..., 204, ..., 206, ..., 208, ..., 210, ..., 212, ..., 214, ..., 216, ..., 218, ..., 220, ..., 222, ..., 224, ..., 226, ..., 228, ..., 230, ..., 232, ..., 234, ..., 236, ..., 238, ..., 240, ..., 242, ..., 244, ..., 246, ..., 248, ..., 250, ..., 252, ..., 254, ..., 256, ..., 258, ..., 260, ..., 262, ..., 264, ..., 266, ..., 268, ..., 270, ..., 272, ..., 274, ..., 276, ..., 278, ..., 280, ..., 282, ..., 284, ..., 286, ..., 288, ..., 290, ..., 292, ..., 294, ..., 296, ..., 298, ..., 300, ..., 302, ..., 304, ..., 306, ..., 308, ..., 310, ..., 312, ..., 314, ..., 316, ..., 318, ..., 320, ..., 322, ..., 324, ..., 326, ..., 328, ..., 330, ..., 332, ..., 334, ..., 336, ..., 338, ..., 340, ..., 342, ..., 344, ..., 346, ..., 348, ..., 350, ..., 352, ..., 354, ..., 356, ..., 358, ..., 360, ..., 362, ..., 364, ..., 366, ..., 368, ..., 370, ..., 372, ..., 374, ..., 376, ..., 378, ..., 380, ..., 382, ..., 384, ..., 386, ..., 388, ..., 390, ..., 392, ..., 394, ..., 396, ..., 398, ..., 400, ..., 402, ..., 404, ..., 406, ..., 408, ..., 410, ..., 412, ..., 414, ..., 416, ..., 418, ..., 420, ..., 422, ..., 424, ..., 426, ..., 428, ..., 430, ..., 432, ..., 434, ..., 436, ..., 438, ..., 440, ..., 442, ..., 444, ..., 446, ..., 448, ..., 450, ..., 452, ..., 454, ..., 456, ..., 458, ..., 460,