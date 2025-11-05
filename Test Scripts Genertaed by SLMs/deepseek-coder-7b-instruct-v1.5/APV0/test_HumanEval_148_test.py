You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given Python function:


import unittest
from HumanEval_148_code import bf

class TestBF(unittest.TestCase):

    def test_correct_planet_names(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_incorrect_planet_names(self):
        self.assertEqual(bf("Earth", "Mars"), ())
        self.assertEqual(bf("Mars", "Earth"), ())
        self.assertEqual(bf("Earth", "Pluto"), ())
        self.assertEqual(bf("Pluto", "Earth"), ())

    def test_same_planet_names(self):
        self.assertEqual(bf("Earth", "Earth"), ())

if __name__ == '__main__':
    unittest.main()


This script includes three test methods:

1. `test_correct_planet_names` tests the function with correct planet names.
2. `test_incorrect_planet_names` tests the function with incorrect planet names and with the same planet name.
3. `test_same_planet_names` tests the function with the same planet name.

Each test method uses the `assertEqual` method to compare the actual output of the function with the expected output. If the actual output matches the expected output, the test passes; otherwise, the test fails.

Please note that you need to have the function `bf` defined in a file named `HumanEval_148_code.py` for this unittest script to work.