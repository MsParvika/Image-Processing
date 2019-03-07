import DataStoring.ImageDataStore
import DataStoring.LocationDataStore
import DataStoring.LocationImagesClusters
import DataStoring.UsersDataStore


def runMeForData(dirPath, db):
    DataStoring.ImageDataStore.storeImage(dirPath, db)
    DataStoring.LocationDataStore.storeLocation(dirPath, db)
    DataStoring.UsersDataStore.storeUser(dirPath, db)
    DataStoring.LocationImagesClusters.createClusters(dirPath, db)
