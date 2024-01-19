import requests

api_key = '2c518ce69111fb944da12a19d8885a0a'

city_name = input("Enter city name: ")

# requests allow us to simulate website and receive contents
url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # checks if  data is a  list & contains at least one item
    if isinstance(data, list) and len(data) > 0:
        city_data = data[0]

        # extract temp & description
        if 'lat' in city_data and 'lon' in city_data and 'country' in city_data:
            print(f'City: {city_data["name"]}, Country: {city_data["country"]}')
            print(f'Latitude: {city_data["lat"]}, Longitude: {city_data["lon"]}')
            print (cityWeather)

        else:
            print('Error: Missing required information in the response.')
    else:
        print('Error: No data or unexpected data structure in the response.')
else:
    print(f'Error fetching weather data. Status Code: {response.status_code}')