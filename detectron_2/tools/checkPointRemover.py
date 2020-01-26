import logging
import os
from collections import OrderedDict
import torch

import detectron2.utils.comm as comm
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.engine import DefaultTrainer, default_argument_parser, default_setup, hooks, launch



WEIGHTS = "/home/roadzen/ParasWork/detectron2/extAngleDamModels/model_final.pth"
model = torch.load(WEIGHTS)
model.pop('scheduler', None)
model.pop('iteration', None)
model.pop('optimizer', None)
print(model.keys())
torch.save(model, "/home/roadzen/ParasWork/detectron2/extAngleDamModels/toUse.pth")