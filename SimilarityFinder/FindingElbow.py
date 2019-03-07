import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import DataStoring.LocationMapping

models = ['CM', 'CM3x3', 'CN', 'CN3x3', 'CSD', 'GLRLM', 'GLRLM3x3', 'HOG', 'LBP', 'LBP3x3']
dirPath = input("Enter Directory path till devset")
location_map = DataStoring.LocationMapping.mapLocationIdWithName(dirPath)

for k, v in location_map.items():
    locationImage = {}
    for model in models:
        csvPath = "\\descvis\\descvis\\img\\{} {}.csv".format(v, model)
        file_name = dirPath + csvPath
        dataset = pd.read_csv(file_name)
        x = dataset.iloc[:, 1:].values
        wcss = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
            kmeans.fit(x)
            wcss.append(kmeans.inertia_)

        plt.plot(range(1, 11), wcss)
        plt.title('The elbow method')
        plt.xlabel('Number of clusters')
        plt.ylabel('WCSS')  # within cluster sum of squares
        plt.show()