import time
import cv2
import numpy as np
import math

pixels = np.zeros((16, 16, 3), dtype=np.uint8)
width = 16
height = 16

def brighten(v):
    return 256 - 256/(v+1)

def show():
    accurate=pixels.copy()
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            accurate[i][j] = (brighten(pixels[i][j][0]), brighten(pixels[i][j][1]), brighten(pixels[i][j][2]))
    accurate = cv2.cvtColor(accurate, cv2.COLOR_RGB2BGR)
    accurate = cv2.resize(accurate, (1024, 1024), interpolation=cv2.INTER_NEAREST)
    cv2.imshow('Display', accurate)
    
    cv2.resizeWindow('Display', 1024, 1024)
    cv2.waitKey(1)
    time.sleep(0.001)

def set_xy(pixel: tuple, color: tuple):
    pixels[pixel] = color

#def set_i(pixel: int, color: tuple):
#    pixels[pixel] = color

def set_m(pixel_list: list):
    for pixel in pixel_list:
        pixels[pixel] = pixel.rgb
    show()

def fill(color: tuple):
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j] = color
    show()

def fade(color: tuple):
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            new = (pixels[i][j][0]*color[0], pixels[i][j][1]*color[1], pixels[i][j][2]*color[2])
            pixels[i][j] = new
    show()

def max_value() -> int:
    max_p = max(range(len(pixels)), key=lambda i: pixels[i][0]+pixels[i][1]+pixels[i][2])
    return max_p, pixels[max_p]