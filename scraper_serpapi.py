import requests
import pandas as pd
import time

API_KEY = input("Enter your SerpApi API key: ")

all_restaurants = []

url = "https://serpapi.com/search.json"

categories = [
    "restaurant",
    "cafe",
    "bistro",
    "brasserie",
    "steakhouse",
    "sushi restaurant",
    "italian restaurant",
    "mexican restaurant",
    "seafood restaurant",
    "vegetarian restaurant",
    "vegan restaurant",
]

for category in categories:
    for start in range(0, 120, 20):
        params = {
            "engine": "google_maps",
            "google_domain": "google.com",
            "hl": "en",
            "ll": "@30.2672,-97.7431,8z",
            "q": category,
            "start": start,
            "type": "search",
            "api_key": API_KEY
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; bot/1.0; +https://yourdomain.example)"
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        places = data.get("local_results", [])
        if not places:
            print(f"Nenhum resultado na página start={start}")
            continue

        for place in places:
            name = place.get("title", "")
            address = place.get("address", "")
            phone = place.get("phone", "")
            website = place.get("website", "")

            all_restaurants.append([name, address, phone, website, "google_maps"])

        time.sleep(1)

df = pd.DataFrame(all_restaurants, columns=["name", "address", "phone", "website", "source"])
df.drop_duplicates(subset=["name", "address"], inplace=True)

df
