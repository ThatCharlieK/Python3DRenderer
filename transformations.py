from math import sin, cos
import numpy as np
from geometry import Mesh
from typing import Optional, List, Tuple


class Transformation:
    def __init__(self, matrix: np.array):
        self.matrix = matrix
        return

    @staticmethod
    def _apply_matrix_transformation_to_mesh(mesh: Mesh, matrix: np.array):
        for point in mesh.points:
            np_point = np.array([point.x, point.y, point.z])
            result_point = matrix @ np_point
            point.x = result_point[0]
            point.y = result_point[1]
            point.z = result_point[2]

    def apply_transformation(self, mesh: Mesh):
        return


class Rotate(Transformation):
    def apply_transformation(self, mesh: Mesh):
        y = self.matrix.x
        b = self.matrix.y
        a = self.matrix.z
        # see https://en.wikipedia.org/wiki/Rotation_matrix for rotation matrix
        rotation = np.array([
            [cos(b) * cos(y), sin(a) * sin(b) * cos(y) - cos(a) * sin(y), cos(a) * sin(b) * cos(y) + sin(a) * sin(y)],
            [cos(b) * sin(y), sin(a) * sin(b) * sin(y) + cos(a) * cos(y), cos(a) * sin(b) * sin(y) - sin(a) * cos(y)],
            [-sin(b), sin(a) * cos(b), cos(a) * cos(b)]
        ])
        Transformation._apply_matrix_transformation_to_mesh(mesh, rotation)


class Scale(Transformation):
    def apply_transformation(self, mesh: Mesh):
        scale = np.array([
            [self.matrix.x, 0, 0],
            [0, self.matrix.y, 0],
            [0, 0, self.matrix.z]
        ])
        Transformation._apply_matrix_transformation_to_mesh(mesh, scale)


class AnimationStep:
    def __init__(self, actions: List[Transformation], step_time):
        self.actions = actions
        self.step_time = step_time
