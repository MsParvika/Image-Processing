import SimilarityFinder.CalculateEuclideanSimilarity


def processTask4(db):
    locationImageData = db.locationImage
    user_input = input("Enter LocationId, Visual Model , value of 'k' separated by space")
    input_list = user_input.split(' ')
    locationImageLocations = {}
    inputTypeRecord = locationImageData.find_one({"locationId": input_list[0]})
    locationImagesRecords = list(locationImageData.find())

    for key, value in inputTypeRecord[input_list[1]].items():
        imageId = key
        locationViseSimilarity = {}
        for document in locationImagesRecords:
            if document["locationId"] == input_list[0]:
                continue
                similarityValue = []
            for recKey, recVal in document[input_list[1]].items():
                similarityValue.append(
                    SimilarityFinder.CalculateEuclideanSimilarity.calculateSimilarity(value, recVal))
                meanValue = sum(similarityValue) / len(similarityValue)
            locationViseSimilarity[document["locationName"]] = meanValue
        locationImageLocations[imageId] = locationViseSimilarity
    print(locationImageLocations)
