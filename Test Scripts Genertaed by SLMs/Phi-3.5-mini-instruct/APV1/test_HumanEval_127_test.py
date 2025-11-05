You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_127_code import intersection
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".

    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    def is_prime(num):
        if num == 1 or num == 0:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0 and is_prime(length):
        return "YES"
    return "NO"

 import unittest
from HumanEval_127_code import intersection

class TestIntersection(unittest.TestCase):

    def test_no_intersection(self):
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")

    def test_length_not_prime(self):
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_length_prime(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_length_zero(self):
        self.assertEqual(intersection((1, 1), (2, 2)), "NO")

    def test_length_negative(self):
        self.assertEqual(intersection((-2, -1), (-1, 0)), "NO")

    def test_length_one(self):
        self.assertEqual(intersection((0, 1), (1, 2)), "NO")

    def test_length_two(self):
        self.assertEqual(intersection((0, 2), (1, 3)), "NO")

    def test_length_three(self):
        self.assertEqual(intersection((0, 3), (2, 5)), "NO")

    def test_length_five(self):
        self.assertEqual(intersection((0, 5), (4, 6)), "NO")

    def test_length_seven(self):
        self.assertEqual(intersection((0, 7), (3, 8)), "YES")

    def test_length_eleven(self):
        self.assertEqual(intersection((0, 11), (5, 12)), "YES")

if __name__ == '__main__':
    unittest.main()