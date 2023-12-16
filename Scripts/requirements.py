import os
import shutil
import cv2
import random
import zipfile

import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torchvision
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

! pip install torchinfo
from torchinfo import summary

from tqdm.auto import tqdm
