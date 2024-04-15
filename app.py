import requests

api_key = '6ca529e338d567026114b8c31b4188c8'

user_input = input("Enter City: ")

base_url = "http://api.openweathermap.org/data/2.5/weather"

params = {
    'q': user_input,
    'appid': api_key,
    'units': 'matric'
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()

#print(response.json())

    city_name = data['name']
    temprature = data['main']['temp']
    weather_description = data['weather'][0]['description']

    print(f"City Name: {city_name}")
    print(f"Temprature: {temprature}")
    print(f"Weather: {weather_description}")

else:
    print("Error: {response.status_code} - Unable to get weather data for {user_data}. Please enter correct input")
