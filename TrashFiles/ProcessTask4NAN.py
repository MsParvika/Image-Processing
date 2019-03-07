import csv

from sklearn.preprocessing import StandardScaler
import DataStoring.LocationMapping
import TrashFiles.CreateCovarianceMatrix
import TrashFiles.CalculateEigenVectorValues
import numpy as np

def processTask4():
    location_map = DataStoring.LocationMapping.mapLocationIdWithName()

    user_input = input("Enter LocationId, Visual Model , value of 'k' separated by space")
    input_list = user_input.split(' ')
    location_id = location_map.get(input_list[0])
    file_name = "Repository\\img\\{} {}.csv".format(location_id, input_list[1])
    with open(file_name, 'r') as f:
        data = list(csv.reader(f))
    inputMatrix= np.array(data)
    X= inputMatrix[:, :1]
    Y= inputMatrix[:, 1:].astype(np.float)
    covarianceMatrix= TrashFiles.CreateCovarianceMatrix.findCovariance(Y)
    print("---------")
    X_std = StandardScaler().fit_transform(Y)
    print(TrashFiles.CreateCovarianceMatrix.findCovariance(X_std))
    TrashFiles.CalculateEigenVectorValues.calculateEigen(covarianceMatrix)