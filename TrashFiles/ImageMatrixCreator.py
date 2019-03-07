import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

import TaskHelpers.RetriveKOutput
import time

start_time = time.time()

def createImageMatrix(collection, model, totalFeatures, k, id):
    print("--- %s Start seconds ---" % (time.time() - start_time))
    inputGlobal_feature = {}  # dictionary for input image matrix with '0' as model value where term is not present
    input_image = collection.find_one({"imageId": id})
    for feature in totalFeatures:
        inputGlobal_feature[feature] = []
    for feature in totalFeatures:
        if (feature in input_image["terms"]):
            index = input_image["terms"].index(feature)
            inputGlobal_feature[feature] = input_image[model][index]
        else:
            inputGlobal_feature[feature] = 0

    input_image = [{id: inputGlobal_feature}]
    data = collection.find()
    imagesFeatureMap = {}
    similarityValues = {}
    counter = 0
    print("--- %s input image done seconds ---" % (time.time() - start_time))
    for record in data:
        print("--- %s found record ---" % (time.time() - start_time))
        if counter > 600:
            print("--- %s counter ---" % (time.time() - start_time))
            newSimilarityValues = get_similarity_values(imagesFeatureMap, input_image, id, k)
            print("--- %s got similarity 600 ---" % (time.time() - start_time))
            similarityValues = get_top_k_two_dict(similarityValues, newSimilarityValues, id, k)
            print("--- %s got top 2 dictionaries 600 ---" % (time.time() - start_time))
            imagesFeatureMap = {}
            counter = 0
        counter += 1
        global_feature = {}  # dictionary for terms and their "Model" values for a SINGLE image except input image
        for feature in totalFeatures:
            global_feature[feature] = []
        for feature in totalFeatures:
            if (feature in record["terms"]):
                index = record["terms"].index(feature)
                global_feature[feature] = (record[model][index])
            else:
                global_feature[feature] = 0
        if record["imageId"] == id:
            continue
        print("--- %s creating record map seconds ---" % (time.time() - start_time))
        imagesFeatureMap[record['imageId']] = global_feature  # creating a image-(feature-model value) map for the records in Mongo
        print("--- %s created MAP seconds ---" % (time.time() - start_time))

    print("--- %s All records seconds ---" % (time.time() - start_time))
    return similarityValues


def get_similarity_values(imagesFeatureMap, input_image, id, k):
    df = pd.DataFrame(imagesFeatureMap)
    input_image_df = pd.DataFrame(input_image[0])
    a = cosine_similarity(df.T, input_image_df.T)
    cos_df = pd.DataFrame(columns=[id], index=list(imagesFeatureMap.keys()), data=a)
    similarityValues = TaskHelpers.RetriveKOutput.getTopKValues(cos_df, id, k)
    return similarityValues


# get the top of the two dictionaries
def get_top_k_two_dict(last_dict, next_dict, id, k):
    index = list(last_dict.keys()) + list(next_dict.keys())
    values = list(last_dict.values()) + list(next_dict.values())
    merged = pd.DataFrame({id: values}, index=index, columns=[id])
    similarityValues = TaskHelpers.RetriveKOutput.getTopKValues(merged, id, int(k))
    return similarityValues
