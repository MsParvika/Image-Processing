import math


def calculateSimilarity(inputFeatures, recordFeatures):
    size = len(inputFeatures)
    minVal = []
    indexList = {}
    leastEuclidianDistance = []
    for i in range(0, size):
        minDistance = 1000000000000000000
        for j in range(0, size):
            distance = math.sqrt(
                sum([(float(a) - float(b)) ** 2 for a, b in zip(inputFeatures[i], recordFeatures[j])]))
            if minDistance > distance:
                minDistance = distance
                indexList[i] = j
        minVal.append(minDistance)
    indexOfInputList = minVal.index(min(minVal))
    indexOfSecondList = indexList.get(indexOfInputList)
    leastEuclidianDistance.append(min(minVal))
    leastEuclidianDistance.append(inputFeatures[indexOfInputList])
    leastEuclidianDistance.append(recordFeatures[indexOfSecondList])
    return leastEuclidianDistance
