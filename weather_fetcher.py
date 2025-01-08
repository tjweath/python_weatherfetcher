import requests

API_KEY = 

def get_coordinates(city_name):
    """
    Fetches the latitude and longitude of a given city using the OpenWeatherMap Geocoding API.
    """
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}"
    try:
        response = requests.get(geo_url)
        response.raise_for_status()
        data = response.json()
        
        if len(data) > 0:
            lat, lon = data[0]["lat"], data[0]["lon"]
            return lat, lon
        else:
            raise ValueError(f"City '{city_name}' not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def get_weather_by_coordinates(lat, lon):
    """
    Fetches weather data for given latitude and longitude using the OpenWeatherMap Current Weather Data API.
    """
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(weather_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
import json

def display_and_save_weather(data, city_name):
    """
    Displays weather information and saves it to a JSON file.
    """
    if not data:
        print("No data available to display.")
        return

    # Parse and display weather details
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"Weather in {city_name}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

    # Save to a file
    filename = f"{city_name.lower()}_weather.json"
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Weather data saved to {filename}")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    lat, lon = get_coordinates(city)
    if lat and lon:
        weather_data = get_weather_by_coordinates(lat, lon)
        display_and_save_weather(weather_data, city)
    else:
        print("Unable to fetch weather data. Please check the city name or API key.")
