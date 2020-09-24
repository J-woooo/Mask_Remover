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

import os, io
from google.cloud import vision
import pandas as pd
import io
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from PIL import Image, ImageDraw
import test

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'calcium-circuit-288507-3bd5d45e277c.json'

client = vision.ImageAnnotatorClient()

file_name = 'origin.jpg'
img = cv2.imread(file_name)
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
image = vision.types.Image(content=content)
response = client.face_detection(image=image)
faceAnnotations = response.face_annotations

for face in faceAnnotations:
    vertices = face.bounding_poly.vertices
    face_vertices = ['({0},{1})'.format(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
    index = [face_vertices[0].split(',')[0][1:],face_vertices[0].split(',')[1][:-1],face_vertices[2].split(',')[0][1:],face_vertices[2].split(',')[1][:-1]]
    img_face = img[int(index[1]):int(index[3]),int(index[0]):int(index[2])]
    cv2.imwrite('images/output_cv.jpg', img_face)
    size = (vertices[1].x-vertices[0].x, vertices[3].y-vertices[0].y)

    test.inpainting()

    template = Image.open("origin.jpg") 
    rgb_im = template.convert('RGB')
    logo = Image.open("mask/mask.png")
    resized_logo = logo.resize(size)
    rgb_im.paste(resized_logo, (vertices[0].x, vertices[0].y))
    rgb_im.save("origin.jpg", "jpg")
    #rgb_im.show()
