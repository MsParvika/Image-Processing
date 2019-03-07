from decimal import Decimal


def findTopContributors(inputDictionary, collection, id, model, dataId):
    inputInformation = collection.find_one({dataId: id})
    allContributorsData = collection.find({dataId: {"$in": list(inputDictionary.keys())}})

    inputTerms = inputInformation['terms']

    for record in allContributorsData:
        termsList = record['terms']
        print("Top 3 similar words for {0} :  {1}".format(dataId, record[dataId]))
        cosMultiply = {}
        commonTermList = set(inputTerms).intersection(termsList)
        for term in commonTermList:
            index1 = record["terms"].index(term)
            indexInput = inputInformation["terms"].index(term)
            cosMultiply[term] = Decimal(record[model][index1]) * Decimal(inputInformation[model][indexInput])
        sorted_by_value = sorted(cosMultiply.items(), key=lambda kv: kv[1], reverse=True)
        current = 0
        for key, value in sorted_by_value:
            if (current < 3):
                print(key)
            else:
                break
            current += 1
