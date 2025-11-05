user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_124_code import valid_date

class TestValidDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertTrue(valid_date('06-04-2020'))
        self.assertTrue(valid_date('12-31-1999'))
        self.assertTrue(valid_date('01-01-2000'))
        self.assertTrue(valid_date('02-28-2000'))
        self.assertTrue(valid_date('02-29-2000')) # leap year
        self.assertTrue(valid_date('12-31-1999'))

    def test_invalid_date(self):
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('04-0-2040'))
        self.assertFalse(valid_date('06/04/2020')) # invalid date format
        self.assertFalse(valid_date('13-12-1999')) # month out of range
        self.assertFalse(valid_date('02-30-2000')) # invalid day for february
        self.assertFalse(valid_date('02-29-1999')) # not a leap year
        self.assertFalse(valid_date('13-12-1999')) # month out of range
        self.assertFalse(valid_date('')) # empty date string
        self.assertFalse(valid_date('abc')) # invalid date format
        self.assertFalse(valid_date('02-29-2001')) # not a leap year

    def test_edge_cases(self):
        self.assertFalse(valid_date('02-29-1999')) # not a leap year
        self.assertFalse(valid_date('02-30-2000')) # invalid day for february
        self.assertFalse(valid_date('02-29-2000')) # not a leap year
        self.assertFalse(valid_date('02-29-2001')) # not a leap year
        self.assertFalse(valid_date('02-29-2002')) # not a leap year
        self.assertFalse(valid_date('02-29-2003')) # not a leap year
        self.assertFalse(valid_date('02-29-2004')) # not a leap year
        self.assertFalse(valid_date('02-29-2005')) # not a leap year
        self.assertFalse(valid_date('02-29-2006')) # not a leap year
        self.assertFalse(valid_date('02-29-2007')) # not a leap year
        self.assertFalse(valid_date('02-29-2008')) # leap year
        self.assertFalse(valid_date('02-29-2009')) # not a leap year
        self.assertFalse(valid_date('02-29-2010')) # leap year
        self.assertFalse(valid_date('02-29-2011')) # not a leap year
        self.assertFalse(valid_date('02-29-2012')) # leap year
        self.assertFalse(valid_date('02-29-2013')) # not a leap year
        self.assertFalse(valid_date('02-29-2014')) # leap year
        self.assertFalse(valid_date('02-29-2015')) # not a leap year
        self.assertFalse(valid_date('02-29-2016')) # leap year
        self.assertFalse(valid_date('02-29-2017')) # not a leap year
        self.assertFalse(valid_date('02-29-2018')) # leap year
        self.assertFalse(valid_date('02-29-2019')) # not a leap year
        self.assertFalse(valid_date('02-29-2020')) # leap year
        self.assertFalse(valid_date('02-29-2021')) # not a leap year
        self.assertFalse(valid_date('02-29-2022')) # leap year
        self.assertFalse(valid_date('02-29-2023')) # not a leap year
        self.assertFalse(valid_date('02-29-2024')) # leap year
        self.assertFalse(valid_date('02-29-2025')) # not a leap year
        self.assertFalse(valid_date('02-29-2026')) # leap year
        self.assertFalse(valid_date('02-29-2027')) # not a leap year
        self.assertFalse(valid_date('02-29-2028')) # leap year
        self.assertFalse(valid_date('02-29-2029')) # not a leap year
        self.assertFalse(valid_date('02-29-2030')) # leap year
        self.assertFalse(valid_date('02-29-2031')) # not a leap year
        self.assertFalse(valid_date('02-29-2032')) # leap year
        self.assertFalse(valid_date('02-29-2033')) # not a leap year
        self.assertFalse(valid_date('02-29-2034')) # leap year
        self.assertFalse(valid_date('02-29-2035')) # not a leap year
        self.assertFalse(valid_date('02-29-2036