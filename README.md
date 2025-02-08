# 🚀 Space Tourism Personal Assistant

Your ultimate companion for planning and experiencing space adventures!

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview
The **Space Tourism Personal Assistant** is a web application designed to assist future space tourists with planning their journey, staying informed, and engaging with space-related content. The app integrates APIs, machine learning, and gamification to provide a seamless and immersive experience.

Whether you're preparing for a trip to space or simply curious about the universe, this app has everything you need:
- Personalized itineraries for space travel.
- Real-time weather updates for launch sites.
- Educational content like space facts and quizzes.
- Predictive analytics for temperature trends.
- Virtual tours of the solar system.

---

## Features
1. **Itinerary Planning**:
   - A personalized schedule for space travel with tips for travelers.
2. **Space Facts**:
   - Daily NASA Astronomy Picture of the Day (APOD) with explanations.
3. **Current Weather**:
   - Real-time weather data for launch sites using OpenWeatherMap API.
4. **Mission Updates**:
   - Latest SpaceX mission details and webcasts.
5. **Quiz**:
   - Interactive space trivia to educate users.
6. **Predictive Analytics**:
   - Predicting temperature trends for launch days using machine learning.
7. **Virtual Tour**:
   - Embedded NASA Eyes on the Solar System for an immersive virtual experience.

---

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ziixh/space-tourism-assistant.git
   cd space-tourism-assistant

2. Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies :
pip install -r requirements.txt

4. Run the Backend :
Start the FastAPI backend server:
uvicorn backend:app --reload

5. Run the Frontend :
Start the Streamlit frontend:
streamlit run frontend.py

6. Access the App :
Open your browser and navigate to http://localhost:8501 to use the app.

## Usage
Use the sidebar to navigate between features like itinerary, space facts, weather updates, and more.
Enter latitude and longitude for real-time weather updates.
Explore mission updates, take quizzes, and enjoy the virtual tour of the solar system.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
git checkout -b feature/YourFeatureName
3. Commit your changes:
git commit -m "Add YourFeatureName"
4. Push to the branch:
git push origin feature/YourFeatureName
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
NASA API: https://api.nasa.gov
OpenWeatherMap API: https://openweathermap.org
SpaceX API: https://docs.spacexdata.com
Streamlit: https://streamlit.io

Made with ❤️ by Ziixh