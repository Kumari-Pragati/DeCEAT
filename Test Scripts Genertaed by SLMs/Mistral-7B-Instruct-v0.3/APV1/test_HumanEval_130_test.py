You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_130_code import tri

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri

 Here is a simple unittest test suite for the given Python function `tri`. The test suite checks the function's behavior for various input values.


import unittest
from HumanEval_130_code import tri

class TestTribonacci(unittest.TestCase):
    def test_tri_0(self):
        self.assertEqual(tri(0), [1])

    def test_tri_1(self):
        self.assertEqual(tri(1), [1, 3])

    def test_tri_2(self):
        self.assertEqual(tri(2), [1, 3, 2])

    def test_tri_3(self):
        self.assertEqual(tri(3), [1, 3, 2, 8])

    def test_tri_4(self):
        self.assertEqual(tri(4), [1, 3, 2, 8, 13])

    def test_tri_5(self):
        self.assertEqual(tri(5), [1, 3, 2, 8, 13, 21])

    def test_tri_6(self):
        self.assertEqual(tri(6), [1, 3, 2, 8, 13, 21, 38])

    def test_tri_7(self):
        self.assertEqual(tri(7), [1, 3, 2, 8, 13, 21, 38, 65])

    def test_tri_8(self):
        self.assertEqual(tri(8), [1, 3, 2, 8, 13, 21, 38, 65, 109])

if __name__ == '__main__':
    unittest.main()


This test suite checks the function's behavior for input values ranging from 0 to 8. You can add more test cases to cover other input values if needed.