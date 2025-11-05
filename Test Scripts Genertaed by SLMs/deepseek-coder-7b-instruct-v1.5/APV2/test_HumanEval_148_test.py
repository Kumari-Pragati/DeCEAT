You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_148_code import bf
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return planet_names[planet1_index + 1: planet2_index]
    else:
        return planet_names[planet2_index + 1: planet1_index]


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_148_code import bf

class TestBF(unittest.TestCase):
    def test_valid_planets(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_invalid_planets(self):
        self.assertEqual(bf("Invalid", "Planet"), ())
        self.assertEqual(bf("Jupiter", "Invalid"), ())
        self.assertEqual(bf("Invalid", "Uranus"), ())

    def test_same_planet(self):
        self.assertEqual(bf("Mercury", "Mercury"), ())

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_valid_planets`: This test case checks the function's output when given valid planet names.
2. `test_invalid_planets`: This test case checks the function's output when given invalid planet names.
3. `test_same_planet`: This test case checks the function's output when given the same planet name twice.

Each test case uses the `assertEqual` method to compare the function's output to the expected output. If the function's output matches the expected output, the test case passes. If the function's output does not match the expected output, the test case fails.