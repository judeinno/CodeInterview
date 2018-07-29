import unittest

from app.age_calculator import ageCalculator


class TestAge_calculator(unittest.TestCase):

    def test_string_to_integer_is_accepted(self):
        birth_year = '1990'
        self.assertEqual(ageCalculator(int(birth_year)), 28)

    def test_correct_age_is_calculated(self):
        birth_year = 1990
        assert ageCalculator(birth_year) == 28

    def test_only_integer_is_accepted(self):
        birth_year = 'two thousand five'
        self.assertEqual(ageCalculator(birth_year), 'Please enter a number.')


if __name__ == '__main__':
    unittest.main()
