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

    def scale_mesh(self, scale: Vector3):
        scale = np.array([
            [scale.x, 0, 0],
            [0, scale.y, 0],
            [0, 0, scale.z]
        ])
        for point in self.points:
            self.__apply_matrix_to_point(point, scale)

    @staticmethod
    def __apply_matrix_to_point(point: Vector3, matrix: np.array):
        np_point = np.array([point.x, point.y, point.z])
        result_point = matrix @ np_point
        point.x = result_point[0]
        point.y = result_point[1]
        point.z = result_point[2]

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
            self.__apply_matrix_to_point(point, rotation)


