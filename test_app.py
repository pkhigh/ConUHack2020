import os
import requests
import json
import cv2 as cv
import numpy as np


IMAGEPATH = input("Enter full path of IMAGE TO TEST : ")
api = 'http://111.93.185.85:8082/car_type'

def drawBox(image,width,height,item):
    box = item['bounding_box']
    topLeft = (int(box['left']*width),
                int(box['top']*height))
    bottomRight = (int((box['left']+box['width'])*width),
                int((box['top']+box['height'])*height))
    temp = cv.rectangle(image, topLeft, bottomRight, (255,0,255), 2)
    cv.putText(img=image,
               text=str(item['class']),
               org=topLeft,
               fontFace=cv.FONT_HERSHEY_COMPLEX,
               fontScale=2,
               thickness=2,
               color=(255,0,0))



print('SENDING')  
files={'userPhoto':open(IMAGEPATH,'rb')}
r = requests.post(url = api, files = files) 
r_json = r.json()
if(r.status_code==200):
    img = cv.imread(IMAGEPATH,1)
    if hasattr(img, 'shape'):
        height,width=img.shape[:2]
        for item in r_json:
            drawBox(img,width,height,item)
        cv.imwrite('tmp.jpg',img) 
print('DONE')
cv.imshow("res", img);cv.waitKey();cv.destroyAllWindows()