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

if __name__ == "__main__":
    camera = Camera(Vector3(30, 80, 50), Vector3(0, 0, 0))
    renderer = Renderer(camera)
    cube = generate_geometry.generate_cube(Vector3(10, 10, 10), 20)
    cube2 = generate_geometry.generate_cube(Vector3(10, 50, 10), 30)
    meshes = [cube, cube2]
    running = True
    while running:
        renderer.render_meshes(meshes)

    pygame.quit()
    sys.exit()
