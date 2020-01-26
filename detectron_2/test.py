import torch
import cv2
import numpy as np
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import GenericMask

configPath = '/home/roadzen/ParasWork/detectron2/tmpPhoneModel/config.yaml'
weightsPath = '/home/roadzen/ParasWork/detectron2/tmpPhoneModel/model_0169999.pth'

cfg = get_cfg()
cfg.merge_from_file(configPath)
cfg.MODEL.WEIGHTS = weightsPath
cfg.freeze()

predictor = DefaultPredictor(cfg)

im = cv2.imread('017250.jpg')
#im = cv2.imread('020125.jpg')

def unwrap(predictions,imageShape):
    boxes = predictions.pred_boxes.tensor.numpy() if predictions.has("pred_boxes") else None
    scores = predictions.scores.numpy() if predictions.has("scores") else None
    classes = predictions.pred_classes.numpy() if predictions.has("pred_classes") else None
    if predictions.has("pred_masks"):
        masks = np.asarray(predictions.pred_masks)
        masks = [GenericMask(x, imageShape[0], imageShape[1]).polygons[0] for x in masks]
        #masks = [GenericMask(x, imageShape[0], imageShape[1]).mask for x in masks]
    else:
        masks = None
    return boxes,masks,scores,classes
            
outputs = predictor(im)["instances"].to("cpu")
boxes,masks,scores,classes = unwrap(outputs,im.shape)

print(masks[0])