import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

class DeveloperWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('400x200')
        self.label = tk.Label(self.window, bg='black')  # set label background to black
        self.window.title("Developer Mode - LED Matrix Simulator")
        self.window.update()
        # Use grid layout manager and set the label to expand
        self.label.grid(sticky='nsew')
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)


    def show_image(self, image):
        # Convert the image to a PIL Image, then to a Tkinter PhotoImage
        image = Image.fromarray(np.array(image))
        # make sure the width is event
        width = self.window.winfo_width() if self.window.winfo_width() % 2 == 0 else self.window.winfo_width() - 1
        height = self.window.winfo_height() 

        # upscale the image to the width of the window while preserving the aspect ratio and pixelation for the matrix effect
        if width > 2*height:
            image = image.resize((self.window.winfo_height()*2, self.window.winfo_height()), Image.NEAREST)
        else: 
            image = image.resize((self.window.winfo_width(), self.window.winfo_width()//2 ), Image.NEAREST)
        self.photo = ImageTk.PhotoImage(image)

        # Update the label to show the new image
        self.label.config(image=self.photo)
        self.window.update_idletasks()


    def mainloop(self):
        self.window.mainloop()
