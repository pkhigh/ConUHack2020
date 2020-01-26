from flask import Flask, request, jsonify
import requests
import cv2
import numpy as np
import imutils
from datetime import *
import os



def parse_incoming_files(files):
    buf_res = {}
    for file_obj in files.getlist('userPhoto'):
        name = file_obj.filename
        buf_res['image_buf'] = file_obj
    return buf_res


def get_valid_image(image_content):
    img = cv2.imdecode(np.asarray(bytearray(image_content), dtype=np.uint8), 1)
    if img is not None:
        return img
    return None


def get_image(files):
    image = None
    try:
        image_content = parse_incoming_files(files)['image_buf'].read()
        image = get_valid_image(image_content)
    except Exception as e:
        print('Invalid Image content :',e)
    return image