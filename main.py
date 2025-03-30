from core.logic.screen import Engine
from core.types import *

app = Engine()

app.setColor(0, 0, 0, 0)

teapot : Model = createModel("obj models/teapot.obj", "image.png", 2, createCoords(0, -10, 0), createCoords(0, 0, 0), createColor(225, 0, 0, 0), createShader("shaders/vert.vert", "shaders/frag.frag"))
app.camera.setPos(0, -20, 0)

app.load_model(teapot)

app.run()