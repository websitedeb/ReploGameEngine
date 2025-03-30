from core.logic.engine import Engine
from core.types import *

app = Engine()
app.setColor(0, 0, 0, 1)

teapot1: Model = createModel(
    "models/teapot.obj", "textures/image.png", 
    1, createCoords(-5, 10, 0), createCoords(0, 90, 0), 
    createColor(255, 255, 255, 1), createShader("shaders/vert.vert", "shaders/frag.frag", "color")
)

teapot2: Model = createModel(
    "models/teapot.obj", None, 
    1, createCoords(5, 10, 0), createCoords(0, 90, 0), 
    createColor(255, 0, 0, 1), createShader("shaders/vert.vert", "shaders/frag.frag", "color")
)

teapot1_model = app.load_model(teapot1)

teapot2_model = app.load_model(teapot2)

def spin_teapot1(task):
    if teapot1_model:
        h, p, r = teapot1_model.getHpr()
        teapot1_model.setHpr(h + 1, p, r)
    return task.cont

app.taskMgr.add(spin_teapot1, "spinTeapot1")

app.run()
