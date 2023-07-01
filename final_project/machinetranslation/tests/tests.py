import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
  def test_englishToFrench(self):
    self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')
    self.assertEqual(englishToFrench('Congratulations'), 'Félicitations')

class TestFrenchToEnglish(unittest.TestCase):
  def test_frenchToEnglish(self):
    self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')


if __name__ == '__main__':
  unittest.main()
