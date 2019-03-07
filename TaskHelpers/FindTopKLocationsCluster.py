def findTopKLocations(k, similarityValues):
    sorted_by_value = sorted(similarityValues.items(), key=lambda kv: kv[1])
    counter = 0
    topLocations = {}
    for key, value in sorted_by_value:
        if counter < int(k):
            topLocations[key] = value
        else:
            break
        counter = counter + 1

    return topLocations
