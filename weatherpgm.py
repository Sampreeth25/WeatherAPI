import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"

def get_weather_forecast(city):
    response = requests.get(API_URL, params={"q": city, "appid": API_KEY})
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Error fetching weather data.")
        return []

def get_temperature(weather_data, target_date):
    for data in weather_data:
        if data["dt_txt"].startswith(target_date):
            return data["main"]["temp"]
    return None

def get_wind_speed(weather_data, target_date):
    for data in weather_data:
        if data["dt_txt"].startswith(target_date):
            return data["wind"]["speed"]
    return None

def get_pressure(weather_data, target_date):
    for data in weather_data:
        if data["dt_txt"].startswith(target_date):
            return data["main"]["pressure"]
    return None

def main():
    city = input("Enter city name: ")
    weather_data = get_weather_forecast(city)
    
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            break
        elif choice == 1:
            date = input("Enter date (YYYY-MM-DD): ")
            temperature = get_temperature(weather_data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature} K")
            else:
                print("Data not found for the specified date.")
        elif choice == 2:
            date = input("Enter date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found for the specified date.")
        elif choice == 3:
            date = input("Enter date (YYYY-MM-DD): ")
            pressure = get_pressure(weather_data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found for the specified date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
