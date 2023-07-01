import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslationMethods(unittest.TestCase):

  def test_englishToFrench(self):
    self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')

  def test_frenchToEnglish(self):
    self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


unittest.main()
