from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from apps import gif_viewer
import pytz

class MainScreen:

    width = 64
    height = 32

    def __init__(self, gif, delay) -> None:
        self.gif = gif_viewer.GifScreen(gif, delay)
        self.font = ImageFont.FreeTypeFont('assets/fonts/tiny.otf', 10)
        self.timezone = pytz.timezone('Asia/Jerusalem')
    

    def getFrame(self) -> None:
        frame = self.gif.getFrame()
        frame_copy = frame.copy()
        draw = ImageDraw.Draw(frame_copy)
        now = datetime.now(self.timezone)
        self.drawShade(draw, now.hour, 4, 4);
        self.drawShade(draw, now.minute, 4, 19);
        self.drawShade(draw, now.day, 46, 4);
        self.drawShade(draw, now.month, 46, 19);
        return frame_copy
    

    def drawShade(self, draw, text , x, y) -> None:
        border_color = (40,40,40)

        # Draw Shade to Draw border add [1,-1,0] to make it all sides 
        for x_offset in [1]:
            for y_offset in [1]:
                draw.text((x + x_offset, y + y_offset), str(text), font=self.font, fill=border_color)
        
        # Draw text on top of border
        draw.text((x, y), str(text), font=self.font)



    

