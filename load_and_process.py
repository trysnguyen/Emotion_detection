import pandas as pd
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor

dataset_path = 'fer2013/fer2013/fer2013.csv'
image_size = (48, 48)

def process_pixel_sequence(pixel_sequence):
    width, height = 48, 48
    face = [int(pixel) for pixel in pixel_sequence.split(' ')]
    face = np.asarray(face).reshape(width, height)
    face = cv2.resize(face.astype('uint8'), image_size)
    return face.astype('float32')

def load_fer2013():
    data = pd.read_csv(dataset_path)
    pixels = data['pixels'].tolist()

    with ThreadPoolExecutor() as executor:
        faces = list(executor.map(process_pixel_sequence, pixels))

    faces = np.asarray(faces)
    faces = np.expand_dims(faces, -1)
    emotions = pd.get_dummies(data['emotion']).to_numpy()
    return faces, emotions

def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x
