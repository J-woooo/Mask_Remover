import os, io
from google.cloud import vision
import pandas as pd
import io
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from PIL import Image, ImageDraw

def drawVertices(image_source, vertices, display_text=''):
    pillow_img = Image.open(io.BytesIO(image_source))

    draw = ImageDraw.Draw(pillow_img)
    for i in range(len(vertices) - 1):
        draw.line(((vertices[i].x, vertices[i].y), (vertices[i + 1].x, vertices[i + 1].y)),
                fill='blue',
                width=8
        )

    draw.line(((vertices[len(vertices) - 1].x, vertices[len(vertices) - 1].y),
               (vertices[0].x, vertices[0].y)),
               fill='blue',
               width=8
    )

    font = ImageFont.truetype('arial.ttf', 16)
    draw.text((vertices[0].x + 10, vertices[0].y),
              font=font, text=display_text, 
              fill=(255, 255, 255))

def crop(file_name, vertice):
    img = Image.open(file_name)
    area = (vertices[0].x, vertices[0].y, vertices[1].x, vertices[3].y)
    cropped_img = img.crop(area)
    
    #cropped_img.show()
    
    return cropped_img


def processing(cropped_image):
    image_shape = (cropped_img.height, cropped_img.width)
    img_data = np.empty((image_shape[0], image_shape[1], 3),dtype=np.float)
    img_data= np.array(img_data, dtype=np.double)
    return img_data
