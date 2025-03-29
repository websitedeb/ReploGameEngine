from direct.showbase.ShowBase import ShowBase
from ..types import Model
from panda3d.core import Shader, LColor

class Screen(ShowBase):
    def __init__(self) -> None:
        ShowBase.__init__(self)

    def setColor(self, r: int, g: int, b: int, a: int | float) -> None:
        """Set the background color (normalized to 0-1 range)."""
        self.setBackgroundColor(r / 255.0, g / 255.0, b / 255.0, a)

    def load_model(self, model : Model) -> None:
        if type(model) == Model:
            self.model = self.loader.loadModel(model.modelFile)
            if self.model.isEmpty():
                print(f"Failed to load model: {model}")

            self.model.reparentTo(self.render)
            self.model.setScale(model.scale)
            self.model.setPos(model.position.X, model.position.Y, model.position.Z)
            self.model.setHpr(model.rotation.X, model.rotation.Y, model.rotation.Z)
            if model.color:
                self.model.setColorScale(LColor(model.color.R, model.color.G, model.color.B, model.color.A))

            self.texture = self.loader.loadTexture(model.textureFile)
            if self.texture:
                self.model.setTexture(self.texture, 1)
            else:
                print(f"Failed to load texture: {self.texture}")

            if model.shader:
                self.shader = Shader.load(Shader.SL_GLSL, vertex=model.shader.vertexShader, fragment=model.shader.fragmentShader)
                self.model.setShader(self.shader)
                self.model.setShaderInput("modelColor", LColor(model.color.R, model.color.G, model.color.B, model.color.A))
