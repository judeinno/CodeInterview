import unittest

from app.Piglatin import PigLatinConverter


class TestConverter(unittest.TestCase):

    def test_for_none_vowel(self):
        self.pig = PigLatinConverter(args='jude')
        result = self.pig.pig_latin()
        self.assertEqual(result, 'udejay')

    def test_for_vowel(self):
        self.pig = PigLatinConverter(args='andela')
        self.assertEqual(self.pig.pig_latin(), 'andelaway')

    def test_for_integers(self):
        self.pig = PigLatinConverter(args= str(55))
        self.assertEqual(self.pig.pig_latin(), 'Please enter a word')

if __name__ == '__main__':
    unittest.main()