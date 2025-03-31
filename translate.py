from google.cloud import translate_v2 as translate
import os
from dotenv import load_dotenv

load_dotenv()

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not credentials_path:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS is not set in .env file")

"""# Path to service account JSON key"""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

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
    'kok': 'Konkani',
    'mai': 'Maithili',
    'ml': 'Malayalam',
    'mni-Mtei': 'Manipuri',
    'mr': 'Marathi',
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

