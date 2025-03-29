class Coords:
    """Interface for creating Coords for Position, Scale, Rotation"""
    X : int | float
    Y : int | float
    Z : int | float

def createCoords(x : int | float, y : int | float, z : int | float) -> Coords:
    """Creates a Coord"""
    class newCoords(Coords):
        X = x
        Y = y
        Z = z

    return newCoords