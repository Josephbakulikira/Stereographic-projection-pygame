import setting
from vertex import Vertex
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
    # adding the North pole
    vertices.append(Vertex(0, 1, 0))

    for i in range(k-1):
        phi = math.pi * (i+1)/k
        for j in range(n):
            theta = 2 * math.pi * j/n
            x = math.sin(phi) * math.cos(theta)
            y = math.cos(phi)
            z = math.sin(phi) * math.sin(theta)
            vertices.append(Vertex(x, y, z))

    # adding the south pole
    vertices.append(Vertex(0, -1, 0))

    return vertices

def StereographicProjection(N, S, vertex):
    x = ( 2 * vertex.x)/(1-vertex.z)
    y = ( 2 * vertex.y)/(1-vertex.z)

    return (x * 20, y * 20)
