from core.logic.engine import Engine
from core.types import *

app = Engine()

app.setColor(0, 0, 0, 1)

teapot: Model = createModel("models/teapot.obj", "textures/image.png", 1, createCoords(0, 0, 0), createCoords(0, 0, 0), createColor(255, 0, 0, 1), createShader("shaders/vert.vert", "shaders/frag.frag", "color"))

app.load_model(teapot)

app.run()