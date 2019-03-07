import SimilarityFinder.CalculateCosineSimilarity
import time

start_time = time.time()

def createImageMatrix(collection, model, id):

    input_image = collection.find_one({"imageId": id})

    inputTermsList = input_image['terms']
    inputModelValuesList =input_image[model]

    data = collection.find()
    similarityValues = {}
    for record in data:
        if record["imageId"] == id:
            continue
        recordTermsList = record['terms']
        recordModelValueList = record[model]
        similarityValue = SimilarityFinder.CalculateCosineSimilarity.calculateCosineSImilarity(inputTermsList, inputModelValuesList, recordTermsList, recordModelValueList)
        similarityValues[record["imageId"]] = similarityValue
    return similarityValues
