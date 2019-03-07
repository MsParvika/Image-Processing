import DataStoring.LocationMapping
import SimilarityFinder.CalculateEuclideanSimilarity
import TaskHelpers.FindTopKLocationsCluster
import TaskHelpers.GetTop3ImagePairs


def processTask4(dirPath, db):
    locationImageData = db.locationImageClusters
    location_map = DataStoring.LocationMapping.mapLocationIdWithName(dirPath)
    user_input = input("Enter LocationId, Visual Model , value of 'k' separated by space")
    input_list = user_input.split(' ')
    inputTypeRecord = locationImageData.find_one({'locationId': input_list[0]})
    inputLocationCentroidsValue = inputTypeRecord[input_list[1]][0]
    dataInDb = list(locationImageData.find())
    locationViseSimilarity = {}
    for loc in dataInDb:
        if loc.get('locationId') == input_list[0]:
            continue
        locationCentroidsValue = loc.get(input_list[1])[0]
        locationViseSimilarity[
            loc.get('locationId')] = SimilarityFinder.CalculateEuclideanSimilarity.calculateSimilarity(
            inputLocationCentroidsValue, locationCentroidsValue)

    topKLocations = TaskHelpers.FindTopKLocationsCluster.findTopKLocations(input_list[2], locationViseSimilarity)
    for key, value in topKLocations.items():
        print("Location - {0} - {1}, similarity value - {2}".format(key, location_map.get(key), value[0]))
    TaskHelpers.GetTop3ImagePairs.findTop3ImagePairs(dataInDb, topKLocations, input_list[1], input_list[0])
