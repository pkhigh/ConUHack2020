import cv2
import numpy as np


import sys
from hardConstants import *

class BOX:
    height = 0
    top = 0
    width = 0
    left = 0
    label = ''
    score = ''
    mask = None
    area = None

def suppressClassWiseConfidence(detectedBoxList):
    newdetectedBoxList = []
    for ObjectBox in detectedBoxList:
        if ObjectBox.score >= thresh:
            newdetectedBoxList.append(ObjectBox)
    return newdetectedBoxList

def bb_intersection_over_union(box1,box2):
    boxA = [box1.left, box1.top, box1.left+box1.width, box1.top+box1.height]
    boxB = [box2.left, box2.top, box2.left+box2.width, box2.top+box2.height]
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou

def reducedCounter(contours):
    largest_area=0
    largest_contour_index=0
    
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if (area>largest_area):
            largest_area=area
            largest_contour_index=i
    cnt = contours[largest_contour_index]
    epsilon = POLYGON_APPROZIMATION_EPSILON
    cnt = cv2.approxPolyDP(cnt,epsilon,True)
    return(cnt)

def getImageBox(image):
    image_height,image_width,channel = image.shape
    imageBox = BOX()
    imageBox.label = 'Image'
    imageBox.score = 1
    imageBox.height = image_height
    imageBox.width = image_width
    imageBox.left = 0
    imageBox.top = 0
    return imageBox    
    
def boxesIntersect(box1,box2):
    X1 = box1.left
    Y1 = box1.top
    W1 = box1.width
    H1 = box1.height

    X2 = box2.left
    Y2 = box2.top
    W2 = box2.width
    H2 = box2.height
    if (X1+W1<X2 or X2+W2<X1 or Y1+H1<Y2 or Y2+H2<Y1):
        return False
    else:
        return True

def displayBox(ObjectBox):
    print(ObjectBox.label,ObjectBox.score,ObjectBox.height,ObjectBox.width,ObjectBox.left,ObjectBox.top)
def displayBoxList(BOXES):
    for ObjectBox in BOXES:
        displayBox(ObjectBox)
    
def generatebox(detection):
    ObjectBox = BOX()
    ObjectBox.label = detection[0]
    ObjectBox.score = detection[1]
    ObjectBox.height = float(detection[2][3])
    ObjectBox.width = float(detection[2][2])
    ObjectBox.left = float(detection[2][0]) - ObjectBox.width/2
    ObjectBox.top = float(detection[2][1]) - ObjectBox.height/2
    return ObjectBox

def generateBoxes(BOXES,detections):
    for detection in detections:
        BOXES.append(generatebox(detection))
    return BOXES

def normalizebox(ObjectBox,image):
    image_height,image_width,channel = image.shape
    ObjectBox.height = ObjectBox.height/image_height
    ObjectBox.width = ObjectBox.width/image_width
    ObjectBox.left = ObjectBox.left/image_width
    ObjectBox.top = ObjectBox.top/image_height
    if ObjectBox.mask is not None:
        ObjectBox.mask = ObjectBox.mask.astype('float64')
        for point in ObjectBox.mask:
            point[0][0] = point[0][0]/image_width
            point[0][1] = point[0][1]/image_height   
    ObjectBox.area = ObjectBox.area/(image_width*image_height)
    return ObjectBox
    
def normalizeBoxes(BOXES,image):
    for ObjectBox in BOXES:
        ObjectBox = normalizebox(ObjectBox,image)
    return BOXES

def makeSubBox(superBox,subBox):
    subBox.left = float(max(subBox.left,superBox.left))
    subBox.top = float(max(subBox.top,superBox.top))
    if (subBox.height + subBox.top > superBox.height + superBox.top):
        subBox.height = float(superBox.height + superBox.top - subBox.top)
    if(subBox.width + subBox.left > superBox.width + superBox.left):
        subBox.width = float(superBox.width + superBox.left - subBox.left)  
    return subBox

def getBoxesIn(BOXES,image_height,image_width):
    if len(BOXES) > 0:
        ImageBox = BOX()
        ImageBox.height = image_height
        ImageBox.width = image_width
        for index in range(len(BOXES)):
            ObjectBox = BOXES[index]
            BOXES[index] = makeSubBox(ImageBox,ObjectBox)  
    return BOXES

def annotate(image,BOXES,imageWritePath):
    image_height,image_width,channel = image.shape
    if len(BOXES) > 0:
        for ObjectBox in BOXES:
            colorToUse = (255,0,255)
            if ObjectBox.mask is not None:
                mask = []
                for point in ObjectBox.mask:
                    maskPoint = []
                    maskPoint.append(point[0][0]*image_width)
                    maskPoint.append(point[0][1]*image_height)
                    mask.append(maskPoint)
                mask = np.array(mask)
                mask = mask.astype('int')
                cv2.drawContours(image,[mask],-1,colorToUse,2)
                topLeft = (int(ObjectBox.left*image_width),int(ObjectBox.top*image_height))
                cv2.putText(image,
                            str(ObjectBox.label) + ':' + str(ObjectBox.score),
                            topLeft,cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            1,
                            colorToUse)
            else:
                topLeft = (int(ObjectBox.left*image_width),int(ObjectBox.top*image_height))
                bottomRight = (int((ObjectBox.left+ObjectBox.width)*image_width),
                               int((ObjectBox.top+ObjectBox.height)*image_height))
                temp = cv2.rectangle(image, topLeft, bottomRight, colorToUse, 2)
                cv2.putText(image,
                            str(ObjectBox.label) + ':' + str(ObjectBox.score),
                            topLeft,cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            1,
                            colorToUse)

    cv2.imwrite(imageWritePath,image)
 
