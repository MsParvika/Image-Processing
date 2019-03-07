from pymongo import ASCENDING


def storeLocation(dirPath, db):
    colList = db.list_collection_names()
    filename = dirPath+'\\desctxt\\desctxt\\devset_textTermsPerPOI.wFolderNames.txt'
    f = open(filename, encoding="utf8")

    if "locationData" not in colList:
        locationData = db.locationData

        for line in f:
            string = line.rstrip()
            word, space, rest = string.partition(' ')
            word2, comma, rest2 = rest.partition('"')
            termsList = (comma + rest2).split(" ")
            terms = []
            tf = []
            df = []
            tfIdf = []
            current = 0
            while current < len(termsList):
                terms.append(termsList[current])
                tf.append(termsList[current + 1])
                df.append(termsList[current + 2])
                tfIdf.append(termsList[current + 3])
                current = current + 4

            doc = {"locationId": word,
                   "locationName": word2.rstrip(),
                   "terms": terms,
                   "TF": tf,
                   "DF": df,
                   "TF-IDF": tfIdf,
                   }
            locationData.insert_one(doc)
        locationData.create_index([("userId", ASCENDING)])

    else:
        print("Location Data already in db")

    f.close()
