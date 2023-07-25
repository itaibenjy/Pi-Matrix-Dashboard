#!/usr/bin/env python
import time
from PIL import Image
class GifScreen:

    width = 64
    height = 32

    def __init__(self, gif, delay) -> None:
        self.image_file = f"assets/images/{gif}"
        self.gif = Image.open(self.image_file)
        self.num_frames = self.gif.n_frames
        self.cur_frame = 0
        self.delay = delay
        self.preprocess()

    def preprocess(self) -> None:
        # Preprocess the gifs frames into canvases to improve playback performance
        self.images = []
        for frame_index in range(0, self.num_frames):
            self.gif.seek(frame_index)
            # must copy the frame out of the gif, since thumbnail() modifies the image in-place
            frame = self.gif.copy()
            frame.thumbnail((self.width, self.height), Image.ANTIALIAS)
            image = frame.convert("RGB")
            self.images.append(image)
        # Close the gif file to save memory now that we have copied out all of the frames
        self.gif.close()

    def getFrame(self):
        frame = self.images[self.cur_frame]
        time.sleep(self.delay)
        self.cur_frame += 1
        if self.cur_frame >= self.num_frames:
            self.cur_frame = 0
        return frame

