# go to openweathermap.org, log in (or create an account),
# and under API find 5 days/3 hours weather forecast
# find API call text and copy
# it is: api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={APIkey}
# then find your API key in your user account info
# here I write the API key used in the lection

import requests

API_KEY = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place_local, days_local=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place_local}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    # the data has values for every 3 hours, that is, 8 values for 1 day
    nr_values = 8 * days_local
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place_local="Tokyo", days_local=3))