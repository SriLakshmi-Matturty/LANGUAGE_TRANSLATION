# NEWS AVATAR- TRANSLATION

## Overview
News Avatar Translation is a Python-based project that translates summarized news into multiple Indian languages using Google Cloud Translation API.

## Features
- Translates news summaries from English to various Indian languages.
- Uses Google Cloud Translation API for accurate translations.
- Supports multiple Indian languages, including Hindi, Telugu, Tamil, Bengali, and more.
- Secure API authentication using environment variables.

## Prerequisites
- Python 3.8+
- Google Cloud Platform (GCP) account with Translation API enabled
- Service account JSON key file
- Internet connection

## Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/News-Avatar-Translation.git
   cd News-Avatar-Translation
   ```

2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project directory.
   - Add the following line (update the path to your service account key file):
     ```sh
     GOOGLE_APPLICATION_CREDENTIALS=path/to/your-service-account.json
     ```

## Usage

1. **Run the script**
   ```sh
   python translate.py
   ```

2. **Provide input**
   - Enter the summarized news in English.
   - Select a target language from the list by entering the corresponding language code.

3. **Get the translation**
   - The script outputs the translated text in the selected language.

## Supported Languages
| Language | Code |
|----------|------|
| Assamese | as |
| Bengali  | bn |
| Bhojpuri | bho |
| Gujarati | gu |
| Hindi    | hi |
| Kannada  | kn |
| Konkani  | kok |
| Maithili | mai |
| Malayalam| ml |
| Manipuri | mni-Mtei |
| Marathi  | mr |
| Odia     | or |
| Punjabi  | pa |
| Sanskrit | sa |
| Sindhi   | sd |
| Tamil    | ta |
| Telugu   | te |
| Urdu     | ur |

## Deployment
This project can be integrated into a web application. Ensure that:
- The `.env` file is configured correctly on the server.
- Required Python dependencies are installed.
- The server has access to Google Cloud Translation API.

## Troubleshooting
### Common Issues & Fixes
- **Translation API Not Working?**
  - Ensure that your Google Cloud project has Translation API enabled.
  - Check if the service account key path in `.env` is correct.
  - Verify internet connectivity and firewall settings.

- **Environment Variables Not Loaded?**
  - Run `echo $GOOGLE_APPLICATION_CREDENTIALS` (Linux/macOS) or `echo %GOOGLE_APPLICATION_CREDENTIALS%` (Windows) to verify.
  - Make sure `load_dotenv()` is correctly called in `translate.py`.
