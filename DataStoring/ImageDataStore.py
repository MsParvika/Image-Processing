from pymongo import ASCENDING


def storeImage(dirPath, db):
    colList = db.list_collection_names()
    filename = dirPath+'\\desctxt\\desctxt\\devset_textTermsPerImage.txt'
    f = open(filename, encoding="utf8")

    if "imageData" not in colList:
        imageData = db.imageData

        for line in f:
            string = line.rstrip()
            word, space, rest = string.partition(' ')
            termsList = rest.split(" ")
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

            doc = {"imageId": word,
                   "terms": terms,
                   "TF": tf,
                   "DF": df,
                   "TF-IDF": tfIdf,
                   },
            imageData.insert_many(doc)
        imageData.create_index([("userId", ASCENDING)])

    else:
        print("Image Data already in db")

    f.close()
