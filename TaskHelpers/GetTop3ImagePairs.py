def findTop3ImagePairs(collection, topKLocations, visualDescriptor, inputLocationId):
    for key, value in topKLocations.items():
        locationIdIndex = int(key) - 1
        record = collection[locationIdIndex].get(visualDescriptor)
        record2 = collection[int(inputLocationId) - 1].get(visualDescriptor)
        outputCentroidNumber = record[0].index(value[2])
        outputImangeIds = record[1].get(str(outputCentroidNumber))
        inputCentroidNumber = record2[0].index(value[1])
        inputImangeIds = record2[1].get(str(inputCentroidNumber))
        counter = 0
        a = []
        b = []
        sortedOutputImagesBySimilarity = sorted(outputImangeIds, key=lambda x: x[1], reverse=True)
        sortedInputImagesBySimilarity = sorted(inputImangeIds, key=lambda x: x[1], reverse=True)

        for image in sortedOutputImagesBySimilarity:
            if counter < 3:
                a.append(image[0])
                counter += 1
            else:
                break
        counter = 0
        for image in sortedInputImagesBySimilarity:
            if counter < 3:
                b.append(image[0])
                counter += 1
            else:
                break
        pairs = list(zip(a, b))
        print("Top 3 Contributing Images: input location {} and location {} :->  {}".format(inputLocationId,
                                                                                            key, pairs))
