import time
import math
import pygame

from quaternion import Quaternion

from scene import Scene
from object3d import Object3d
from camera import Camera
from mesh import Mesh
from material import Material
from color import Color
from vector3 import Vector3

def Viewer(a):

    k = a
    k = pygame.key.get_pressed()

    if(k[pygame.K_UP]):
        angle = 15
        axis = Vector3(1, 0, 0)
    elif (k[pygame.K_DOWN]):
        angle = -15
        axis = Vector3(1, 0, 0)
    elif (k[pygame.K_LEFT]):
        angle = 15
        axis = Vector3(0, 1, 0)
    elif (k[pygame.K_RIGHT]):
        angle = -15
        axis = Vector3(0, 1, 0)
    elif (k[pygame.K_PAGEUP]):
        angle = 15
        axis = Vector3(0, 0, 1)
    elif (k[pygame.K_PAGEDOWN]):
        angle = -15
        axis = Vector3(0, 0, 1)
    else:
        angle = 0