import math


def calculateLocationSimilarity(inputFeatures, recordFeatures):
    size = len(inputFeatures)
    minVal = []
    leastEuclidianDistance = []
    for i in range(0, size):
        minDistance = 1000000000000000000
        for j in range(0, size):
            distance = math.sqrt(
                sum([(float(a) - float(b)) ** 2 for a, b in zip(inputFeatures[i], recordFeatures[j])]))
            if minDistance > distance:
                minDistance = distance
        minVal.append(minDistance)
    leastEuclidianDistance.append(min(minVal))
    return leastEuclidianDistance
