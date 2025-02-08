from fastapi import FastAPI
import requests
import random
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI()

# NASA API Key
NASA_API_KEY = "hqj3QWhu108i1UA6yXnilHjA0WlBCTuE8F0SMlgT"

# OpenWeatherMap API Key
OPENWEATHERMAP_API_KEY = "113d459265a0f8d169843e20e9d4fe94"

# Example itinerary data with tips
example_itinerary = {
    "launch_time": "10:00 AM UTC",
    "duration": "6 hours",
    "activities": ["Launch", "Orbit Stabilization", "Space Walk"],
    "tips": [
        "Pack light but include essentials like a spacesuit and personal items.",
        "Stay hydrated during the journey.",
        "Follow all safety instructions from the crew."
    ]
}

# Endpoint to get the itinerary
@app.get("/itinerary")
def get_itinerary():
    return example_itinerary

# Endpoint to fetch Astronomy Picture of the Day (APOD)
@app.get("/space-fact")
def get_space_fact():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url).json()
    return {
        "title": response.get("title"),
        "explanation": response.get("explanation"),
        "image_url": response.get("url")
    }

# Endpoint to fetch current weather data
@app.get("/current-weather/{lat}/{lon}")
def get_current_weather(lat: float, lon: float):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url).json()
    return {
        "location": response["name"],
        "weather": response["weather"][0]["description"],
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "wind_speed": response["wind"]["speed"]
    }

# Endpoint to fetch mission updates
@app.get("/mission-updates")
def get_mission_updates():
    url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url).json()
    return {
        "mission_name": response["name"],
        "date": response["date_utc"],
        "details": response["details"],
        "webcast": response["links"]["webcast"]
    }

# Quiz endpoint with more questions
@app.get("/quiz")
def get_quiz():
    questions = [
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "Who was the first human to travel into space?", "answer": "Yuri Gagarin"},
        {"question": "Which company launched the first private spacecraft?", "answer": "SpaceX"},
        {"question": "What is the name of Earth's moon?", "answer": "Moon"},
        {"question": "What is the closest star to Earth?", "answer": "Sun"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What is the name of NASA's Mars rover that landed in 2021?", "answer": "Perseverance"},
        {"question": "What causes the Northern Lights?", "answer": "Solar wind interacting with Earth's magnetic field"}
    ]
    return random.choice(questions)

# Predictive analytics endpoint
X = np.array([[1], [2], [3], [4], [5]])  # Days since launch
y = np.array([20, 22, 24, 25, 26])       # Temperatures
model = LinearRegression()
model.fit(X, y)

@app.get("/predict-weather/{day}")
def predict_weather(day: int):
    prediction = model.predict(np.array([[day]]))
    return {"predicted_temperature": round(prediction[0], 2)}