def consolidate_data(BOXES):
    FinalListOfDetections = []
    if len(BOXES) > 0:
        for ObjectBox in BOXES:
            manual = {}
            manual['class'] = ObjectBox.label
            manual['score'] = round(ObjectBox.score,2)
            manual['bounding_box'] = {
                                    'left': round(ObjectBox.left,2),
                                    'top': round(ObjectBox.top,2),
                                    'width': round(ObjectBox.width,2),
                                    'height': round(ObjectBox.height,2)
                                    }
            if ObjectBox.area is not None:
                manual['area'] = round(ObjectBox.area,4) 
            if ObjectBox.mask is not None:
                manual['polygon'] = []
                for point in ObjectBox.mask:
                    maskPoint = [round(float(point[0][0]),2),round(float(point[0][1]),2)]
                    manual['polygon'].append(maskPoint)
            FinalListOfDetections.append(manual)
    return FinalListOfDetections 

def addLitUnlitFlag(jsonList):
    if len(jsonList) > 0:
        for detection in jsonList:
            if detection['class'] == 'UnlitPhone':
                detection['class'] = 'Phone'
                detection['Screen_ON'] = 0
            elif detection['class'] == 'LitPhone':
                detection['class'] = 'Phone'
                detection['Screen_ON'] = 1
    return jsonList

def getBoxListfromJsonList(jsonList):
    boxList = []
    if len(jsonList) > 0:
        for detection in jsonList:
            ObjectBox = BOX()
            ObjectBox.label = detection['class']
            ObjectBox.score = detection['score']
            ObjectBox.height = detection['bounding_box']['height']
            ObjectBox.width = detection['bounding_box']['width']
            ObjectBox.left = detection['bounding_box']['left']
            ObjectBox.top = detection['bounding_box']['top']
            ObjectBox.area = detection['area']
            if 'polygon' in detection:
                ObjectBox.mask = []
                for point in detection['polygon']:
                    maskPoint = []
                    maskPoint.append(point[0])
                    maskPoint.append(point[1])
                    ObjectBox.mask.append([maskPoint])
                ObjectBox.mask = np.array(ObjectBox.mask)
            boxList.append(ObjectBox)
    return boxList

def highestScoringBox(detectedBoxList):
    hsb = None
    for ObjectBox in detectedBoxList:
        if hsb is None:
            hsb = ObjectBox
        elif ObjectBox.score > hsb.score:
            hsb = ObjectBox
    return hsb

def sortBoxList(detectedBoxList):
    new_list = []
    while detectedBoxList:
        maximum = detectedBoxList[0]
        for x in detectedBoxList:
            if x.score > maximum.score:
                maximum = x
        new_list.append(maximum)
        detectedBoxList.remove(maximum)
    return new_list

def highestScoringPhoneBox(detectedBoxList):
    PhoneBox = None
    for ObjectBox in detectedBoxList:
        if ObjectBox.label == 'Phone':
            if PhoneBox is None:
                PhoneBox = ObjectBox
            elif ObjectBox.score > PhoneBox.score:
                PhoneBox = ObjectBox
    return PhoneBox

def removeMultiplePhoneBoxes(detectedBoxList):
    boxList = []
    PhoneBox = highestScoringPhoneBox(detectedBoxList)
    if PhoneBox is None:
        return boxList
    else:
        boxList.append(PhoneBox)
        for ObjectBox in detectedBoxList:
            ObjectBox.score = round(ObjectBox.score,2)
            if ObjectBox.label == 'Phone':
                continue
            else:
                if boxesIntersect(PhoneBox,ObjectBox):
                    ObjectBox = makeSubBox(PhoneBox,ObjectBox)
                    boxList.append(ObjectBox)
    return boxList

def getsubImage(subBox,image):
    topLeft = (int(subBox.left),int(subBox.top))
    bottomRight = (int((subBox.left+subBox.width)),int((subBox.top+subBox.height)))
    roi = image[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]]
    roi = np.copy(roi)
    return roi


def updateContourCoordinates(contour,ObjectBox):
    for count in contour:
        count[0][0] += ObjectBox.left 
        count[0][1] += ObjectBox.top
    return contour

def centralizeBoxes(BOXES,PhoneBox):
    if len(BOXES) > 0:
        for ObjectBox in BOXES:
            ObjectBox.left = ObjectBox.left + PhoneBox.left
            ObjectBox.top = ObjectBox.top + PhoneBox.top
            if ObjectBox.mask is not None:
                ObjectBox.mask = updateContourCoordinates(ObjectBox.mask,PhoneBox)
    return BOXES