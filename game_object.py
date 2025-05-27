from geometry import Mesh
from transformations import AnimationStep
from typing import Optional, List, Tuple


class GameObject:
    def __init__(self, mesh: Mesh, animation: List[AnimationStep] = None):
        self.mesh = mesh
        self.animation = animation
        if animation is None:
            return
        self.current_time_in_animation_step = 0
        self.animation_step_index = 0  # the index that the animation is currently on
        self.current_animation_step = animation[self.animation_step_index]

    def __apply_animation_step(self, animation_step: AnimationStep):
        for transformation in animation_step.actions:
            transformation.apply_transformation(self.mesh)
        return

    def update_animation(self, frame_time: float):
        self.current_time_in_animation_step += frame_time
        print(f"time in animation step: {self.current_time_in_animation_step}")
        self.__apply_animation_step(self.current_animation_step)
        # if the current animation step is finished
        if self.current_time_in_animation_step > self.current_animation_step.step_time:
            # go to the next animation
            if self.animation_step_index >= len(self.animation)-1:
                # loop back around if at the end
                self.animation_step_index = 0
            else:
                self.animation_step_index += 1
            self.current_animation_step = self.animation[self.animation_step_index]
            self.current_time_in_animation_step = 0
        return
