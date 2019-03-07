import numpy as np

def findVariance(inputMatrix):
    mean_vec = np.mean(inputMatrix, axis=0)
    cov_mat = (inputMatrix - mean_vec).T.dot((inputMatrix - mean_vec)) / (inputMatrix.shape[0]-1)
    return cov_mat