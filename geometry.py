import pygame
import sys
from typing import Optional, List, Tuple
import numpy as np
import generate_geometry
import math
from vectors import Vector2, Vector3
import constants


class Mesh:
    def __init__(self, points: List[Vector3], edges: List[Tuple[int, int]]):
        """
        :param points: what verticies of the matrix in 3d
        :param edges: each edge is a line between 2 points, represented by
        (index in points for the starting point, index in points for the ending point)
        """
        self.points = points
        self.edges = edges


