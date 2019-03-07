import SimilarityFinder.CalculateCosineSimilarity


def createSimilarityMatrix(collection, model, inputId, inputTypeId ):
    inputTypeRecord = collection.find_one({inputTypeId: inputId})

    inputTermsList = inputTypeRecord['terms']
    inputModelValuesList = inputTypeRecord[model]

    data = collection.find()
    similarityValues = {}
    for record in data:
        if record[inputTypeId] == inputId:
            continue
        recordTermsList = record['terms']
        recordModelValueList = record[model]
        similarityValue = SimilarityFinder.CalculateCosineSimilarity.calculateCosineSImilarity(inputTermsList,
                                                                                               inputModelValuesList,
                                                                                               recordTermsList,
                                                                                               recordModelValueList)
        similarityValues[record[inputTypeId]] = similarityValue
    return similarityValues
