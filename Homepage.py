import requests


def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Set up the parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
    }

    # Make the API call
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")
        return None


def main():
    api_key = '9f6930e1d6505ed136bd2863a790dab8'

    # Input the city name
    city_name = input("Enter the city name: ")

    # Get weather data
    weather_data = get_weather(api_key, city_name)

    # Display the result
    if weather_data:
        print("\nWeather Information for", city_name)
        print("Temperature:", weather_data['main']['temp'], "K")
        print("Weather Condition:", weather_data['weather'][0]['description'])
        print("Humidity:", weather_data['main']['humidity'], "%")
        print("Wind Speed:", weather_data['wind']['speed'], "m/s")
    else:
        print("Failed to retrieve weather information.")


if __name__ == "__main__":
    main()
