import requests
from bs4 import BeautifulSoup

def get_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    reviews = []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print("Error fetching page:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("div", class_="thumbnail")

    for item in items:
        try:
            desc = item.find("p", class_="description").text.strip()

            reviews.append({
                "text": desc,
                "rating": "N/A",
                "author": "Anonymous"
            })
        except Exception:
            continue

    return reviews