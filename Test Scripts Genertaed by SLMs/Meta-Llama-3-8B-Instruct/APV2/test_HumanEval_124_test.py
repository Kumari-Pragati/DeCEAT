system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_124_code import valid_date
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True
    valid_date('15-01-2012') => False
    valid_date('04-0-2040') => False
    valid_date('06-04-2020') => True
    valid_date('06/04/2020') => False
    """
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
            return False
        if month in [4, 6, 9, 11] and (day < 1 or day > 30):
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
    except:
        return False
    return Trueassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_124_code import valid_date

class TestValidDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('04-0-2040'))
        self.assertTrue(valid_date('06-04-2020'))
        self.assertFalse(valid_date('06/04/2020'))
        self.assertFalse(valid_date(''))
        self.assertFalse(valid_date('12-31-2020'))
        self.assertFalse(valid_date('13-31-2020'))
        self.assertFalse(valid_date('02-29-2020'))
        self.assertFalse(valid_date('02-30-2020'))
        self.assertFalse(valid_date('02-31-2020'))
        self.assertFalse(valid_date('13-30-2020'))
        self.assertFalse(valid_date('02-0-2020'))
        self.assertFalse(valid_date('02-32-2020'))
        self.assertFalse(valid_date('02-29-2021'))
        self.assertFalse(valid_date('02-29-2022'))
        self.assertFalse(valid_date('02-29-2023'))
        self.assertFalse(valid_date('02-29-2024'))
        self.assertFalse(valid_date('02-29-2025'))
        self.assertFalse(valid_date('02-29-2026'))
        self.assertFalse(valid_date('02-29-2027'))
        self.assertFalse(valid_date('02-29-2028'))
        self.assertFalse(valid_date('02-29-2029'))
        self.assertFalse(valid_date('02-29-2030'))
        self.assertFalse(valid_date('02-29-2031'))
        self.assertFalse(valid_date('02-29-2032'))
        self.assertFalse(valid_date('02-29-2033'))
        self.assertFalse(valid_date('02-29-2034'))
        self.assertFalse(valid_date('02-29-2035'))
        self.assertFalse(valid_date('02-29-2036'))
        self.assertFalse(valid_date('02-29-2037'))
        self.assertFalse(valid_date('02-29-2038'))
        self.assertFalse(valid_date('02-29-2039'))
        self.assertFalse(valid_date('02-29-2040'))
        self.assertFalse(valid_date('02-29-2041'))
        self.assertFalse(valid_date('02-29-2042'))
        self.assertFalse(valid_date('02-29-2043'))
        self.assertFalse(valid_date('02-29-2044'))
        self.assertFalse(valid_date('02-29-2045'))
        self.assertFalse(valid_date('02-29-2046'))
        self.assertFalse(valid_date('02-29-2047'))
        self.assertFalse(valid_date('02-29-2048'))
        self.assertFalse(valid_date('02-29-2049'))
        self.assertFalse(valid_date('02-29-2050'))
        self.assertFalse(valid_date('02-29-2051'))
        self.assertFalse(valid_date('02-29-2052'))
        self.assertFalse(valid_date('02-29-2053'))
        self.assertFalse(valid_date('02-29-2054'))
        self.assertFalse(valid_date('02-29-2055'))
        self.assertFalse(valid_date('02-29-2056'))
        self.assertFalse(valid_date('02-29-2057'))
        self.assertFalse(valid_date('02-29-2058'))
        self.assertFalse(valid_date('02-29-2059'))
        self.assertFalse(valid_date('02-29-2060'))
        self.assertFalse(valid_date('02-29-2061'))
        self.assertFalse(valid_date('02-29-2062'))
        self.assertFalse(valid_date('02-29-2063'))
        self.assertFalse(valid_date('02-29-2064'))
        self.assertFalse(valid_date('02-29-2065'))
        self.assertFalse(valid_date('02-29-2066'))
        self.assertFalse(valid_date('02-29-2067'))
        self.assertFalse(valid_date('02-29-2068'))
        self.assertFalse(valid_date('02-29-2069'))
        self.assertFalse(valid_date('02-29-2070'))
        self.assertFalse(valid_date('02-29-2071'))
        self.assertFalse(valid_date('02-29-2072'))
        self.assertFalse(valid_date('02-29-2073'))
        self.assertFalse(valid_date('02-29-2074'))
        self.assertFalse(valid_date('02-29-2075'))
        self.assertFalse(valid_date('02-29-2076'))
        self.assertFalse(valid_date('02-29-2077'))
        self.assertFalse(valid_date('02-29-2078'))
        self.assertFalse(valid_date('02-29-2079'))
        self.assertFalse(valid_date('02-29-2080'))
        self.assertFalse(valid_date('02-29-2081'))
        self.assertFalse(valid_date('02-29-2082