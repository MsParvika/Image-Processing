import math


def calculateMinEuclidean(inputFeatures, centroidsVectors):
    size = len(centroidsVectors)
    indexMin = 0
    minDistance = 1000000000000000000
    similarityValueAndCentroidIndex = []
    for j in range(0, size):
        distance = math.sqrt(
            sum([(float(a) - float(b)) ** 2 for a, b in zip(inputFeatures, centroidsVectors[j])]))
        if minDistance > distance:
            minDistance = distance
            indexMin = j
    similarityValueAndCentroidIndex.append(minDistance)
    similarityValueAndCentroidIndex.append(indexMin)

    return similarityValueAndCentroidIndex
