import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        # Testing Transaltion of 'Bonjour' to 'Hello'
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Testing that null input outputs null
        self.assertNotEqual(french_to_english('Moon'), '')

class TestEnglishToFrench(unittest.TestCase):       
    def test_englishToFrench(self):
        # Testing Transaltion of 'Hello' to 'Bonjour'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
         # Testing that null input outputs null
        self.assertNotEqual(english_to_french('Moon'), '')

if __name__ == '__main__':
    unittest.main()