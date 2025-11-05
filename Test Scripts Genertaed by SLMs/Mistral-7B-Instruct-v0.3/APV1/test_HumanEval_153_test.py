You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_153_code import Strongest_Extension

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans

 Here is a comprehensive unittest test suite for the given Python function `Strongest_Extension`.


import unittest
from HumanEval_153_code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Strongest_Extension('my_class', []), 'my_class.None')

    def test_single_extension(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA']), 'my_class.AA')
        self.assertEqual(Strongest_Extension('my_class', ['aa']), 'my_class.aa')
        self.assertEqual(Strongest_Extension('my_class', ['A1']), 'my_class.A1')
        self.assertEqual(Strongest_Extension('my_class', ['1A']), 'my_class.1A')

    def test_multiple_extensions(self):
        self.assertEqual(Strongest_Extension('my_class', ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'my_class.SErviNGSliCes')
        self.assertEqual(Strongest_Extension('my_class', ['Beef', 'Pork', 'Chicken']), 'my_class.Beef')
        self.assertEqual(Strongest_Extension('my_class', ['beef', 'pork', 'chicken']), 'my_class.beef')
        self.assertEqual(Strongest_Extension('my_class', ['CC', 'BB', 'AA']), 'my_class.AA')
        self.assertEqual(Strongest_Extension('my_class', ['cc', 'bb', 'aa']), 'my_class.aa')

    def test_same_strength(self):
        self.assertEqual(Strongest_Extension('my_class', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Cheese']), 'my_class.SErviNGSliCes')
        self.assertEqual(Strongest_Extension('my_class', ['Beef', 'Pork', 'Chicken', 'Pork']), 'my_class.Beef')

    def test_no_uppercase_letters(self):
        self.assertEqual(Strongest_Extension('my_class', ['1', '2', '3']), 'my_class.1')

    def test_no_lowercase_letters(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'BB', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as empty list, single extension, multiple extensions with different strengths, multiple extensions with the same strength, no uppercase letters, and no lowercase letters.