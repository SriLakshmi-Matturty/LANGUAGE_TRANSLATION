from google.cloud import translate_v2 as translate
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials path from environment variable
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not credentials_path:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS is not set in .env file")

# Set Google Cloud authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# Initialize the Google Translate client
translate_client = translate.Client()

# Indian languages supported by Google Translate
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

# Read input JSON file
with open("input.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    headline = data.get("headline", "")
    summary = data.get("summary", "")
    lang_code = data.get("language", "").strip()
    date = data.get("date", "")
    time = data.get("time", "")

# Validate language code
if lang_code not in target_languages:
    raise ValueError(f"Invalid language code: {lang_code}")

# Translate headline and summary
translated_headline = translate_client.translate(headline, target_language=lang_code)["translatedText"]
translated_summary = translate_client.translate(summary, target_language=lang_code)["translatedText"]

# Prepare output data
output_data = {
    "headline": headline,
    "translated_headline": translated_headline,
    "translated_text": translated_summary,
    "language": target_languages[lang_code],
    "date": date,
    "time": time
}

# Save output JSON file
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)

print(f"Translation saved to output.json")
