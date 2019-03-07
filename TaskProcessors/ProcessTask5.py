import SimilarityFinder.FindLocationSimilairty
import TaskHelpers.ReturnTopKLocations
import TaskHelpers.FindTopKModelValues
import DataStoring.LocationMapping


def processTask5(dirPath, db):
    locationImageData = db.locationImageClusters
    location_map = DataStoring.LocationMapping.mapLocationIdWithName(dirPath)
    visualDescriptorsModels = ['CM', 'CM3x3', 'CN', 'CN3x3', 'CSD', 'GLRLM', 'GLRLM3x3', 'HOG', 'LBP', 'LBP3x3']
    user_input = input("Enter LocationId, value of 'k' separated by space")
    input_list = user_input.split(' ')
    inputTypeRecord = locationImageData.find_one({'locationId': input_list[0]})
    result={}
    for model in visualDescriptorsModels:
        inputLocationCentroidsValue=inputTypeRecord[model][0]
        similarityResult = {}
        for key, value in location_map.items():
            if key == input_list[0]:
                continue
            record = locationImageData.find_one({'locationId': key})
            recordLocationCentroidsValue = record[model][0]
            locationViseSimilarity= SimilarityFinder.FindLocationSimilairty.calculateLocationSimilarity(inputLocationCentroidsValue, recordLocationCentroidsValue)
            similarityResult[key] = locationViseSimilarity
        result[model] = similarityResult

    topkLoc= TaskHelpers.ReturnTopKLocations.getTopKLocations(input_list[1], result, input_list[0])
    print("Top {} locations are ".format(input_list[1]))

    for locId in topkLoc:
        sum = 0
        for key, value in result.items():
            sum += float(value.get(locId)[0])
        print("{} - {} Score : {}" .format(locId, location_map.get(locId), float(sum/10)))

    TaskHelpers.FindTopKModelValues.getModelValuesForTopLocations(topkLoc, result)
