user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_71_code import triangle_area
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1.
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.

    Example:
        triangle_area(3, 4, 5) == 6.00
        triangle_area(1, 2, 10) == -1
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return areaassistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_zero_sides(self):
        self.assertEqual(triangle_area(0, 0, 0), -1)

    def test_negative_sides(self):
        self.assertEqual(triangle_area(-1, 2, 3), -1)

    def test_non_integer_sides(self):
        self.assertEqual(triangle_area(1.5, 2.5, 3.5), 2.5)

    def test_sides_with_decimal_points(self):
        self.assertEqual(triangle_area(1.0, 2.0, 3.0), 2.5)

    def test_sides_with_large_values(self):
        self.assertEqual(triangle_area(1000, 2000, 3000), 4166.67)

if __name__ == '__main__':
    unittest.main()


This test script includes test cases for valid and invalid triangles, zero sides, negative sides, non-integer sides, sides with decimal points, and sides with large values.