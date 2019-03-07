import pandas as pd
from pymongo import ASCENDING
from sklearn.cluster import KMeans

import DataStoring.LocationMapping
import SimilarityFinder.CalculateMinEuclideanDistance

def createClusters(dirPath, db):
    colList = db.list_collection_names()
    location_map = DataStoring.LocationMapping.mapLocationIdWithName(dirPath)
    models = ['CM', 'CM3x3', 'CN', 'CN3x3', 'CSD', 'GLRLM', 'GLRLM3x3', 'HOG', 'LBP', 'LBP3x3']
    if "locationImageClusters" not in colList:
        locationImageClusters = db.locationImageClusters
        clusterCentroidPerLoc = {}
        for k, v in location_map.items():
            eachModelCluster = []
            for model in models:
                clusterLoc= []
                csvPath = "\\descvis\\descvis\\img\\{} {}.csv".format(v, model)
                file_name = dirPath+ csvPath
                dataset = pd.read_csv(file_name, header=None)
                imageValues = dataset.iloc[:, 1:].values
                kmeans = KMeans(n_clusters=6, init='k-means++', max_iter=300, n_init=10, random_state=0)
                kmeans.fit(imageValues)
                clusters = kmeans.cluster_centers_
                centroidImages = {}
                for index in range(len(clusters)):
                    centroidImages[str(index)] = []
                for row in dataset.itertuples():
                    imageIdAndsimilarityValue=[]
                    imageId = row[1]
                    featureValues = list(row[2:len(row)-1])
                    similarityValueAndCentroidIndex = SimilarityFinder.CalculateMinEuclideanDistance.calculateMinEuclidean(featureValues, kmeans.cluster_centers_)
                    imageIdAndsimilarityValue.append(imageId)
                    imageIdAndsimilarityValue.append(similarityValueAndCentroidIndex[0])
                    centroidImages[str(similarityValueAndCentroidIndex[1])].append(imageIdAndsimilarityValue)
                clusterLoc.append(clusters.tolist())
                clusterLoc.append(centroidImages)
                eachModelCluster.append(clusterLoc)
            clusterCentroidPerLoc[k] = eachModelCluster

            doc = {"locationId": k,
               "locationName": v,
               "CM": eachModelCluster[0],
               "CM3x3":eachModelCluster[1],
               "CN": eachModelCluster[2],
               "CN3x3":eachModelCluster[3],
               "CSD": eachModelCluster[4],
               "GLRLM": eachModelCluster[5],
               "GLRLM3x3": eachModelCluster[6],
               "HOG": eachModelCluster[7],
               "LBP": eachModelCluster[8],
               "LBP3x3": eachModelCluster[9]
               }
            locationImageClusters.insert_one(doc)
        locationImageClusters.create_index([("locationId", ASCENDING)])