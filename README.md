# LANGUAGE_TRANSLATION

## **Overview**
**LANGUAGE_TRANSLATION** is a Python-based project that translates summarized news into multiple Indian languages using the **Google Cloud Translation API**.

## **Features**
- Translates news **headlines and summaries** from English to various Indian languages.
- Utilizes **Google Cloud Translation API** for **highly accurate translations**.
- Supports **multiple Indian languages**, including **Hindi, Telugu, Tamil, Bengali, and more**.
- Uses **secure API authentication** via environment variables.
- Outputs results in **JSON format**.

---

## **Prerequisites**
- Python **3.8+**
- **Google Cloud Platform (GCP) account** with Translation API enabled
- **Service account JSON key file**
- **Internet connection**

---

## **Installation**

### **1. Clone the repository**
```sh
git clone https://github.com/your-username/LANGUAGE_TRANSLATION.git
cd LANGUAGE_TRANSLATION
```

### **2. Create a virtual environment (optional but recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3. Install dependencies**
```sh
pip install -r requirements.txt
```

### **4. Set up environment variables**
- **Create a `.env` file** in the project directory.
- **Add the following line** (update the path to your service account key file):
  ```sh
  GOOGLE_APPLICATION_CREDENTIALS=C:\Users\srila\Downloads\awesome-aspect-455006-b6-56a66c72947e.json
  ```

---

## **Usage**

### **1. Prepare the input file**
Modify the `input.json` file with the news details:
```json
{
    "headline": "Breaking News: Major Earthquake Hits City",
    "summary": "A massive earthquake struck the city today, causing widespread damage. The earthquake caused severe destruction.",
    "date": "01/04/2025",
    "time": "11:10 PM",
    "language": "hi"
}
```

### **2. Run the translation script**
```sh
python translate.py
```

### **3. View the translated output**
The **translated output** is saved in `output.json`:
```json
{
    "headline": "Breaking News: Major Earthquake Hits City",
    "translated_headline": "ब्रेकिंग न्यूज़: बड़े भूकंप ने शहर को हिला दिया",
    "translated_text": "आज शहर में एक बड़ा भूकंप आया, जिससे व्यापक क्षति हुई। इस भूकंप ने गंभीर विनाश किया।",
    "language": "Hindi",
    "date": "01/04/2025",
    "time": "11:10 PM"
}
```

---

## **Supported Languages**

| Language  | Code |
|-----------|------|
| Assamese  | as   |
| Bengali   | bn   |
| Bhojpuri  | bho  |
| Gujarati  | gu   |
| Hindi     | hi   |
| Kannada   | kn   |
| Konkani   | kok  |
| Maithili  | mai  |
| Malayalam | ml   |
| Manipuri  | mni-Mtei |
| Marathi   | mr   |
| Odia      | or   |
| Punjabi   | pa   |
| Sanskrit  | sa   |
| Sindhi    | sd   |
| Tamil     | ta   |
| Telugu    | te   |
| Urdu      | ur   |

---

## **Deployment**
This project can be integrated into a web application. Ensure that:
- The `.env` file is configured correctly on the server.
- Required Python dependencies are installed.
- The server has access to **Google Cloud Translation API**.

---

## **Troubleshooting**

### **Common Issues & Fixes**

- **Translation API Not Working?**
  - Ensure that your Google Cloud project has **Translation API enabled**.
  - Check if the service account key path in `.env` is **correct**.
  - Verify **internet connectivity** and **firewall settings**.

- **Environment Variables Not Loaded?**
  - Run `echo $GOOGLE_APPLICATION_CREDENTIALS` (Linux/macOS) or `echo %GOOGLE_APPLICATION_CREDENTIALS%` (Windows) to verify.
  - Make sure `load_dotenv()` is correctly called in `translate.py`.

---

## **License**
This project is licensed under the **MIT License**.

---

## **Contributing**
Contributions are welcome! Feel free to **fork the repo** and submit a **pull request**.

---

## **Contact**
For queries or support, reach out to: **[your-email@example.com]**
