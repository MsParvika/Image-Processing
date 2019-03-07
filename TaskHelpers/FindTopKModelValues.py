def getModelValuesForTopLocations(topK, data):
    for key, value in data.items():
        print("Contribution of Model {} ".format(key))
        for locId in topK:
            print("Location {} is {}".format(locId, value.get(locId)))
