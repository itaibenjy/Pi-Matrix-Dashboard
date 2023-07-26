#!/usr/bin/env python
import time
import sys, os, inspect 
from config import Config
import argparse

currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir+"/rpi-rgb-led-matrix/bindings/python")

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from apps import main_screen
from develop import DeveloperWindow

# Parse command-line arguments
parser = argparse.ArgumentParser(description='LED Matrix display software.')
parser.add_argument('-d', '--dev-mode', action='store_true', help='Run in development mode (show image in a tkinter window instead of sending it to the LED matrix).')
args = parser.parse_args()


# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.pixel_mapper_config = "U-mapper;Rotate:180"

matrix = RGBMatrix(options = options)

penguinGif = main_screen.MainScreen(gif=Config.data['background'] ,delay=0.08)

# Create the develper window
if args.dev_mode:
    dev_window = DeveloperWindow()

try:
    print("Press CTRL-C to stop.")

    while(True):
        frame = penguinGif.getFrame()
        if args.dev_mode:
            # Display the frame in the image window
            dev_window.show_image(frame)
            dev_window.window.update()
        else:
            # Send the frame to the LED matrix
            matrix.SetImage(frame)

except KeyboardInterrupt:
    sys.exit(0)
