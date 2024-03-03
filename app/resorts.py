import requests
from resorts_selection import find_nearest_resorts


class Resorts:
    """
    Description:
    """
    def __init__(self, city_name):
        """XXX"""
        self._weather_data = None
        while self._weather_data is None:
            self._weather_data = self._get_weather_data(city_name)
        self._city = city_name
        self._city_lat = self._weather_data['coord']['lat']
        self._city_lon = self._weather_data['coord']['lon']
        data_list = find_nearest_resorts(self._city_lat, self._city_lon)
        self._rating_1 = data_list[0][4]
        self._weather_data_1 = self._get_weather_data(0, data_list[0][3], data_list[0][4])
        self._temperature_1 = self._weather_data_1['main']['temp']
        self._description_1 = self._weather_data_1['weather'][0]['description']

    def _get_weather_data(self, city_name, lat=0, lon=0):
        """XXX"""
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        # Set up the parameters for the API request
        api_key = '9f6930e1d6505ed136bd2863a790dab8'
        if city_name != 0:
            params = {
                'q': city_name,
                'appid': api_key,
            }
        else:
            params = {
                'lat': lat,
                'lon': lon,
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

    def _get_ski_data(self, city_name):
        """XXX"""
        base_url = 'https://api.weatherunlocked.com/'
        app_id = 'fc992c67'

        # Set up the parameters for the API request
        resort_id = ''
        api_key = '682f0c84a538be674d9fda439ba005ae'
        params = {
            'resort_id': resort_id,
            'app_id': app_id,
            'app_key': api_key,
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

    def get_temperature(self):
        """XXX"""
        return self._temperature_1

    def get_description(self):
        """XXX"""
        return self._description_1

    def get_rating(self):
        """XXX"""
        return self._rating_1



# resorts_1 = Resorts('Indianapolis')
# print("hi")

    # def get_city(self):
    #     """XXX"""
    #     return self._city

    # def get_humidity(self):
    #     """XXX"""
    #     return self._humidity
    #
    # def get_speed(self):
    #     """XXX"""
    #     return self._speed
