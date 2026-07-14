import requests

from datetime import datetime

from config import API_KEY



# ==========================================================
# Base URL
# ==========================================================

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ==========================================================
# Welcome Screen
# ==========================================================

def welcome_screen():

    print("\n" + "=" * 60)
    print("                     WEATHER APP")
    print("=" * 60)

    print("\nWelcome! 🌤️")

    print("\nThis application provides real-time weather data.")

    print("\nFeatures")
    print("-" * 60)

    print("• Current Temperature")
    print("• Feels Like Temperature")
    print("• Humidity")
    print("• Wind Speed")
    print("• Pressure")
    print("• Sunrise & Sunset")
    print("• Weather Description")

    input("\nPress Enter to continue...")

# ==========================================================
# Display Menu
# ==========================================================

def display_menu():

    print("\n" + "=" * 60)
    print("                     MAIN MENU")
    print("=" * 60)

    print("1. Search Weather")
    print("2. Exit")

# ==========================================================
# Get City Name
# ==========================================================

def get_city():

    city = input(
        "\nEnter city name: "
    ).strip()

    return city

# ==========================================================
# Get Weather Data
# ==========================================================

def get_weather(city):

    url = (
        f"{BASE_URL}"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    return response
# ==========================================================
# Display Weather
# ==========================================================

def display_weather(data):

    print("\n" + "=" * 60)
    print("                  WEATHER REPORT")
    print("=" * 60)

    city = data["name"]
    country = data["sys"]["country"]

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    wind_speed = data["wind"]["speed"]
    visibility = data["visibility"] / 1000

    clouds = data["clouds"]["all"]

    sunrise = datetime.fromtimestamp(
             data["sys"]["sunrise"]
        ).strftime("%I:%M %p")

    sunset = datetime.fromtimestamp(
             data["sys"]["sunset"]
               ).strftime("%I:%M %p")

    latitude = data["coord"]["lat"]

    longitude = data["coord"]["lon"]

    description = data["weather"][0]["description"].title()
    condition = data["weather"][0]["main"]

    if condition == "Clear":
        emoji = "☀"

    elif condition == "Clouds":
        emoji = "☁"

    elif condition == "Rain":
        emoji = "🌧"

    elif condition == "Thunderstorm":
        emoji = "⛈"

    elif condition == "Snow":
        emoji = "❄"

    elif condition in ["Mist", "Fog", "Haze"]:
        emoji = "🌫"

    else:
        emoji = "🌍"

    print(f"\n📍 Location      : {city}, {country}")
    print(f"🌡 Temperature   : {temperature:.1f}°C")
    print(f"🤗 Feels Like    : {feels_like:.1f}°C")
    print(f"💧 Humidity      : {humidity}%")
    print(f"🌬 Wind Speed    : {wind_speed} m/s")
    print(f"📈 Pressure      : {pressure} hPa")
    print(f"☁ Cloud Cover   : {clouds}%")
    print(f"👀 Visibility    : {visibility:.1f} km")
    print(f"🌅 Sunrise       : {sunrise}")
    print(f"🌇 Sunset        : {sunset}")
    print(f"📌 Latitude      : {latitude}")
    print(f"📌 Longitude     : {longitude}")
    print(f"{emoji} Condition     : {description}")

# ==========================================================
# Search Weather
# ==========================================================

def search_weather():

    city = get_city()

    if not city:

        print("\n❌ City name cannot be empty.")

        input("\nPress Enter to continue...")

        return

    response = get_weather(city)

    if response.status_code == 200:

        data = response.json()

        display_weather(data)

    else:

        print("\n❌ City not found.")

    input("\nPress Enter to continue...")
# ==========================================================
# Main Function
# ==========================================================

def main():

    welcome_screen()

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            search_weather()

        elif choice == "2":

            print("\nThank you for using Weather App! 👋")

            break

        else:

            print("\n❌ Invalid choice.")
            input("\nPress Enter to continue...")
# ==========================================================
# Run Program
# ==========================================================

if __name__ == "__main__":

    main()

