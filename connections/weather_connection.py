import requests
import threading

class WeatherUpdater:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city
        self.base_url = "https://api.openweathermap.org/data/3.0/onecall"
        self.current_url = "https://api.openweathermap.org/data/2.5/weather"
        self.weather_data = {}
        self.update_weather()
        threading.Timer(600, self.update_current).start()  # schedule next simple update in 10 minutes (600 seconds)

    def update_weather(self):
        print(self.city)
        params = {
            'appid': self.api_key,
            'lon': self.city['lon'],
            'lat': self.city['lat'],
            'units': 'metric'  # you can change this to 'imperial' for Fahrenheit
        }
        # use open weather auth 
        response = requests.get(self.base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            self.weather_data = {
                'name': self.city["name"],
                'low_temp': int(data['daily'][0]['temp']['min']),
                'high_temp': int(data['daily'][0]['temp']['max']),
                'current_temp': int(data['current']['temp']),
                'is_rain': data['current']['weather'][0]['main'] == 'Rain',
                'rain': data['daily'][0]['pop'],
                'icon_name': data['current']['weather'][0]['icon'],
            }
        else:
            print(f'Error fetching weather data: {data["message"]}')
        threading.Timer(600*6, self.update_weather).start()  # schedule next update in 60 minutes (600*6 seconds)
    
    def update_current(self):
        params = {
            'q': self.city,
            'appid': self.api_key,
            'units': 'metric'  # you can change this to 'imperial' for Fahrenheit
        }
        response = requests.get(self.current_url, params=params)
        data = response.json()
        if response.status_code == 200:
            self.weather_data['current_temp'] = data['main']['temp']
            self.weather_data['is_rain'] = data['weather'][0]['main'] == 'Rain'
        else:
            print(f'Error fetching weather data: {data["message"]}')
        threading.Timer(600, self.update_current).start()

    def get_weather_data(self):
        return self.weather_data
