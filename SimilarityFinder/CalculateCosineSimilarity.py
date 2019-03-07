from decimal import Decimal


def calculateCosineSImilarity(inputTerms, inputModelValues, recordTerms, recordModelValues):
    cosProduct = 0
    inputVectorAbsoluteNormValue = 0
    recordVectorAbsoluteNormValue = 0
    for term in inputTerms:
        inputIndex = inputTerms.index(term)
        inputTermModelValue = Decimal(inputModelValues[inputIndex])
        inputVectorAbsoluteNormValue += inputTermModelValue * inputTermModelValue
        if term in recordTerms:
            recordIndex = recordTerms.index(term)
            recordTermModelValue = Decimal(recordModelValues[recordIndex])
            cosProduct += inputTermModelValue * recordTermModelValue

    for recordTerm in recordTerms:
        recordIndex = recordTerms.index(recordTerm)
        recordTermModelValue = Decimal(recordModelValues[recordIndex])
        recordVectorAbsoluteNormValue += recordTermModelValue * recordTermModelValue

    denominator = Decimal(inputVectorAbsoluteNormValue).sqrt() * Decimal(recordVectorAbsoluteNormValue).sqrt()
    if not denominator:
        return 0.0
    return Decimal(cosProduct) / denominator
