from core.logic.screen import Screen
from core.types import *

app = Screen()

teapot : Model = createModel("obj models/teapot.obj", "image.png", 1, createCoords(0, 10, 0), createCoords(0, 0, 0), None, createShader("shaders/vert.vert", "shaders/frag.frag"))

app.load_model(teapot)

app.run()