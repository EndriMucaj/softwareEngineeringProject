import pandas as pd
import spacy
import requests
import time

# --- CONFIGURATION ---
API_KEY = "f7338d8d720f9c9bb2a9ac1fc3aa9011"
INPUT_FILE = r"C:\Users\user\Desktop\project\data\news.csv"
OUTPUT_FILE = r"C:\Users\user\Desktop\project\data\news_with_weather.csv"

# Load NLP model for location extraction
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def get_weather(location):
    """Fetches weather data for a specific city or country."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"{temp}°C, {desc}"
        else:
            return "Weather data not found"
    except Exception as e:
        return f"Error: {e}"

def extract_locations(text):
    """Extracts city/country names from a headline."""
    doc = nlp(text)
    # GPE = Geopolitical Entity (Countries, Cities, States)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return list(set(locations))  # Remove duplicates

def process_news():
    print(f"Reading {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE)
    
    results = []

    for index, row in df.iterrows():
        headline = row['title']
        locations = extract_locations(headline)
        
        if not locations:
            results.append({
                "Headline": headline,
                "Location": "No country/city mentioned",
                "Weather": ""
            })
        else:
            for loc in locations:
                print(f"Fetching weather for: {loc}")
                weather_info = get_weather(loc)
                results.append({
                    "Headline": headline,
                    "Location": loc,
                    "Weather": weather_info
                })
                # Small delay to avoid hitting API limits too fast
                time.sleep(0.2)

    # Save to new CSV
    new_df = pd.DataFrame(results)
    new_df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
    print(f"\nSuccess! Data saved to {OUTPUT_FILE}")
    print(new_df.head(10))

if __name__ == "__main__":
    process_news()