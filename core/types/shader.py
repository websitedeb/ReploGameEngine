class Shader:
    """Interface to create Shaders"""
    vertexShader : str
    fragmentShader: str

def createShader(v : str, f : str) -> Shader:
    """Creates ShaderScripts"""
    class NewShader(Shader):
        vertexShader = v
        fragmentShader = f

    return NewShader