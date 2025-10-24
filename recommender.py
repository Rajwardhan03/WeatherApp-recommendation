# This module contains all the recommendation logic.

def get_recommendations(temp, condition):
    """Generates recommendations based on weather."""
    
    # Clothing recommendations
    if temp > 30:
        clothing = "🔥 Very hot! Wear light cottons, shorts, and stay hydrated."
    elif 20 <= temp <= 30:
        clothing = "☀️ Pleasant weather. A t-shirt and jeans/shorts are perfect."
    elif 10 <= temp < 20:
        clothing = "☁️ A bit cool. A light jacket or sweater is a good idea."
    else: # temp < 10
        clothing = "❄️ It's cold! Wear a warm jacket, gloves, and a hat."

    # Activity recommendations
    if condition == "Rain" or condition == "Drizzle":
        activity = "🌧️ It's raining! A perfect day to read a book, visit a museum, or watch a movie indoors."
    elif condition == "Clear":
        activity = "😎 Clear skies! Great for a picnic, a walk in the park, or any outdoor sport."
    elif condition == "Clouds":
        activity = "🌥️ It's cloudy. Good for a jog or visiting an outdoor market."
    elif condition == "Snow":
        activity = "⛄️ Snowing! Time for building a snowman or having some hot chocolate."
    elif condition == "Thunderstorm":
        activity = "🌩️ Stay indoors! It's not safe to be outside."
    else:
        activity = "Just a regular day. Enjoy your plans!"
        
    return clothing, activity
def get_food_recommendation(temp, condition):
    """Generates food recommendations based on weather."""
    
    if temp > 30:
        food = "☀️ It's hot! Time for something refreshing like a cold salad, fresh fruit juice, or ice cream."
    elif 20 <= temp <= 30:
        if condition == "Rain":
            food = "🌧️ Rainy and warm. A perfect excuse for some hot pakoras and tea, or a light soup."
        else:
            food = "😎 Great weather! Perfect for a barbecue, a sandwich, or any of your favorite meals."
    elif 10 <= temp < 20:
        food = "☁️ It's cool. A great evening for some hot soup, pasta, or a warm cup of coffee."
    else: # temp < 10
        food = "❄️ Brr, it's cold! You need something warm and hearty. Think hot stew, biryani, or hot chocolate."

    return food