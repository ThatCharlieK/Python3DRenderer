import main


def generate_cube(center: main.Vector3, width: float):
    half_width = width/2
    return [
        main.Vector3(center.x - half_width, center.y - half_width, center.z - half_width),
        main.Vector3(center.x - half_width, center.y + half_width, center.z - half_width),

        main.Vector3(center.x - half_width, center.y - half_width, center.z + half_width),
        main.Vector3(center.x - half_width, center.y + half_width, center.z + half_width),

        main.Vector3(center.x + half_width, center.y - half_width, center.z - half_width),
        main.Vector3(center.x + half_width, center.y + half_width, center.z - half_width),

        main.Vector3(center.x + half_width, center.y - half_width, center.z + half_width),
        main.Vector3(center.x + half_width, center.y + half_width, center.z + half_width)
    ]