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
    data = get_city_name()
    weather_data = get_weather_data()


def get_city_name():
    """XXX"""
    city = input("What city to ski?: ")
    api_key = '9f6930e1d6505ed136bd2863a790dab8'
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'
    data = make_api_call(url)
    return data


def get_weather_data(lat, lon):
    """XXX"""
    api_key = '9f6930e1d6505ed136bd2863a790dab8'
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}'


def make_api_call(url):
    """XXX"""
    r = requests.get(url)
    print("Status code:", r.status_code)

    # Process information about each submission.
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # Make a separate API call for each submission.
        url = ('https://hacker-news.firebaseio.com/v0/item/' +
               str(submission_id) + '.json')
        submission_r = requests.get(url)
        print(submission_r.status_code)
        response_dict = submission_r.json()

        submission_dict = {
            'title': response_dict['title'],
            'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
            'comments': response_dict.get('descendants', 0)
        }
        submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                              reverse=True)

    for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])


if __name__ == '__main__':
    main()
