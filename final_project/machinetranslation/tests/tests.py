import unittest
from machinetranslation import translator

class TestTranslate(unittest.TestCase): 
    def test_frenchToEnglish(self): 
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Hello')
        
    def test_englishToFrench(self): 
        self.assertNotEqual(translator.english_to_french('Hello'), 'Bonjour')

unittest.main()