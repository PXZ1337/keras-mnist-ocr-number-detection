
import os

FILE_PATH = os.path.abspath(__file__)
PROJECT_DIR = os.path.dirname(os.path.dirname(FILE_PATH))
IMAGE_DIR = os.path.join(PROJECT_DIR, "src","ressources", "imgs")
GUI_DIR = os.path.join(PROJECT_DIR, "src","ressources", "gui")

MNIST_IMAGE_WIDTH = 28
MNIST_IMAGE_HEIGHT = 28
