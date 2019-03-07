import pandas as pd
from sklearn.cluster import KMeans

import DataStoring.LocationMapping


def locationClusterValue():

    location_map = DataStoring.LocationMapping.mapLocationIdWithName()
    models = ['CM', 'CM3x3', 'CN', 'CN3x3', 'CSD', 'GLRLM', 'GLRLM3x3', 'HOG', 'LBP', 'LBP3x3']

    clusterCentroidPerLoc = {}
    for k, v in location_map.items():
        locationImage = {}
        for model in models:
            file_name = "Repository\\img\\{} {}.csv".format(v, model)
            dataset = pd.read_csv(file_name, header=None)
            x = dataset.iloc[:, 1:].values
            kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
            kmeans.fit(x)
            locationImage[model] = kmeans.cluster_centers_
        clusterCentroidPerLoc[k] = locationImage

    return clusterCentroidPerLoc
