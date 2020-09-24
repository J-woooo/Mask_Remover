import os, io
from google.cloud import vision
import pandas as pd
import io
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from PIL import Image, ImageDraw
import detection_func

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
    img_face = cv2.resize(img_face,(256,256))
    cv2.imwrite('images/output_cv.jpg', img_face)
    size = (vertices[1].x-vertices[0].x, vertices[3].y-vertices[0].y)
