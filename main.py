from Controller import *
import viz

window = viz.MainWindow
window.ortho(-320,320,-240, 240,-1,1)
window.clearcolor(viz.BLACK)
viz.eyeheight(0)

c = Controller()

viz.mouse(viz.OFF)
viz.go()