import random
from config import Config
from connections.weather_connection import WeatherUpdater
from PIL import Image, ImageDraw, ImageFont
from utils.text import textShade


weather_background = (0,0,0)
drops_color = (1,106,175)
high_temp_color = (200,0,0)
low_temp_color = (0,0,2000)

class WeatherScreen:

    def __init__(self) -> None:
        self.weather = Config.data['weather']
        self.cities = self.weather['cities']
        self.api_key = self.weather['api_key']
        self.current_city = 0
        
        self.weather_updaters = [WeatherUpdater(self.api_key, city) for city in self.cities]

    def getFrame(self) -> Image.Image:
        frame = Image.new("RGBA", (Config.data["matrix"]["width"], Config.data["matrix"]["height"]), weather_background)
        draw = ImageDraw.Draw(frame)
        self.drawWeather(draw, frame)
        return frame
    
    def drawWeather(self, draw, frame) -> None:
        font = ImageFont.truetype('assets/fonts/tiny.otf', 5)
        data = self.weather_updaters[self.current_city].weather_data
        #data = {"name": "Karmiel", "current_temp": 25, "low_temp": 15, "high_temp": 31, "rain": 0.15, "is_rain": False, "icon_name": "01d"}
        if not data:
            return

        if data['is_rain']:
            self.randomRain(draw);

        # Draw Icon image
        icon = Image.open(f"assets/weather/{data['icon_name']}.png").convert("RGBA")
        # Resize icon to 20 height and keep aspect ratio
        frame.alpha_composite(icon, (38, 5))

        # Draw City Name Icon and Weather
        draw.text((3, 4), data['name'], font=font)
        draw.text((3, 12), str(data['low_temp']), low_temp_color, font=font)
        draw.text((13, 12), str(data['current_temp']),  font=font)
        draw.text((23, 12), str(data['high_temp']), high_temp_color, font=font)
        draw.text((3, 20), "RAIN", font=font)
        draw.text((21, 20), f"{int(data['rain']*100)}%", font=font)
        
    
    def randomRain(self, draw) -> None:
        drops = []
        for i in range(0, 10):
            drops.append((random.randint(0, 64), random.randint(0, 32)))
        draw.point(drops, drops_color)





