import setting
from vertex import Vertex
from polygon import Polygon
import math
import numpy as np

def xRot(theta):
    return np.array([
    [1, 0, 0],
    [0, math.cos(theta), -math.sin(theta)],
    [0, math.sin(theta), math.cos(theta)]
    ])

def yRot(theta):
    return np.array([
    [math.cos(theta), 0, math.sin(theta)],
    [0, 1, 0],
    [-math.sin(theta), 0, math.cos(theta)]
    ])

def zRot(theta):
    return np.array([
    [math.cos(theta), -math.sin(theta), 0],
    [math.sin(theta), math.cos(theta), 0],
    [0, 0, 1]
    ])

def MatrixToVertex(mat):
    return Vertex(mat[0][0], mat[1][0], mat[2][0])

def GenerateUVSphere(n, k):
    vertices = []
    polygons = []
    # adding the North pole
    north_pole = Vertex(0, 1, 0)
    vertices.append(north_pole)

    for i in range(k-1):
        phi = math.pi * (i+1)/k
        for j in range(n):
            theta = 2 * math.pi * j/n
            x = math.sin(phi) * math.cos(theta)
            y = math.cos(phi)
            z = math.sin(phi) * math.sin(theta)
            vertices.append(Vertex(x, y, z))

    # adding the south pole
    south_pole = Vertex(0, -1, 0)
    vertices.append(south_pole)

    # Add north and south pole triangles
    for i in range(n):
        # North polygons
        index_0 = i + 1
        index_1 = ( i + 1) % n + 1
        North = Polygon()
        North.vertices.append(north_pole)
        North.vertices.append(vertices[index_0])
        North.vertices.append(vertices[index_1])
        polygons.append(North)

        # South polygons
        index_0 = i + n * (k - 2) + 1
        index_1 = (i + 1) % n + n * (k - 2) + 1
        South = Polygon()
        South.vertices.append(south_pole)
        South.vertices.append(vertices[index_0])
        South.vertices.append(vertices[index_1])
        polygons.append(South)

    for i in range(k-2):
        index_0 = i * n + 1
        index_1 = (i + 1) * n + 1
        for j in range(n):
            i0 = index_0 + j
            i1 = index_0 + (j + 1) % n
            i2 = index_1 + (j + 1) % n
            i3 = index_1 + j
            quad = Polygon()
            quad.vertices.append(vertices[i0])
            quad.vertices.append(vertices[i1])
            quad.vertices.append(vertices[i2])
            quad.vertices.append(vertices[i3])

            polygons.append(quad)


    return polygons

def StereographicProjection(N, S, vertex, scale=1):
    x = ( vertex.x)/(1-vertex.z)
    y = ( vertex.y)/(1-vertex.z)

    return (x * scale, y * scale)

def Lerp(a, b, t):
    return a + (b-a) * t
