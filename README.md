# 🌦️ Weather Recommendation Engine

A smart web application built with Python and Streamlit that fetches real-time weather data for any city and provides personalized recommendations for clothing, activities, and food.

This app features a clean, multi-file structure and a modern "glassmorphism" UI built with custom CSS.

## ✨ Features

* **Real-Time Weather:** Enter any city and get instant data (temperature, condition, humidity, wind) from the OpenWeatherMap API.
* **3-Tier Recommendations:** Receive smart advice on:
    * 👕 **Clothing:** What to wear for the current temperature.
    * 🏃 **Activity:** What to do (e.g., stay indoors, go for a picnic).
    * 🍲 **Food:** What to eat or drink based on the weather.
* **Modern UI:** A clean, responsive interface with a "glassmorphism" (frosted-glass) effect.
* **Professional Structure:** The code is refactored into a clean, multi-file structure:
    * `app.py`: The main Streamlit app (UI logic).
    * `api_client.py`: Handles all API calls.
    * `recommender.py`: Contains all the "brain" logic for recommendations.
    * `config.py`: Holds the secret API key.
    * `style.css`: Contains all custom styling.

## 🛠️ Tech Stack

* **Backend:** Python
* **Frontend:** Streamlit
* **Styling:** Custom CSS
* **Data:** OpenWeatherMap API

## 🚀 How to Run This Project

Follow these steps to get the app running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Rajwardhan03/WeatherApp-recommendation.git](https://github.com/Rajwardhan03/WeatherApp-recommendation.git)
    cd WeatherApp-recommendation
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Get your API Key:**
    * Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/).
    * Navigate to your account page and find your **API key**.

5.  **Create the config file:**
    * In the project's root directory, create a new file named `config.py`.
    * Inside `config.py`, add the following line, pasting your own API key:
    ```python
    API_KEY = "YOUR_SECRET_API_KEY_HERE"
    ```
    *(This file is listed in `.gitignore`, so your secret key will not be pushed to GitHub.)*

6.  **Run the app!**
    ```bash
    streamlit run app.py
    ```

Your app should now be open and running in your web browser!