import pygame
import sys
from typing import Optional, List, Tuple
import numpy as np
import generate_geometry
import math
from vectors import Vector2, Vector3
import constants
from geometry import Mesh
from camera import Camera
from renderer import Renderer
import time

if __name__ == "__main__":
    camera = Camera(Vector3(30, 20, 30), Vector3(0, 0, 0))
    renderer = Renderer(camera)
    cube = generate_geometry.generate_cube(Vector3(0, 0, 0), 10)

    running = True
    while running:
        cube.rotate_mesh(Vector3(0, 0.005, 0))
        cube.scale_mesh(Vector3(1.001, 1.001, 1.001))
        meshes = [cube]
        renderer.render_meshes(meshes)
        time.sleep(0.005)

    pygame.quit()
    sys.exit()
