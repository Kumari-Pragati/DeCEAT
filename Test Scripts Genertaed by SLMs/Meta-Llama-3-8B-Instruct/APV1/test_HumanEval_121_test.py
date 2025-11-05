user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5]), 9)
        self.assertEqual(solution([10, 20, 30, 40, 50]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9]), 15)
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9)
        self.assertEqual(solution([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure the function is working correctly. The test cases cover different scenarios, such as lists with odd and even numbers, lists with only odd numbers, lists with only even numbers, and lists with a mix of odd and even numbers.