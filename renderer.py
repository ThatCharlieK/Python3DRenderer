import pygame
from typing import Optional, List, Tuple
import numpy as np
import math
from vectors import Vector2, Vector3
import constants
from geometry import Mesh
from camera import Camera
from game_object import GameObject


class Renderer:
    def __init__(self, cam: Camera):
        pygame.init()
        self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("3D Renderer")
        self.camera = cam

    def get_view_matrix(self) -> np.ndarray:
        """
        :return: the matrix that transforms world coordinates into camera space
        Basically, the camera always stays at the same position and the geometry actually moves around it
        """
        forward = (self.camera.look_at - self.camera.position).normalized()
        right = forward.cross(Vector3(0, 1, 0)).normalized()
        up = right.cross(forward)

        rotation = np.array([
            [right.x, right.y, right.z, 0],
            [up.x, up.y, up.z, 0],
            [-forward.x, -forward.y, -forward.z, 0],
            [0, 0, 0, 1]
        ])

        translation = np.array([
            [1, 0, 0, -self.camera.position.x],
            [0, 1, 0, -self.camera.position.y],
            [0, 0, 1, -self.camera.position.z],
            [0, 0, 0, 1]
        ])
        # the view matrix, how things are shifted around in the scene to be relative to the camera,
        # is simply dependent on the camera's rotation and position
        view_matrix = rotation @ translation
        return view_matrix

    def get_perspective_matrix(self) -> np.ndarray:
        """
        Vertices that have been transformed in view space then need to be transformed by the perspective matrix
        into a space called the clip space
        :return:
        """
        fov_deg = 90
        near = 0.1
        far = 10000
        fov_rad = 1 / math.tan(math.radians(fov_deg) / 2)
        aspect_ratio = self.width / self.height
        q = far / (far - near)

        return np.array([
            # scale x axis based on horizontal FOV
            [aspect_ratio * fov_rad, 0, 0, 0],
            # scale y axis based on vertical FOV
            [0, fov_rad, 0, 0],

            [0, 0, q, -near * q],
            [0, 0, 1, 0]
        ])

    def project_point(self, point: Vector3) -> Optional[Tuple[int, int]]:
        model_pos = np.array([[point.x], [point.y], [point.z], [1]])
        view = self.get_view_matrix()
        proj = self.get_perspective_matrix()
        # 1. transform from model position into view space (into camera space)
        # 2. project it into the clipping plane
        transformed = proj @ view @ model_pos
        w = transformed[3][0]
        # prevent division by 0
        if w == 0:
            return None

        x_ndc = transformed[0][0] / w
        y_ndc = transformed[1][0] / w

        x_screen = int((x_ndc + 1) * 0.5 * self.width)
        y_screen = int((1 - y_ndc) * 0.5 * self.height)

        return x_screen, y_screen

    def draw_point(self, point: Vector3) -> None:
        projected = self.project_point(point)
        if projected:
            pygame.draw.circle(self.screen, constants.RED, projected, 2)

    def draw_line(self, p1: Vector3, p2: Vector3) -> None:
        proj1 = self.project_point(p1)
        proj2 = self.project_point(p2)
        if proj1 and proj2:
            pygame.draw.line(self.screen, constants.BLUE, proj1, proj2, 2)

    def __render_mesh(self, mesh: Mesh) -> None:
        for edge in mesh.edges:
            self.draw_line(mesh.points[edge[0]], mesh.points[edge[1]])
        for point in mesh.points:
            self.draw_point(point)

    def render_gameobjects(self, game_objects: List[GameObject]):

        self.screen.fill(constants.WHITE)
        for game_object in game_objects:
            self.__render_mesh(game_object.mesh)
        pygame.event.get()
        pygame.display.flip()
