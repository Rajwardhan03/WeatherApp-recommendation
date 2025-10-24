# This module handles all API calls to OpenWeatherMap.
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city, api_key):
    """Fetches weather data from the OpenWeatherMap API."""
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Request temperature in Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        data = response.json()
        
        # Extract the data we need
        temperature = data['main']['temp']
        condition = data['weather'][0]['main'] 
        description = data['weather'][0]['description'] 
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        return temperature, condition, description, humidity, wind_speed
    
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return "Error", "City not found. Please check the spelling.", None, None, None
        else:
            return "Error", f"An error occurred: {err}", None, None, None
    except Exception as e:
        return "Error", f"An unexpected error occurred: {e}", None, None, None