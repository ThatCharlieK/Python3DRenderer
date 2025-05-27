import pygame
import sys
from typing import Optional, List, Tuple
import numpy as np
import generate_geometry
import math
from vectors import Vector2, Vector3
import constants
from math import cos, sin
import numpy as np


class Mesh:
    def __init__(self, points: List[Vector3], edges: List[Tuple[int, int]]):
        """
        :param points: what verticies of the matrix in 3d
        :param edges: each edge is a line between 2 points, represented by
        (index in points for the starting point, index in points for the ending point)
        """
        self.points = points
        self.edges = edges

    def rotate_mesh(self, rotation: Vector3):
        y = rotation.x
        b = rotation.y
        a = rotation.z
        # see https://en.wikipedia.org/wiki/Rotation_matrix for rotation matrix
        rotation = np.array([
            [cos(b) * cos(y), sin(a) * sin(b) * cos(y) - cos(a) * sin(y), cos(a) * sin(b) * cos(y) + sin(a)*sin(y)],
            [cos(b) * sin(y), sin(a) * sin(b) * sin(y) + cos(a) * cos(y), cos(a) * sin(b) * sin(y) - sin(a) * cos(y)],
            [-sin(b), sin(a) * cos(b), cos(a) * cos(b)]
        ])

        for point in self.points:
            np_point = np.array([point.x, point.y, point.z])
            rotated_point = rotation @ np_point
            point.x = rotated_point[0]
            point.y = rotated_point[1]
            point.z = rotated_point[2]


