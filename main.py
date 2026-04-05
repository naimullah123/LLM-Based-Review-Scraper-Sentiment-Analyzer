from scraper import get_reviews
from preprocess import clean_text
from llm import summarize_review
import pandas as pd
import time

url = input("Enter product URL: ")
print("Scraping started...")

reviews = get_reviews(url)
print("Scraping completed.")
print("Number of reviews scraped:", len(reviews))
if not reviews:
    print("No reviews found. Check URL or scraping logic.")
    exit()
data = []

for i, r in enumerate(reviews, start=1):
    print(f"Processing review {i}/{len(reviews)}")

    try:
        cleaned = clean_text(r["text"])
        summary = summarize_review(cleaned)
    except Exception as e:
        summary = "Processing Error"

    data.append({
        "author": r["author"],
        "rating": r["rating"],
        "review": r["text"],
        "summary": summary
    })

    time.sleep(1)

df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)
df.to_json("output.json", orient="records", indent=2)

print("Done! Saved to output.csv and output.js")