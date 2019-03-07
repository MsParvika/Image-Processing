import numpy as np

def manhattanDistance(inputVector, recordVector):
    return max(np.sum(np.fabs(inputVector - recordVector)))