import pygame
from setting import *
from utils import *
from render import Render

setting = Setting()

pygame.init()
display = pygame.display.set_mode(setting.get_resolution())
clock = pygame.time.Clock()

n = 20
k = 20
sphereMesh = GenerateUVSphere(n, k)

# apply rotation
for polygon in sphereMesh:
    for index, vertex in enumerate(polygon.vertices):
        vertex = np.matmul(zRot(setting.PI/2), vertex.ToMatrix())
        vertex = MatrixToVertex(vertex)
        polygon.vertices[index] = vertex

theta = 0
prev = None

run = True
while run:
    display.fill(setting.black)
    clock.tick(setting.fps)
    frame_rate = int(clock.get_fps())
    pygame.display.set_caption("Stereographic projection : fps: {0}".format(frame_rate))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False

    # for index, vtx in enumerate(sphereMesh):
    #     vertex = np.matmul(xRot(theta), vtx.ToMatrix())
    #     vertex = np.matmul(yRot(theta), vertex)

    #     vertex = MatrixToVertex(vertex)
    #     v = vertex.translatetoScreen(-1, 1, 0, 200)
    #     pygame.draw.circle(display, white, (v.x  + width//2 - 100, v.y + height //2 - 100), 2)

    #     if index > 0 and index < len(sphereMesh)-1:
    #         x, y = StereographicProjection(None, None, vertex)
    #         # pygame.draw.circle(display, (100, 100, 100), (x + width//2 , y + height//2), 1)
    
    # for index, tgl in enumerate(triangles):
        
    #     v1 = np.matmul(xRot(theta), tgl.v1.ToMatrix())
    #     v2 = np.matmul(xRot(theta), tgl.v2.ToMatrix())
    #     v3 = np.matmul(xRot(theta), tgl.v3.ToMatrix())

    #     v1 = MatrixToVertex(v1)
    #     v2 = MatrixToVertex(v2)
    #     v3 = MatrixToVertex(v3)

    #     vertex1 = v1.translatetoScreen(-1, 1, 0, 200)
    #     vertex2 = v2.translatetoScreen(-1, 1, 0, 200)
    #     vertex3 = v3.translatetoScreen(-1, 1, 0, 200)
        
    #     pygame.draw.circle(display, white, (vertex1.x  + width//2 - 100, vertex1.y + height //2 - 100), 2)
    #     pygame.draw.circle(display, white, (vertex2.x  + width//2 - 100, vertex2.y + height //2 - 100), 2)
    #     pygame.draw.circle(display, white, (vertex3.x  + width//2 - 100, vertex3.y + height //2 - 100), 2)

    #     pygame.draw.line(display, white, (vertex1.x  + width//2 - 100, vertex1.y + height //2 - 100), (vertex2.x  + width//2 - 100, vertex2.y + height //2 - 100), 2)
    #     pygame.draw.line(display, white, (vertex1.x  + width//2 - 100, vertex1.y + height //2 - 100), (vertex3.x  + width//2 - 100, vertex3.y + height //2 - 100), 2)
    #     pygame.draw.line(display, white, (vertex3.x  + width//2 - 100, vertex3.y + height //2 - 100), (vertex2.x  + width//2 - 100, vertex2.y + height //2 - 100), 2)

    Render( polygons=sphereMesh , display=display, theta=theta, setting=setting)

    theta += 0.01
    pygame.display.update()

pygame.quit()
