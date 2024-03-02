import requests


class Resort:
    """
    Description:
    """
    def __init__(self, city_name):
        """XXX"""
        self._weather_data = None
        while self._weather_data is None:
            self._weather_data = self._get_weather_data(city_name)
        self._city = city_name
        self._temperature = temperature = self._weather_data['main']['temp']
        self._description =  self._weather_data['weather'][0]['description']
        self._humidity = self._weather_data['main']['humidity']
        self._speed = self._weather_data['wind']['speed']

    def _get_weather_data(self, city_name):
        """XXX"""
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        # Set up the parameters for the API request
        api_key = '9f6930e1d6505ed136bd2863a790dab8'
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
            print(f"Error: Unable to fetch weather data. Status Code: Try again.")
            return None

    def get_city(self):
        """XXX"""
        return self._city

    def get_temperature(self):
        """XXX"""
        return self._temperature

    def get_description(self):
        """XXX"""
        return self._description

    def get_humidity(self):
        """XXX"""
        return self._humidity

    def get_speed(self):
        """XXX"""
        return self._speed
