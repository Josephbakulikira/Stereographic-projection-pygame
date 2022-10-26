from ui import *


panel = Panel()

StereographicButton = Button("Stereographic Projection")
ShowStereoButton = ToggleButton()
ShowStereoButton.state = True
ShowStereoButton.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+100)
showStereoText = TextUI(
    "Show projection", (StereographicButton.position[0], StereographicButton.position[1]+100), (255, 255, 255))

ShowSphereButton = ToggleButton()
ShowSphereButton.state = True
ShowSphereButton.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+150)
showSphereText = TextUI(
    "Show sphere", (StereographicButton.position[0], StereographicButton.position[1]+150), (255, 255, 255))


showLines = ToggleButton()
showLines.state = False
showLines.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+200)
showLinesText = TextUI(
    "Show Lines", (StereographicButton.position[0], StereographicButton.position[1]+200), (255, 255, 255))

showVertices = ToggleButton()
showVertices.state = True
showVertices.position = (
    StereographicButton.position[0] + 170, StereographicButton.position[1]+250)
showVerticesText = TextUI(
    "Show vertices", (StereographicButton.position[0], StereographicButton.position[1]+250), (255, 255, 255))