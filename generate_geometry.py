import main


def generate_cube(center: main.Vector3, width: float):
    half = width / 2

    # Vertices (numbered 0-7)
    vertices = [
        main.Vector3(center.x - half, center.y - half, center.z - half),  # 0
        main.Vector3(center.x - half, center.y + half, center.z - half),  # 1
        main.Vector3(center.x - half, center.y - half, center.z + half),  # 2
        main.Vector3(center.x - half, center.y + half, center.z + half),  # 3
        main.Vector3(center.x + half, center.y - half, center.z - half),  # 4
        main.Vector3(center.x + half, center.y + half, center.z - half),  # 5
        main.Vector3(center.x + half, center.y - half, center.z + half),  # 6
        main.Vector3(center.x + half, center.y + half, center.z + half),  # 7
    ]

    # Edges defined by vertex index pairs
    edges = [
        (0, 1), (1, 3), (3, 2), (2, 0),  # left face
        (4, 5), (5, 7), (7, 6), (6, 4),  # right face
        (0, 4), (1, 5), (2, 6), (3, 7)   # connecting edges between faces
    ]

    return vertices, edges
