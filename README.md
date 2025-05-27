# Python3dRenderer
In this project, I created a 3D renderer in Python, focusing on applying linear algebra concepts.
I used the following linear algebra:
## View matrix
The view matrix: the matrix that transforms world coordinates 
into camera space. Essentially, in 3d rendering, 
the camera always stays in the same place and the geometry actually moves around this. 
The view matrix does that transformation to turn (x, y, z) coordinates 
relative to world space to (x, y, z) coordinates relative to the camera.
The view matrix is made up of the rotation:

```
    ⎡ right.x       right.y    right.z     0 ⎤
R = ⎢ up.x            up.y      up.z       0 ⎥
    ⎢ -forward.x  -forward.y  -forward.z   0 ⎥
    ⎣ 0                0          0        1 ⎦
```
Which is an orthonormal basis transformation, a change of basis from the world 
space to camera space.

The second part is a translation matrix. If the camera is moved in any (x, y, z)
direction, this matrix "undoes" that camera movement so that it seems like the 
camera is at (0, 0, 0). In reality, it does this by moving the entire world back,
not the camera.

Translation matrix:
```
    ⎡ 1     0     0     -camera.x ⎤
T = ⎢ 0     1     0     -camera.y ⎥
    ⎢ 0     0     1     -camera.z ⎥
    ⎣ 0     0     0        1      ⎦
```
The full view matrix, that transforms world coordinates into camera space, is then:
```
V = R @ T 
```

## Perspective matrix
Once vertices are transformed into view/camera space using the view matrix,
they are then transformed into the  "clip space" using a perspective matrix:

```
    ⎡ aspect_ratio*fov     0      0          0    ⎤
P = ⎢        0            fov     0          0    ⎥
    ⎢        0             0      q     -near * q ⎥
    ⎣        0             0      1          0    ⎦
```
The perspective matrix is multiplied by an (x, y, z, 1) coordinate in view space,
meaning each row of the perspective matrix has its own function:

| Row   | Function                                                          |
|-------|-------------------------------------------------------------------|
| row 1 | scales x axis based on horizontal FOV                             |
| row 2 | scales y axis based on vertical FOV                               |
| row 3 | Squashes view space Z values in the range (near, far) into (0, 1) |
| row 4 | Makes the homogenous coordinate W = Z for use in  a later step    |

## Project point
The project point function finally brings everything together and project sa point in 3d
onto normalized device coordinates. The function takes an input matrix pos3d = [x, y, z, 1] and does
the following steps and calculates the transformed (x, y, z, w) to be:
```
transformed = prospective matrix * view matrix * pos3d
```
then, it takes the w value of transformed. The W value (the homogenous coordinate) is
the Z value from the perspective matrix. It then calculates the x and y normalized device coordinates 
by taking the (x, y) from transformed and dividing it by the W value:
```
x_ndc  = x/w
y_ndc = y/w
```
This means that for a larger w, the x and y coordinates will be closer to zero.
x_ndc and y_ndc are in the range of (-1, 1), so that means that objects that appear further away
will appear closer to the screen. This is how perspective works - think of a road
winding into the horizon and converging at the center of the screen. Finally, the x_ndc and y_ndc are projected on a screen with a set width and height

Sources:
https://learnopengl.com/Getting-started/Coordinate-Systems
https://carmencincotti.com/2022-05-02/homogeneous-coordinates-clip-space-ndc/
