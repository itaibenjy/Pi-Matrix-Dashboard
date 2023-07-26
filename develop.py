import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

class DeveloperWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.label = tk.Label(self.window)
        self.label.pack()

    def show_image(self, image):
        # Convert the image to a PIL Image, then to a Tkinter PhotoImage
        image = Image.fromarray(np.array(image))
        photo = ImageTk.PhotoImage(image)

        # Update the label to show the new image
        self.label.config(image=photo)

    def mainloop(self):
        self.window.mainloop()
