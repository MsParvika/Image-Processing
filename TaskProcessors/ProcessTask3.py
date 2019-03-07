import DataStoring.LocationDataStore
import DataStoring.LocationMapping
import SimilarityFinder.SimilarityMatrixCreator
import TaskHelpers.GetTop3Contributors
import TaskHelpers.RetriveKOutput


def processTask3(dirPath, db):
    location_map = DataStoring.LocationMapping.mapLocationIdWithName(dirPath)

    locationData = db.locationData

    location_input = input("Enter LocationId, Model , value of 'k' separated by space")
    input_list = location_input.split(' ')

    location_id = location_map.get(input_list[0])

    locationSimilarityMatrix = SimilarityFinder.SimilarityMatrixCreator.createSimilarityMatrix(locationData,
                                                                                               input_list[1],
                                                                                               location_id,
                                                                                               "locationId")
    locationTopKValues = TaskHelpers.RetriveKOutput.getTopKValues(locationSimilarityMatrix,
                                                                  input_list[2])
    for key, value in locationTopKValues.items():
        locationId = [mapKey for mapKey, mapValue in location_map.items() if mapValue == key][0]
        print("LocationId - {0}, location - {1}, similarity value - {2}".format(locationId, key, value))

    TaskHelpers.GetTop3Contributors.findTopContributors(locationTopKValues, locationData, location_id,
                                                        input_list[1], 'locationId')
