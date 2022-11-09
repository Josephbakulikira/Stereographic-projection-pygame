from ui import *
from setting import Setting
s = Setting()

panel = Panel()
panel.h = 600

StereographicButton = TextUI("Press ' A ' to toggle animation of projection  ", (s.width-300, 140), (255, 255, 255))


ShowStereoButton = ToggleButton()
ShowStereoButton.state = True
ShowStereoButton.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+100)
showStereoText = TextUI(
    "Show projection", (StereographicButton.position[0]+20, StereographicButton.position[1]+100+10), (255, 255, 255))


ShowSphereButton = ToggleButton()
ShowSphereButton.state = True
ShowSphereButton.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+150)
showSphereText = TextUI(
    "Show sphere", (StereographicButton.position[0]+20, StereographicButton.position[1]+150+10), (255, 255, 255))


showLines = ToggleButton()
showLinesSphere = ToggleButton()

showLines.state = True
showLinesSphere.state = False

showLines.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+200)
showLinesSphere.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+250)

showLinesText = TextUI(
    "Show Lines Projection", (StereographicButton.position[0]+20, StereographicButton.position[1]+200+10), (255, 255, 255))
showLinesSphereText = TextUI(
    "Show Lines sphere", (StereographicButton.position[0]+20, StereographicButton.position[1]+250+10), (255, 255, 255))

showVertices = ToggleButton()
showVerticesSphere = ToggleButton()

showVertices.state = False
showVerticesSphere.state = True

showVertices.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+300)
showVerticesSphere.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+350)

showVerticesText = TextUI(
    "Show vertices Projection", (StereographicButton.position[0]+20, StereographicButton.position[1]+300+10), (255, 255, 255))
ShowVerticesSphereText = TextUI(
    "Show vertices Sphere", (StereographicButton.position[0]+20, StereographicButton.position[1]+350+10), (255, 255, 255))

StereographicButton.position = (StereographicButton.position[0]+95, StereographicButton.position[1])
StereographicButton.fontSize = 14
StereographicButtonInverse = TextUI("Press ' S ' to toggle animation of Inverse projection  ", (StereographicButton.position[0], 200), (255, 255, 255))
StereographicButtonInverse.fontSize = 14
