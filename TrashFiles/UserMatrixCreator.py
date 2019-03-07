import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def createMatrix(collection, model, totalFeatures):
    data = collection.find()
    usersFeatureMap = {}  # contains USERS with their "Term" and "Model" values as a dictionary
    for record in data:
        global_feature = {}  # dictionary for terms and their "Model" values for a SINGLE user
        for feature in totalFeatures:
            global_feature[feature] = []
        for feature in totalFeatures:
            if (feature in record["terms"]):
                index = record["terms"].index(feature)
                global_feature[feature] = (record[model][index])
            else:
                global_feature[feature] = 0

        user = record['userId']  # gives userID of the user from the record in mongo
        usersFeatureMap[user] = global_feature  # creating a user-(feature-model value) map for the records in Mongo

    # created table for user and its tfs for every term
    df = pd.DataFrame(usersFeatureMap)
    #df = pd.DataFrame().from_dict(data=usersFeatureMap, orient="index")
    a = cosine_similarity(df.T)
    # creating a data frame for Users and its similarity matrix
    cos_df = pd.DataFrame(columns=list(usersFeatureMap.keys()), index=list(usersFeatureMap.keys()), data=a)

    return cos_df
