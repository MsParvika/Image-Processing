def getTopKLocations(k, locationSimilarity, inputLocationId):
    sortedValues = []
    locationContribution = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,
                            '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0,
                            '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0,
							'31': 0, '32': 0, '33': 0, '34': 0, '35': 0}
    for key, value in locationSimilarity.items():
        sortedValues.append(sorted(value.items(), key=lambda x: x[1], reverse=True))
    for list in sortedValues:
        counter = 0
        for item in list:
            location_id = item[0]
            location_index = counter
            locationContribution[location_id] += location_index
            counter += 1

    del locationContribution[inputLocationId]
    result = []
    counterIndex = 0
    for key, value in sorted(locationContribution.items(), key=lambda x: x[1]):
        if counterIndex < int(k):
            result.append(key)
        else:
            break
        counterIndex += 1

    return result
