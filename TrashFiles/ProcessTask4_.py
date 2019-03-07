import sys

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

import DataStoring.LocationMapping
import TrashFiles.FlushInput

def processTask4():
    location_map = DataStoring.LocationMapping.mapLocationIdWithName()

    user_input = input("Enter LocationId, Visual Model , value of 'k' separated by space")
    TrashFiles.FlushInput.flush_input()
    sys.stdout.flush()
    input_list = user_input.split(' ')

    location_id = location_map.get(input_list[0])
    file_name = "Repository\\img\\{} {}.csv".format(location_id, input_list[1])
    givenDataFrame = pd.read_csv(file_name, index_col=0, header=None)

    for location in location_map.values():
        file_name = "Repository\\img\\{} {}.csv".format(location, input_list[1])
        locationDataFrame = pd.read_csv(file_name, index_col=0, header=None)
        a = cosine_similarity(givenDataFrame, locationDataFrame)
        cos_df = pd.DataFrame(data=a, columns=locationDataFrame.index.values, index=givenDataFrame.index.values)
        similarityFileName = "Repository\\SimilarLocations\\{}-{}.csv".format(location_id, location)
        cos_df.to_csv(similarityFileName)
