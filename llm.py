import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def summarize_review(text: str) -> str:
    if not text:
        return "Empty review"

    try:
        # Try API if key exists
        if os.getenv("OPENAI_API_KEY"):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Give sentiment and short summary"},
                    {"role": "user", "content": text}
                ]
            )
            return response.choices[0].message.content.strip()
    except Exception:
        pass

    # Fallback: simple keyword-based sentiment analysis
    text_lower = text.lower()

    # Positive keywords
    positive_words = ["good", "great", "best", "excellent", "fast", "powerful", "high performance"]
    # Negative keywords
    negative_words = ["bad", "poor", "slow", "worst", "lag", "issue"]

    if any(word in text_lower for word in positive_words):
        return "Positive - good performance and features"
    elif any(word in text_lower for word in negative_words):
        return "Negative - performance or usability issues"
    elif "i7" in text_lower or "16gb" in text_lower:
        return "Positive - high-performance configuration"
    elif "i3" in text_lower or "4gb" in text_lower:
        return "Neutral - basic configuration"
    else:
        return "Neutral - average product"