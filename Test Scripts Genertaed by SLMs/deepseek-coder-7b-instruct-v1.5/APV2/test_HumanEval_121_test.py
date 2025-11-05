You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_121_code import solution
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5]), 3)
        self.assertEqual(solution([10, 20, 30, 40, 50]), 0)
        self.assertEqual(solution([-1, -2, -3, -4, -5]), -3)
        self.assertEqual(solution([0, 0, 0, 0, 0]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9]), 15)
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for a variety of different cases, including both positive and negative numbers, as well as even and odd numbers. It also tests the function with a list of all odd numbers, all even numbers, and a list with no odd numbers.