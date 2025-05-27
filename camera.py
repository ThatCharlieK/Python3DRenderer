from vectors import Vector2, Vector3


class Camera:
    def __init__(self, position: Vector3, look_at: Vector3):
        self.position = position
        self.look_at = look_at