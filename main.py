import numpy as np
import cv2
from glob import glob
import tensorflow as tf
import os


batch_size = 8
learning_rate  = 0.0001
epochs = 100

path = os.path.join("datasets", "train")

