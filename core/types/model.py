from .color import Color
from .coords import Coords, createCoords
from .shader import Shader

class Model:
    """Interface for creating a Model"""
    modelFile : str
    textureFile : str
    color : Color | None
    scale : float
    position : Coords
    rotation : Coords
    shader : Shader | None

def createModel(_modelFile : str, _textureFile : str, _scale : float = 1.0, _position : Coords = createCoords(0, 0, 0), _rotation : Coords = createCoords(0, 0, 0), _color : Color | None = None, _shader : Shader | None = None) -> Model:
    """Creates Model"""
    class NewModel(Model):
        modelFile = _modelFile
        textureFile = _textureFile
        color = _color
        scale = _scale
        position = _position
        rotation = _rotation
        shader = _shader

    return NewModel