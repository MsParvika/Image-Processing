import csv

from pymongo import ASCENDING

import DataStoring.LocationMapping


def storeImageLocation(db):
    location_map = DataStoring.LocationMapping.mapLocationIdWithName()
    colList = db.list_collection_names()
    models = ['CM', 'CM3x3', 'CN', 'CN3x3', 'CSD', 'GLRLM', 'GLRLM3x3', 'HOG', 'LBP', 'LBP3x3']
    if "locationImage" not in colList:
        locationImage = db.locationImage
        for k, v in location_map.items():
            modelsArray = []
            for model in models:
                file_name = "Repository\\img\\{} {}.csv".format(v, model)
                file_reader = open(file_name, "rt", encoding='utf8')
                read = csv.reader(file_reader)
                images = {}
                for row in read:
                    imageId = row.pop(0)
                    featureValues = list(row)
                    images[imageId] = featureValues
                modelsArray.append(images)
                file_reader.close()
            doc = {"locationId": k,
                   "locationName": v,
                   "CM": modelsArray[0],
                   "CM3x3": modelsArray[1],
                   "CN": modelsArray[2],
                   "CN3x3": modelsArray[3],
                   "CSD": modelsArray[4],
                   "GLRLM": modelsArray[5],
                   "GLRLM3x3": modelsArray[6],
                   "HOG": modelsArray[7],
                   "LBP": modelsArray[8],
                   "LBP3x3": modelsArray[9]
                   }
            locationImage.insert_one(doc)
        locationImage.create_index([("locationId", ASCENDING)])

    else:
        print("Location Image Data already in db")
