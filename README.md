# LLM-Based-Review-Scraper-Sentiment-Analyzer

## 📌 Objective

The objective of this project is to build a robust Python application that:

* Scrapes product review data from a given URL
* Preprocesses the extracted text
* Uses an LLM (or fallback mechanism) to generate sentiment summaries
* Stores results in a structured format (CSV & JSON)

---

## ⚙️ Features

* 🔍 Web scraping using `requests` and `BeautifulSoup`
* 🧹 Text preprocessing and cleaning
* 🤖 LLM-based sentiment summarization (OpenAI-compatible)
* 🔁 Fallback sentiment system (for API failures or quota limits)
* 📊 Structured output in CSV and JSON formats
* ⚠️ Error handling for API failures and empty data
* ⏳ Rate limiting to avoid API overuse

---

## 🏗️ Project Structure

```
llm-review-analyzer/
│
├── scraper.py        # Scrapes product reviews
├── preprocess.py     # Cleans and preprocesses text
├── llm.py            # LLM integration + fallback logic
├── main.py           # Main pipeline
├── output.csv        # Output file (CSV)
├── output.json       # Output file (JSON)
├── requirements.txt  # Dependencies
└── .env              # API key (not included in repo)
```

---

## 🔗 Input Used

For demonstration, the following test site was used:

```
https://webscraper.io/test-sites/e-commerce/static/computers
```

> Note: Amazon was initially attempted, but due to dynamic loading and anti-scraping mechanisms, a static test site was used for reliable execution.

---

## 🚀 How It Works

1. The user provides a product URL
2. The scraper extracts product descriptions (used as reviews)
3. Text is cleaned and preprocessed
4. Each review is sent to:

   * OpenAI API (if available), OR
   * A fallback sentiment system
5. Results are stored in CSV and JSON formats

---

## 🤖 LLM & Fallback Strategy

* The system first attempts to use an OpenAI-compatible API
* If the API fails (quota, key issues, etc.), a fallback rule-based sentiment system is used

### Example Output:

```
Positive – high-performance configuration  
Neutral – average product  
Negative – performance issues  
```

---

## ⚠️ Challenges & Solutions

### Challenge 1: Amazon Scraping

* Amazon blocks scraping and uses dynamic content
* ✅ Solution: Switched to a static test site

### Challenge 2: API Quota Limit

* OpenAI API returned quota errors
* ✅ Solution: Implemented fallback sentiment system

### Challenge 3: Environment Variables

* API key loading issues due to system variables
* ✅ Solution: Proper `.env` setup and debugging

---

## 🔐 Security

* API keys are stored using environment variables (`.env`)
* No keys are hardcoded in the source code

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python main.py
```

Then enter the product URL when prompted.

---

## 📊 Output

* `output.csv` → tabular format
* `output.json` → structured format

---

## 🔮 Future Improvements

* Add support for dynamic websites using Selenium
* Improve sentiment analysis using fine-tuned models
* Add visualization dashboards
* Support batch URL processing

---

## ✅ Conclusion

This project demonstrates a complete pipeline involving:

* Data scraping
* Preprocessing
* LLM integration
* Robust error handling

It is designed to handle real-world challenges like API failures and scraping limitations.

---
