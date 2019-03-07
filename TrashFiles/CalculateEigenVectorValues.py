import numpy as np
def calculateEigen(covMatrix):
    eig_vals, eig_vecs = np.linalg.eig(covMatrix)