def getTopKValues(similarityMatrix, k):
    sortedMatrix = sorted(similarityMatrix.items(), key=lambda x: x[1], reverse=True)
    similarityValues = {}
    counter = 0
    for key, value in sortedMatrix:
        if counter < int(k):
            similarityValues[key] = value
        else:
            break
        counter = counter + 1
    return similarityValues
