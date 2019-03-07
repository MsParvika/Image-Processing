import pymongo


def storeUser(dirPath, db):
    colList = db.list_collection_names()
    filename = dirPath+'\\desctxt\\desctxt\\devset_textTermsPerUser.txt'
    f = open(filename, encoding="utf8")

    if "userData" not in colList:
        userData = db.userData

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

            doc = {"userId": word,
                   "terms": terms,
                   "TF": tf,
                   "DF": df,
                   "TF-IDF": tfIdf,
                   },
            userData.insert_many(doc)
        userData.create_index([("userId", pymongo.ASCENDING)])

    else:
        print("User Data already in db")
    f.close()
