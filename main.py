import pygame
import sys
from typing import Optional, List, Tuple
import numpy as np
import generate_geometry


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y # y is up
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self


class Camera:
    def __init__(self, position: Vector3):
        self.position = position

    def get_distance_from_center(self):
        return self.position.z  # simple solution for when it lays along (0, 0, d)


class Renderer:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Renderer")
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.camera = Camera(Vector3(0, 0, 500))

    def draw_point(self, point: Vector3) -> None:
        # Create a 3x4 matrix
        d = self.camera.get_distance_from_center()
        transformation = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, -1/d, 1]
        ])
        # add a homogenous coordinate, making a transform in 4d act like a shift in 3d
        homogenous_position = np.array([
            [point.x],
            [point.y],
            [point.z],
            [1]
        ])
        projected_position = transformation @ homogenous_position
        projected_position *= (1/(1-(point.z/d)))
        projected_x = float(projected_position[0][0])
        projected_y = float(projected_position[1][0])
        pygame.draw.circle(self.screen, self.RED, (projected_x, projected_y), 5)
        return

    def render_points(self, points: list[Vector3]) -> None:
        self.screen.fill(self.WHITE)
        for point in points:
            self.draw_point(point)
        pygame.event.get()
        pygame.display.flip()


if __name__ == "__main__":
    renderer = Renderer()
    test_points = generate_geometry.generate_cube(Vector3(200, 200, 200), 100)
    running = True
    while running:
        renderer.render_points(test_points)

    pygame.quit()
    sys.exit()
