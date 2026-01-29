import pandas as pd
import os
import time
# We import the functions you already have
from scraper import scrape_news 
# Note: Ensure your weather_api.py has a function called get_weather(city)
from weather_api import get_weather, extract_locations 

def main():
    print("Step 1: Scraping news from BBC...")
    news_titles = scrape_news() # This returns a list of headlines
    
    results = []

    print("Step 2: Processing headlines and fetching weather...")
    for title in news_titles:
        # We find locations (like 'Iran' or 'Portugal') inside the headline
        locations = extract_locations(title)
        
        if not locations:
            # If no place is mentioned, per your requirement
            results.append({
                "title": title,
                "city": "no country/city mentioned",
                "temperature": "",
                "weather_description": ""
            })
        else:
            # If multiple locations are found (e.g., Israel AND Iran), 
            # we fetch weather for each one.
            for city in locations:
                weather_data = get_weather(city)
                
                # Check if the API returned valid data or an error
                if isinstance(weather_data, dict) and "main" in weather_data:
                    results.append({
                        "title": title,
                        "city": city,
                        "temperature": f"{weather_data['main']['temp']}°C",
                        "weather_description": weather_data['weather'][0]['description']
                    })
                else:
                    results.append({
                        "title": title,
                        "city": city,
                        "temperature": "N/A",
                        "weather_description": "Not Found"
                    })
                
                # Sleep briefly to avoid hitting OpenWeather limits too fast
                time.sleep(0.2)

    # Step 3: Create the DataFrame and Save
    df = pd.DataFrame(results)
    
    # Ensure the 'data' folder exists
    if not os.path.exists("data"):
        os.makedirs("data")
        
    df.to_csv("data/final_data.csv", index=False, encoding='utf-8')
    print("\nSUCCESS: All data combined and saved to data/final_data.csv!")
    print(df.head())

if __name__ == "__main__":
    main()