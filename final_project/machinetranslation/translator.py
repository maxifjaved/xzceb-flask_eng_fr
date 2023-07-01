"""
This module contains functions for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    """
    Translates English text to French.
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def frenchToEnglish(french_text):
    """
    Translates French text to English.
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
