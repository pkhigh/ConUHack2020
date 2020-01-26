import sys
from dataParsingFunctions import *
from modelClass import *
from hardConstants import *


CAR_MODEL = model()
CAR_MODEL.configPath = configPath
CAR_MODEL.weightsPath = weightsPath
CAR_MODEL.classes = CLASSES
CAR_MODEL.thresh = thresh
CAR_MODEL.nms = nms

CAR_MODEL.load()

app = Flask(__name__)

def removeRedundantPhoneBoxes(detectedBoxList):
    detectedBoxList = sortBoxList(detectedBoxList)
    newBoxList = []
    for ObjectBox in detectedBoxList:
        add = True
        for otherBox in newBoxList:
            if bb_intersection_over_union(ObjectBox,otherBox) > nms:
                add = False
                break
        if add:
            newBoxList.append(ObjectBox)
    return newBoxList

@app.route("/car_type", methods= ['POST'])
def main():
    response = []
    try:
        image = get_image(request.files)
        detectedBoxList = CAR_MODEL.detect(image)
        detectedBoxList = suppressClassWiseConfidence(detectedBoxList)
        
        detectedBoxList = removeRedundantPhoneBoxes(detectedBoxList)
        detectedBoxList = normalizeBoxes(detectedBoxList,image)
        print(detectedBoxList)
        annotate(image,detectedBoxList,ANNOTATED_TEMP_IMG)
        response = consolidate_data(detectedBoxList)
    except Exception as e:
        print(e)
    return jsonify(response)

    
app.run(debug=False, host='0.0.0.0', port=SERVER_PORT)