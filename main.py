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
inverseButton = False
transitionAnimation = False
sphere_is_projected = False

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
            if event.key == pygame.K_s:
                transitionAnimation = True
                animation = 0
            if event.key == pygame.K_a:
                animation = 0
                stereoButton = not stereoButton
            if event.key == pygame.K_s:
                animation = 0
                inverseButton = not inverseButton
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseclicked = True

    if pygame.mouse.get_pressed(3)[0]:
        theta = Translate(pygame.mouse.get_pos()[
                          0], 0,  setting.width, 0, 2 * setting.PI)

    Render(polygons=sphereMesh, display=display,
           theta=theta, setting=setting, animation=animation,
           showSphere=ShowSphereButton.state, showStereo=ShowStereoButton.state,
           showlines=showLines.state, showvertices=showVertices.state, showSphereLines = showLinesSphere.state,
           showVerticesSphere=showVerticesSphere.state, 
           stereo_button=stereoButton, inverse_button=inverseButton)

    if showUI:
        panel.Render(display)
        StereographicButton.Render(display)
        StereographicButtonInverse.Render(display)

        # ShowStereoButton.Render(display, mouseclicked)
        ShowSphereButton.Render(display, mouseclicked)
        showLines.Render(display, mouseclicked)
        showVertices.Render(display, mouseclicked)
        showVerticesSphere.Render(display, mouseclicked)
        showLinesSphere.Render(display, mouseclicked)

        # showStereoText.Render(display)
        showSphereText.Render(display)
        showLinesText.Render(display)
        showVerticesText.Render(display)
        ShowVerticesSphereText.Render(display)
        showLinesSphereText.Render(display)


    theta += 0.01
    animation += 0.02
    if animation > 1:
        animation = 1
        transitionAnimation = False

    sphere_is_projected = True
    pygame.display.update()

pygame.quit()
