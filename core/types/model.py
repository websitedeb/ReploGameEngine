from .color import Color
from .coords import Coords, createCoords
from .shader import Shader

class Model:
    """Class for creating a 3D Model"""
    def __init__(
        self, 
        modelFile: str, 
        textureFile: str, 
        scale: float = 1.0, 
        position: Coords = createCoords(0, 0, 0), 
        rotation: Coords = createCoords(0, 0, 0), 
        color: Color | None = None, 
        shader: Shader | None = None
    ) -> None:
        self.modelFile = modelFile
        self.textureFile = textureFile
        self.scale = scale
        self.position = position
        self.rotation = rotation
        self.color = color
        self.shader = shader

def createModel(
    _modelFile: str,
    _textureFile: str,
    _scale: float = 1.0,
    _position: Coords = createCoords(0, 0, 0),
    _rotation: Coords = createCoords(0, 0, 0),
    _color: Color | None = None,
    _shader: Shader | None = None
) -> Model:
    """Creates and returns a Model instance."""
    return Model(
        modelFile=_modelFile,
        textureFile=_textureFile,
        scale=_scale,
        position=_position,
        rotation=_rotation,
        color=_color,
        shader=_shader
    )
