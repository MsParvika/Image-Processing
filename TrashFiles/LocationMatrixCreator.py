import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def createLocationMatrix(collection, model, totalFeatures):
    data = collection.find()
    locationsFeatureMap = {}  # contains Locations with their "Term" and "Model" values as a dictionary
    for record in data:
        global_feature = {}  # dictionary for terms and their "Model" values for a SINGLE location
        for feature in totalFeatures:
            global_feature[feature] = []
        for feature in totalFeatures:
            if (feature in record["terms"]):
                index = record["terms"].index(feature)
                global_feature[feature] = (record[model][index])
            else:
                global_feature[feature] = 0

        location = record['locationId']  # gives locationID of the location from the record in mongo
        locationsFeatureMap[
            location] = global_feature  # creating a location-(feature-model value) map for the records in Mongo

    # created table for location and its tfs for every term
    df = pd.DataFrame(locationsFeatureMap)
    #df = pd.DataFrame().from_dict(data=locationsFeatureMap, orient="index")
    a = cosine_similarity(df.T)
    # creating a data frame for Locations and its similarity matrix
    cos_df = pd.DataFrame(columns=list(locationsFeatureMap.keys()), index=list(locationsFeatureMap.keys()), data=a)

    return cos_df
