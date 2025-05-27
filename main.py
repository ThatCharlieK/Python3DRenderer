import pygame
import sys
from vectors import Vector2, Vector3
from camera import Camera
from renderer import Renderer
import time
from transformations import Transformation, Rotate, Scale, AnimationStep
import geometry
from game_object import GameObject

if __name__ == "__main__":
    camera = Camera(Vector3(30, 20, 30), Vector3(0, 0, 0))
    renderer = Renderer(camera)
    # generate a cube and its animations
    cube = geometry.generate_cube(Vector3(0, 0, 0), 10)
    step1 = AnimationStep([Scale(Vector3(1.005, 1.005, 1.005)), Rotate(Vector3(0.005, 0.005, 0.005))], 1.5)
    step2 = AnimationStep([Scale(Vector3(0.995, 0.995, 0.995)), Rotate(Vector3(-0.005, -0.005, -0.005))], 1.5)
    animation = [step1, step2]
    cube_game_object = GameObject(cube, animation)
    # define all gameObjects
    gameObjects = [cube_game_object]

    frame_time = 0.005
    running = True
    while running:
        for gameObject in gameObjects:
            gameObject.update_animation(frame_time)
        renderer.render_gameobjects(gameObjects)
        time.sleep(frame_time)

    pygame.quit()
    sys.exit()
