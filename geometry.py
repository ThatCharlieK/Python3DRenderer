from typing import Optional, List, Tuple
from vectors import Vector2, Vector3
from math import sin, cos
import numpy as np


class Mesh:
    def __init__(self, points: List[Vector3], edges: List[Tuple[int, int]]):
        """
        :param points: what vertices of the matrix in 3d
        :param edges: each edge is a line between 2 points, represented by
        (index in points for the starting point, index in points for the ending point)
        """
        self.points = points
        self.edges = edges


def generate_cube(center: Vector3, width: float) -> Mesh:
    half = width / 2

    vertices = [
        Vector3(center.x - half, center.y - half, center.z - half),  # 0
        Vector3(center.x - half, center.y + half, center.z - half),  # 1
        Vector3(center.x - half, center.y - half, center.z + half),  # 2
        Vector3(center.x - half, center.y + half, center.z + half),  # 3
        Vector3(center.x + half, center.y - half, center.z - half),  # 4
        Vector3(center.x + half, center.y + half, center.z - half),  # 5
        Vector3(center.x + half, center.y - half, center.z + half),  # 6
        Vector3(center.x + half, center.y + half, center.z + half),  # 7
    ]
    edges = [
        (0, 1), (1, 3), (3, 2), (2, 0),  # left face
        (4, 5), (5, 7), (7, 6), (6, 4),  # right face
        (0, 4), (1, 5), (2, 6), (3, 7)   # connecting edges between faces
    ]
    return Mesh(vertices, edges)



