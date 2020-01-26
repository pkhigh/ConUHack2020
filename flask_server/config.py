import sys
sys.path.insert(0, '..')

from otherUtils.dataParsingFunctions import *
from otherUtils.BoxesFunctions import *
from mainServer.hardConstants import *

#sys.path.insert(0, '/home/rajesh/MobileWork/mobile_insurance_fraud_detection/Src')
#from detectObstruction import *


def getDatafromLocalServer(image,api):
    ret = {}
    _,img_encoded = cv2.imencode('.jpg', image)
    try:
        r = requests.post(url = api, files = {'userPhoto': img_encoded.tostring() })
        return r.json()
    except:
        return {}

def shutOutwardPixels(image,contour):
    mask = np.zeros(image.shape,np.uint8)
    contour = contour.astype('int')
    mask = cv2.drawContours(mask,[contour],-1,(1,1,1),-1)
    image = np.multiply(image, mask)
    return image


def removeRedundantPhoneBoxes(phoneBoxList):
    phoneBoxList = sortBoxList(phoneBoxList)
    newphoneBoxList = []
    for ObjectBox in phoneBoxList:
        add = True
        for otherBox in newphoneBoxList:
            if bb_intersection_over_union(ObjectBox,otherBox) > PHONE_nms:
                add = False
                break
        if add:
            newphoneBoxList.append(ObjectBox)
    return newphoneBoxList

    
def getCombinedResponse(image):
    detectionBoxList = []
    phoneResponse = getDatafromLocalServer(image,PHONE_API)
    phoneBoxList = getBoxListfromJsonList(phoneResponse)
    phoneBoxList = removeRedundantPhoneBoxes(phoneBoxList)
    detectionBoxList += phoneBoxList
    for phoneBox in phoneBoxList:
        phoneImage = np.copy(image)
        if phoneBox.mask is not None:
            phoneImage = shutOutwardPixels(phoneImage,phoneBox.mask)
        phoneImage = getsubImage(phoneBox,phoneImage)
        damageResponse = getDatafromLocalServer(phoneImage,DAMAGE_API)
        damageBoxList = getBoxListfromJsonList(damageResponse)
        #annotate(phoneImage,normalizeBoxes(damageBoxList,phoneImage),ANNOTATED_TEMP_DAM_IMG)
        damageBoxList = centralizeBoxes(damageBoxList,phoneBox)
        detectionBoxList += damageBoxList
    return detectionBoxList
  
def changeJsonList(jsonList):
    newjsonList = []
    if len(jsonList) > 0:
        for detection in jsonList:
            className = detection['class']
            det = {}
            det['bounding_box'] = detection['bounding_box']
            det['score'] = detection['score']
            if className in ['Crack','Broken','Reflection','Scratch']:
                det['class'] = 'Damage'
            else:
                det['class'] = 'Phone'
#                det['obstruction'] = detection['obstruction']
            newjsonList.append(det) 
    return newjsonList    
'''
def addObstruction(jsonList,image):
    newjsonList = []
    damageObjectsList = []
    for detection in jsonList:
        if detection['class'] in ['Crack','Broken','Reflection','Scratch']:
            polygonList = []
            for point in detection['polygon']:
                polygonList.append(point[0])
                polygonList.append(point[1])
            damageObjectsList.append(polygonList)
    for detection in jsonList:
        if detection['class'] == 'Phone':
            detection['obstruction'] = round(float(getObstructionPercentage(image, [detection], damageObjectsList, True)),2)
        newjsonList.append(detection) 
    return newjsonList
'''
def centralizedResponse(image,SEND_OLD_FORMAT=False):
    detectedBoxList = getCombinedResponse(image)
    detectedBoxList = normalizeBoxes(detectedBoxList,image)
    if SAVE_ANNOTATION:
        annotate(image,detectedBoxList,ANNOTATED_TEMP_IMG)
    jsonList = consolidate_data(detectedBoxList)    
    #jsonList = addLitUnlitFlag(jsonList)
    #jsonList = addObstruction(jsonList,image)
    if SEND_OLD_FORMAT:
        jsonList = changeJsonList(jsonList)
    return jsonList