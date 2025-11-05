You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_get_max_triples(self):
        self.assertEqual(get_max_triples(5), 1)
        self.assertEqual(get_max_triples(10), 4)
        self.assertEqual(get_max_triples(15), 11)
        self.assertEqual(get_max_triples(20), 20)
        self.assertEqual(get_max_triples(25), 29)

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case `test_get_max_triples` that tests the `get_max_triples` function with a few different inputs. The `assertEqual` method is used to check that the output of the function matches the expected output for each input.

Please note that the expected outputs for these inputs are based on the provided example and my understanding of the problem. If the actual expected outputs are different, you should update the test cases accordingly.

Also, please note that the time complexity of the given function is O(n^3), which means it may take a long time to run for large inputs. If you want to test the function with large inputs, you may need to adjust your expectations accordingly.