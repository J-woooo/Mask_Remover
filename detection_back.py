import os, io
from google.cloud import vision
import pandas as pd
import io
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from PIL import Image, ImageDraw
import detection_func

template = Image.open("origin.jpg")   
rgb_im = template.convert('RGB')
logo = Image.open('results/output_cv_out_0.png')
resized_logo = logo.resize(size)
rgb_im.paste(resized_logo, (vertices[0].x, vertices[0].y))
rgb_im.save("origin.jpg", "JPEG")
#rgb_im.show()