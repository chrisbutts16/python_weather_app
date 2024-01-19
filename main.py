import requests


api_key = '2c518ce69111fb944da12a19d8885a0a'

city_name = input("Enter city name: ")

# requests allow us to simulate website and receive contents
url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'

url2 = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # checks if  data is a  list & contains at least one item
    if isinstance(data, list) and len(data) > 0:
        city_data = data[0]

        # extract temp & description
        if 'lat' in city_data and 'lon' in city_data and 'country' in city_data:
            print(f'City: {city_data["name"]}, Country: {city_data["country"]}')
            lat={city_data["lat"]}
            lon={city_data["lon"]}
            part = 'alerts'
            API_key= '9b5297fd3b2e86e2a4ea3a384845a3be'
            print(f'Latitude: {city_data["lat"]}, Longitude: {city_data["lon"]}')

            response2 = requests.get(url2)
            
            if response2.status_code == 200:
                data = response2.json()
                if isinstance(data, list) and len(data) > 0:
                    weatherData = data[0]
                    if 'current' in weatherData and 'weather' in weatherData:
                        print(f'current weather: {weatherData["current"]}, Weather: {weatherData["weather"]}')
                    else:
                        print('Error: Missing required information in the response.')
                else:
                    print('Error: No data or unexpected data structure in the response.')
            else:
                print(f'Error fetching weather data. Status Code: {response.status_code}')
        else:
            print('Error: Missing required information in the response.')
    else:
        print('Error: No data or unexpected data structure in the response.')
else:
    print(f'Error fetching weather data. Status Code: {response.status_code}')
