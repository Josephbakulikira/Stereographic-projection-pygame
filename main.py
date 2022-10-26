import pygame
from setting import Setting, Translate
from utils import *
from setup import *
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
animation = 0
showUI = False
stereoButton = False

run = True
while run:
    display.fill(setting.black)
    clock.tick(setting.fps)
    frame_rate = int(clock.get_fps())
    pygame.display.set_caption(
        "Stereographic projection : fps: {0}".format(frame_rate))
    mouseclicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                showUI = not showUI
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseclicked = True

    if pygame.mouse.get_pressed(3)[0]:
        theta = Translate(pygame.mouse.get_pos()[
                          0], 0,  setting.width, 0, 2 * setting.PI)

    Render(polygons=sphereMesh, display=display,
           theta=theta, setting=setting, animation=animation, stereo=stereoButton, showSphere=ShowSphereButton.state, showStereo=ShowStereoButton.state, showlines=showLines.state, showvertices=showVertices.state)

    if showUI:
        panel.Render(display)
        StereographicButton.Render(display, mouseclicked, True)

        ShowStereoButton.Render(display, mouseclicked)
        ShowSphereButton.Render(display, mouseclicked)
        showLines.Render(display, mouseclicked)
        showVertices.Render(display, mouseclicked)

        showStereoText.Render(display)
        showSphereText.Render(display)
        showLinesText.Render(display)
        showVerticesText.Render(display)

    stereoButton = StereographicButton.state
    StereographicButton.state = False

    theta += 0.01
    animation += 0.02
    if animation > 1:
        animation = 1
    pygame.display.update()

pygame.quit()
