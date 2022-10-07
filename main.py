import pygame
from setting import *
from utils import *


pygame.init()
display = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
fps = 30

sphereMesh = GenerateUVSphere(10, 10)

theta = 0


run = True
while run:
    display.fill(black)
    clock.tick(fps)
    frame_rate = int(clock.get_fps())
    pygame.display.set_caption("Stereographic projection : fps: {0}".format(frame_rate))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False

    for index, vertex in enumerate(sphereMesh):
        vertex = np.matmul(xRot(theta), vertex.ToMatrix())
        vertex = MatrixToVertex(vertex)
        v = vertex.translatetoScreen(-1, 1, 0, 200)
        pygame.draw.circle(display, white, (v.x  + width//2 - 100, v.y + height //2 - 100), 2)
        if index > 0 and index < len(sphereMesh)-1:
            x, y = StereographicProjection(None, None, vertex)
            pygame.draw.circle(display, (100, 100, 100), (x + width//2 , y + height//2), 1)


    theta += 0.01
    pygame.display.update()

pygame.quit()
