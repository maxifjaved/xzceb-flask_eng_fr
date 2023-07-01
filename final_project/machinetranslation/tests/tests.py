import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
  def test_englishToFrench(self):
    self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')
    self.assertNotEqual(englishToFrench('Hello'), 'Test')

class TestFrenchToEnglish(unittest.TestCase):
  def test_frenchToEnglish(self):
    self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    self.assertNotEqual(frenchToEnglish('Au revoir'), 'Test')


if __name__ == '__main__':
  unittest.main()
