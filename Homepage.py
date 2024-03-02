# Makes HTTP Requests in Python
import requests

# Used to retrieve items from an iterable object
from operator import itemgetter

# Make an API call, and store the response.

def main():
    """
    Description: Main function for program.

    :returns: Void
    """
    lat, long get_city_name()
    lat = input("What latitude?" )
    long = input("What longitude?")



def make_api_call():
    """XXX"""
    key = '9f6930e1d6505ed136bd2863a790dab8'

    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'
    r = requests.get(url)
    print("Status code:", r.status_code)

if __name__ == '__main__':
    main()
