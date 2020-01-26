import torch
import cv2
import numpy as np
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import GenericMask

import sys
sys.path.insert(0, '..')
from BoxesFunctions import *

def load_net(configPath,weightsPath,nms):
    cfg = get_cfg()
    cfg.merge_from_file(configPath)
    cfg.MODEL.WEIGHTS = weightsPath
    cfg.MODEL.ROI_HEADS.NMS_THRESH_TEST = nms
    cfg.freeze()
    predictor = DefaultPredictor(cfg)
    return predictor

def unwrap(predictions,imageShape):
    boxes = predictions.pred_boxes.tensor.numpy() if predictions.has("pred_boxes") else None
    scores = predictions.scores.numpy() if predictions.has("scores") else None
    classes = predictions.pred_classes.numpy() if predictions.has("pred_classes") else None
    if predictions.has("pred_masks"):
        masks = np.asarray(predictions.pred_masks)
        masks = [GenericMask(x, imageShape[0], imageShape[1]).mask for x in masks]
    else:
        masks = None
    return boxes,masks,scores,classes

def filterBoxes(boxes,masks,scores,classes,CLASS_LABELS,thresh=0.9):
    if (boxes is None) or (len(boxes) == 0):
        sorted_inds = []
    else:
        areas = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
        sorted_inds = np.argsort(-areas)
    boxList = []
    for i in sorted_inds:
        bbox = boxes[i]
        score = scores[i]
        if score < thresh:
            continue
        contour = None
        mask = masks[i]
        if masks is not None and len(masks) > i:
            mask = masks[i]
            contour = cv2.findContours(mask.astype("uint8"), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)[-2]
            if len(contour) == 0:
                continue
            contour = reducedCounter(contour)
        ObjectBox = BOX()
        ObjectBox.label = str(CLASS_LABELS[int(classes[i])])
        ObjectBox.score = round(float(score),2)
        ObjectBox.left = int(bbox[0])
        ObjectBox.top = int(bbox[1])
        ObjectBox.width = int(bbox[2] - bbox[0])
        ObjectBox.height = int(bbox[3] - bbox[1])
        contour = None
        if contour is not None:
            ObjectBox.mask = contour
            ObjectBox.area = float(cv2.contourArea(contour))
        else:
            ObjectBox.mask = None
            ObjectBox.area = float(ObjectBox.height*ObjectBox.width)            
        boxList.append(ObjectBox)
    return boxList

def detect(model,CLASS_LABELS,thresh,image):
    boxes,masks,scores,classes = unwrap(model(image)["instances"].to("cpu"),image.shape)
    return filterBoxes(boxes,masks,scores,classes,CLASS_LABELS,thresh)