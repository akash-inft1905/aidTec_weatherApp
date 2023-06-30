import requests
import json

API_KEY = 'df1d5a0cdd2a977e788cdb9217f320a6'
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

# Function to get the current weather data
def get_weather(location):
    url = f'{BASE_URL}weather?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)

    if data['cod'] == '404':
        print('Location not found. Please try again.')
        return

    print('Current Weather Data:')
    print('---------------------')
    print(f'Location: {data["name"]}, {data["sys"]["country"]}')
    print(f'Temperature: {data["main"]["temp"]}°C')
    print(f'Humidity: {data["main"]["humidity"]}%')
    print(f'Wind Speed: {data["wind"]["speed"]} m/s')
    print(f'Weather Condition: {data["weather"][0]["description"]}')

# Function to get the weather forecast
def get_forecast(location):
    url = f'{BASE_URL}forecast?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)

    if data['cod'] == '404':
        print('Location not found. Please try again.')
        return

    print('Weather Forecast:')
    print('-----------------')
    for forecast in data['list']:
        date = forecast['dt_txt'].split()[0]
        time = forecast['dt_txt'].split()[1]
        temp = forecast['main']['temp']
        weather = forecast['weather'][0]['description']
        print(f'Date: {date}, Time: {time}, Temperature: {temp}°C, Weather: {weather}')

# Function to save a location
def save_location(location):
    with open('saved_locations.txt', 'a') as file:
        file.write(location + '\n')
    print(f'Location "{location}" saved successfully.')

# Function to view saved locations
def view_saved_locations():
    try:
        with open('saved_locations.txt', 'r') as file:
            locations = file.readlines()
            if not locations:
                print('No saved locations.')
            else:
                print('Saved Locations:')
                print('----------------')
                for location in locations:
                    print(location.strip())
    except FileNotFoundError:
        print('No saved locations.')

# Main program loop
while True:
    print('\nWeather App')
    print('-----------')
    print('1. Get Current Weather')
    print('2. Get Weather Forecast')
    print('3. Save Location')
    print('4. View Saved Locations')
    print('5. Quit')

    choice = input('Enter your choice (1-5): ')

    if choice == '1':
        location = input('Enter location: ')
        get_weather(location)
    elif choice == '2':
        location = input('Enter location: ')
        get_forecast(location)
    elif choice == '3':
        location = input('Enter location: ')
        save_location(location)
    elif choice == '4':
        view_saved_locations()
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')
