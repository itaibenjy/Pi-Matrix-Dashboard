from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from apps import gif_viewer
import pytz
from config import Config
from utils.text import textShade

class MainScreen:

    width = 64
    height = 32

    def __init__(self, gif) -> None:
        self.gif = gif_viewer.GifScreen(gif)
        self.font = ImageFont.FreeTypeFont('assets/fonts/tiny.otf', 10)
        self.timezone = pytz.timezone(Config.data['timezone'])
    

    def getFrame(self) -> None:
        frame = self.gif.getFrame()
        frame_copy = frame.copy()
        draw = ImageDraw.Draw(frame_copy)
        now = datetime.now(self.timezone)
        textShade(draw, "{:02}".format(now.hour), 4, 4, self.font);
        textShade(draw, "{:02}".format(now.minute), 4, 19, self.font);
        textShade(draw, "{:02}".format(now.day), 46, 4, self.font);
        textShade(draw, "{:02}".format(now.month), 46, 19, self.font);
        return frame_copy
    




    

