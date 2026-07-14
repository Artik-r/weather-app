# 🌦️ Weather App

A simple and interactive command-line Weather App built with Python that fetches real-time weather information using the OpenWeatherMap API.

---

## 📌 Features

* 🌍 Search weather by city name
* 🌡️ Current temperature
* 🤗 Feels like temperature
* 💧 Humidity
* 🌬️ Wind speed
* 📈 Atmospheric pressure
* ☁️ Cloud coverage
* 👀 Visibility
* 🌅 Sunrise time
* 🌇 Sunset time
* 📍 Latitude & Longitude
* 🌤️ Weather condition with emojis
* ❌ Handles invalid city names gracefully

---

## 🛠️ Technologies Used

* Python 3
* Requests
* OpenWeatherMap API
* JSON
* Datetime Module

---

## 📂 Project Structure

```text
weather-app/
│
├── .gitignore
├── README.md
├── config.py              # Your API key (ignored by Git)
├── config_example.py      # Example configuration
├── main.py
└── requirements.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/weather-app.git
```

Go to the project folder:

```bash
cd weather-app
```

Install the required package:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Setup

Create a free account at **OpenWeatherMap**.

Generate an API key.

Open `config.py` and add your key:

```python
API_KEY = "YOUR_API_KEY"
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📸 Sample Output

```text
============================================================
                  WEATHER REPORT
============================================================

📍 Location      : London, GB
🌡 Temperature   : 20.1°C
🤗 Feels Like    : 20.2°C
💧 Humidity      : 75%
🌬 Wind Speed    : 2.24 m/s
📈 Pressure      : 1021 hPa
☁ Cloud Cover   : 40%
👀 Visibility    : 10.0 km
🌅 Sunrise       : 04:58 AM
🌇 Sunset        : 09:14 PM
📌 Latitude      : 51.51
📌 Longitude     : -0.13
☁ Condition      : Scattered Clouds
```

---

## 🎯 Future Improvements

* 5-Day Weather Forecast
* Weather by GPS Location
* Air Quality Index (AQI)
* Weather Alerts
* Save Search History
* Graphical User Interface (Tkinter or Flask)

---

## 👨‍💻 Artika

