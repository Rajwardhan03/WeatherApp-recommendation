import streamlit as st

# Import our custom modules
from api_client import fetch_weather
from recommender import get_recommendations, get_food_recommendation
from config import API_KEY

# --- Function to load our custom CSS ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- UI Setup ---
st.set_page_config(page_title="Weather Advisor", page_icon="🌦️", layout="wide")
load_css("style.css") 

st.title("Weather Recommendation Engine")

# --- Main App Logic ---
city = st.text_input("Enter your city:")

if st.button("Get Recommendation", type="primary"): 
    if city:
        with st.spinner(f"Fetching weather for {city}..."):
            temp, condition, desc, humidity, wind = fetch_weather(city, API_KEY)
        
        if temp != "Error":
            clothing_rec, activity_rec = get_recommendations(temp, condition)
            food_rec = get_food_recommendation(temp, condition)
            
            st.subheader(f"Weather in {city.title()}:")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(label="Temperature", value=f"{temp}°C")
            with col2:
                st.metric(label="Condition", value=f"{condition}")
            with col3:
                st.metric(label="Humidity", value=f"{humidity}%")
            with col4:
                st.metric(label="Wind Speed", value=f"{wind} m/s")

            st.info(f"Description: {desc.title()}")
            
            st.subheader("Your Personal Recommendations:")
            
            # --- [NEW] Using st.markdown for custom cards ---
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(
                    f"""
                    <div class="recommendation-card">
                        <p>👕 <strong>Clothing:</strong><br>{clothing_rec}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            with col2:
                st.markdown(
                    f"""
                    <div class="recommendation-card">
                        <p>🏃 <strong>Activity:</strong><br>{activity_rec}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            with col3:
                st.markdown(
                    f"""
                    <div class="recommendation-card">
                        <p>🍲 <strong>Food:</strong><br>{food_rec}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            # --- End of new section ---
            
        else:
            # We'll use st.error for errors, as that's appropriate
            st.error(f"❌ {condition}")
            
    else:
        # We'll use st.warning for warnings
        st.warning("Please enter a city name.")