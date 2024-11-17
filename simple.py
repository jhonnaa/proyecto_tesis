import os
import json
import numpy as np
import skimage.draw
from mrcnn.visualize import display_instances
from mrcnn import utils
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
from matplotlib import pyplot as plt

# define the prediction configuration
class PredictionConfig(Config):
	# define the name of the configuration
	NAME = "knee_cfg"
	# number of classes (background + Blue Marbles + Non Blue marbles)
	NUM_CLASSES = 1 + 2
	# Set batch size to 1 since we'll be running inference on
            # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1

cfg = PredictionConfig()
model = MaskRCNN(mode='inference', model_dir='logs', config=cfg)
# load model weights
model.load_weights('mask_rcnn_knee_cfg_0001.h5', by_name=True)
marbles_img = skimage.io.imread("test8.jpg")

detected = model.detect([marbles_img])
results = detected[0]
class_names = ['BG', 'normal', 'severo']
display_instances(marbles_img, results['rois'], results['masks'], 
                  results['class_ids'], class_names, results['scores'])
