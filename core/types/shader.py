class Shader:
    """Interface to create Shaders"""
    vertexShader : str
    fragmentShader: str
    fragColorVarName : str

def createShader(v : str, f : str, n : str) -> Shader:
    """Creates ShaderScripts"""
    class NewShader(Shader):
        vertexShader = v
        fragmentShader = f
        fragColorVarName = n

    return NewShader