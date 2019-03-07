import DataStoring.LocationDataStore
import DataStoring.LocationMapping
import TrashFiles.LocationMatrixCreator
import TaskHelpers.RetriveKOutput
import TaskHelpers.GetTop3Contributors


def processTask3(db):
    totalFeatures = DataStoring.LocationDataStore.totalFeatures
    location_map = DataStoring.LocationMapping.mapLocationIdWithName()

    locationData = db.locationData

    location_input = input("Enter LocationId, Model , value of 'k' separated by space")
    input_list = location_input.split(' ')

    location_id = location_map.get(input_list[0])

    locationSimilarityMatrix = TrashFiles.LocationMatrixCreator.createLocationMatrix(locationData, input_list[1],
                                                                                     totalFeatures)
    locationSimilarityValues = TaskHelpers.RetriveKOutput.getTopKValues(locationSimilarityMatrix, location_id,
                                                                        input_list[2])
    for key, value in locationSimilarityValues.items():
        print("locationId - {0}, similarity value - {1}".format(key, value))

    TaskHelpers.GetTop3Contributors.findTopContributors(locationSimilarityValues, locationData, location_id,
                                                        input_list[1], 'locationId')
