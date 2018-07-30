import unittest

from app.age_calculator import ageCalculator

""" These tests are for the age calculator"""
class TestAge_calculator(unittest.TestCase):

    """This test makes sure once someone enters a string and its coverted into an int an age value is returned"""
    def test_string_to_integer_is_accepted(self):
        birth_year = '1990'
        self.assertEqual(ageCalculator(int(birth_year)), 28)

    """This test makes sure that the function calculates age"""
    def test_correct_age_is_calculated(self):
        birth_year = 1990
        assert ageCalculator(birth_year) == 28

    """This test makes sure a string is not entered"""
    def test_only_integer_is_accepted(self):
        birth_year = 'two thousand five'
        self.assertEqual(ageCalculator(birth_year), 'Please enter a number.')


if __name__ == '__main__':
    unittest.main()
