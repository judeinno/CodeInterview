import unittest

from app.Piglatin import PigLatinConverter

""" These tests are for the piglatin converter"""

class TestConverter(unittest.TestCase):

    """This test makes sure that once the first letters are not vowels they are moved to the end"""
    def test_for_none_vowel(self):
        self.pig = PigLatinConverter(args='jude')
        result = self.pig.pig_latin()
        self.assertEqual(result, 'udejay')

    """This test makes sure that once the first letter is a vowel the word way is added to the end of the word"""
    def test_for_vowel(self):
        self.pig = PigLatinConverter(args='andela')
        self.assertEqual(self.pig.pig_latin(), 'andelaway')

    """This test makes sure that an integer is not entered"""
    def test_for_integers(self):
        self.pig = PigLatinConverter(args= str(55))
        self.assertEqual(self.pig.pig_latin(), 'Please enter a word')

if __name__ == '__main__':
    unittest.main()