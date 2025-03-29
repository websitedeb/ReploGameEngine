class Color:
    """Interface for creating Color"""
    R : int
    G : int
    B : int
    A : int | float

def createColor(r : int, g : int, b : int, a : int | float) -> Color:
    """Creates a Color"""
    class NewColor(Color):
        R = r
        G = g
        B = b
        A = a

    return NewColor