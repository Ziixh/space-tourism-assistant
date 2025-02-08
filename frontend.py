import streamlit as st
import requests

# Direct URL of the background image
background_image = "https://image.lexica.art/full_webp/e6a67e16-d583-4c97-a685-a0c3a456cb5e"

# Add the image as the background for both the main app and the sidebar
st.markdown(
    f"""
    <style>
    /* Apply background image to the main app */
    .stApp {{
        background-image: url('{background_image}');
        background-size: cover; /* Ensures the image covers the entire screen */
        background-repeat: no-repeat; /* Prevents the image from repeating */
        background-attachment: fixed; /* Fixes the background while scrolling */
    }}

    /* Apply background image to the sidebar */
    [data-testid="stSidebar"] {{
        background-image: url('{background_image}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Add a semi-transparent overlay to the main app */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* Black with 50% opacity */
        z-index: -1;
    }}

    /* Add a semi-transparent overlay to the sidebar */
    [data-testid="stSidebar"]::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* Black with 50% opacity */
        z-index: -1;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title
st.title("🚀 Space Tourism Personal Assistant")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", [
    "Itinerary",
    "Space Fact",
    "Current Weather",
    "Mission Updates",
    "Quiz",
    "Predictive Analytics",
    "Virtual Tour"
])

# Fetch itinerary from the backend
def fetch_itinerary():
    response = requests.get("http://127.0.0.1:8000/itinerary")
    return response.json()

# Fetch space fact from the backend
def fetch_space_fact():
    response = requests.get("http://127.0.0.1:8000/space-fact")
    return response.json()

# Fetch current weather data from the backend
def fetch_current_weather(lat, lon):
    response = requests.get(f"http://127.0.0.1:8000/current-weather/{lat}/{lon}")
    return response.json()

# Fetch mission updates from the backend
def fetch_mission_updates():
    response = requests.get("http://127.0.0.1:8000/mission-updates")
    return response.json()

# Fetch quiz question from the backend
def fetch_quiz():
    response = requests.get("http://127.0.0.1:8000/quiz")
    return response.json()

# Fetch predictive analytics from the backend
def fetch_prediction(day):
    response = requests.get(f"http://127.0.0.1:8000/predict-weather/{day}")
    return response.json()

# Display content based on menu selection
if menu == "Itinerary":
    st.header("📅 Itinerary")
    if st.button("Show My Itinerary"):
        itinerary = fetch_itinerary()
        st.write(f"**Launch Time:** {itinerary['launch_time']}")
        st.write(f"**Duration:** {itinerary['duration']}")
        st.write("**Activities:**")
        for activity in itinerary['activities']:
            st.write(f"- {activity}")
        st.write("**Travel Tips:**")
        for tip in itinerary['tips']:
            st.write(f"- {tip}")

elif menu == "Space Fact":
    st.header("🌌 Space Fact")
    if st.button("Show Space Fact"):
        space_fact = fetch_space_fact()
        st.write(f"**Title:** {space_fact['title']}")
        st.write(f"**Explanation:** {space_fact['explanation']}")
        st.image(space_fact['image_url'], caption="Space Image", use_container_width=True)

elif menu == "Current Weather":
    st.header("🌤️ Current Weather at Launch Site")
    lat = st.text_input("Enter Latitude (e.g., 28.6139 for Cape Canaveral)")
    lon = st.text_input("Enter Longitude (e.g., -80.5774 for Cape Canaveral)")
    if st.button("Check Current Weather"):
        if lat and lon:
            weather = fetch_current_weather(float(lat), float(lon))
            st.write(f"**Location:** {weather['location']}")
            st.write(f"**Weather:** {weather['weather']}")
            st.write(f"**Temperature:** {weather['temperature']}°C")
            st.write(f"**Humidity:** {weather['humidity']}%")
            st.write(f"**Wind Speed:** {weather['wind_speed']} m/s")

elif menu == "Mission Updates":
    st.header("🛰️ Mission Updates")
    if st.button("Check Latest Mission Updates"):
        mission = fetch_mission_updates()
        st.write(f"**Mission Name:** {mission['mission_name']}")
        st.write(f"**Date:** {mission['date']}")
        st.write(f"**Details:** {mission['details']}")
        if mission["webcast"]:
            st.video(mission["webcast"])
        else:
            st.warning("No webcast available for this mission.")

elif menu == "Quiz":
    st.header("🎯 Quiz")
    if st.button("Start Space Quiz"):
        quiz = fetch_quiz()
        st.session_state.quiz_question = quiz["question"]
        st.session_state.quiz_answer = quiz["answer"]
        st.write(f"**Question:** {st.session_state.quiz_question}")
    
    if "quiz_question" in st.session_state:
        user_answer = st.text_input("Your Answer")
        if st.button("Submit Answer"):
            if user_answer.lower() == st.session_state.quiz_answer.lower():
                st.success("Correct!")
            else:
                st.error(f"Wrong! The correct answer is: {st.session_state.quiz_answer}")

elif menu == "Predictive Analytics":
    st.header("📊 Predictive Analytics")
    lat = st.text_input("Enter Latitude (e.g., 28.6139 for Cape Canaveral)")
    lon = st.text_input("Enter Longitude (e.g., -80.5774 for Cape Canaveral)")
    day = st.number_input("Enter Day Since Launch", min_value=1, max_value=10)
    if st.button("Predict Weather"):
        if lat and lon:
            weather = fetch_current_weather(float(lat), float(lon))
            st.write(f"**Current Location:** {weather['location']}")
            st.write(f"**Current Weather:** {weather['weather']}")
        prediction = fetch_prediction(day)
        st.write(f"**Predicted Temperature on Day {day}:** {prediction['predicted_temperature']}°C")

elif menu == "Virtual Tour":
    st.header("🌍 Virtual Tour of the Solar System")
    st.markdown("""
    <iframe src="https://eyes.nasa.gov/" width="100%" height="600px"></iframe>
    """, unsafe_allow_html=True)