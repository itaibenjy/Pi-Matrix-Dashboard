#!/usr/bin/env python
import time
import sys, os, inspect 
from config import Config
import argparse

currentdir = os.getcwd()
sys.path.append(os.path.join(currentdir,"rpi-rgb-led-matrix","bindings","python"))

from apps import main_screen, weather_screen
from develop import DeveloperWindow

# Parse command-line arguments
parser = argparse.ArgumentParser(description='LED Matrix display software.')
parser.add_argument('-d', '--dev-mode', action='store_true', help='Run in development mode (show image in a tkinter window instead of sending it to the LED matrix).')
args = parser.parse_args()

penguinGif = main_screen.MainScreen(gif=Config.data['background'])
weather = weather_screen.WeatherScreen()


# Run in development mode
if(args.dev_mode):
    print("Running in development mode.")
    dev_window = DeveloperWindow()

    try:
        print("Press CTRL-C to stop.")

        while(True):
            frame = weather.getFrame()
            dev_window.show_image(frame)
            dev_window.window.update()
            time.sleep(0.08) 

        dev_window.window.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)


# Run in regular mode
try:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions
except ModuleNotFoundError:
    print("Could not find the rpi-rgb-led-matrix library. Please follow the installation instructions (maybe you need to run 'make' command) at github or run in developer mode")
    sys.exit(1)

    

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.pixel_mapper_config = "U-mapper;Rotate:180"

matrix = RGBMatrix(options = options)


try:
    print("Press CTRL-C to stop.")

    while(True):
        frame = weather.getFrame()

        # Send the frame to the LED matrix
        matrix.SetImage(frame)
        time.sleep(0.08) 

except KeyboardInterrupt:
    sys.exit(0)
