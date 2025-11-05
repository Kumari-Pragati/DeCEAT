You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_147_code import get_max_triples

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    A = [i * i - i + 1 for i in range(1, n + 1)]
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    ans += [(A[i], A[j], A[k])]
    return len(ans)

 Here is a comprehensive unittest test suite for the given Python function `get_max_triples`. I've included several test cases to cover various scenarios.


import unittest
from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_get_max_triples_1(self):
        n = 1
        expected_output = 0
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_2(self):
        n = 2
        expected_output = 0
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_3(self):
        n = 3
        expected_output = 0
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_4(self):
        n = 4
        expected_output = 0
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_5(self):
        n = 5
        expected_output = 1
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_6(self):
        n = 6
        expected_output = 1
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_7(self):
        n = 7
        expected_output = 0
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_8(self):
        n = 8
        expected_output = 1
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_9(self):
        n = 9
        expected_output = 0
        self.assertEqual(get_max_triples(n), expected_output)

    def test_get_max_triples_10(self):
        n = 10
        expected_output = 1
        self.assertEqual(get_max_triples(n), expected_output)

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for various input sizes, including the example provided in the function description. It checks if the function returns the expected output for each test case.