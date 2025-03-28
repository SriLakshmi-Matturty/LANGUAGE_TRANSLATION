# -*- coding: utf-8 -*-
"""Translate.ipynb

Original file is located at
    https://colab.research.google.com/drive/1rUC9eFHjnx1YYIopjyPaVKtFMwpiTaxs
"""

from google.cloud import translate_v2 as translate
import os

"""# Path to service account JSON key"""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/content/awesome-aspect-455006-b6-56a66c72947e.json'

"""# Initializing the Google Translate client"""

translate_client = translate.Client()

"""# Indian languages supported by Google Translate"""

target_languages = {
    'as': 'Assamese',
    'bn': 'Bengali',
    'bho': 'Bhojpuri',
    'gu': 'Gujarati',
    'hi': 'Hindi',
    'kn': 'Kannada',
    'ks': 'Kashmiri',
    'mai': 'Maithili',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ne': 'Nepali',
    'or': 'Odia',
    'pa': 'Punjabi',
    'sa': 'Sanskrit',
    'sd': 'Sindhi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'ur': 'Urdu',
}

"""# Input Text"""

summary = input("Enter the summarized news in English:\n")

"""# Input Target Language"""

print("\nSelect the target language:")
for code, lang in target_languages.items():
    print(f"{code} - {lang}")

lang_code = input("\nEnter language code from above: ").strip()

"""# Result"""

result = translate_client.translate(summary, target_language=lang_code)
print(f"\nTranslated to {target_languages[lang_code]}:\n{result['translatedText']}")

