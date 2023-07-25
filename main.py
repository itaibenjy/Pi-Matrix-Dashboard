#!/usr/bin/env python
import time
import sys, os, inspect 


currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir+"/rpi-rgb-led-matrix/bindings/python")

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from apps import main_screen

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.pixel_mapper_config = "U-mapper;Rotate:180"

matrix = RGBMatrix(options = options)

penguinGif = main_screen.MainScreen(gif="penguin.gif" ,delay=0.08)

try:
    print("Press CTRL-C to stop.")

    while(True):
        frame = penguinGif.getFrame()
        matrix.SetImage(frame)

except KeyboardInterrupt:
    sys.exit(0)
