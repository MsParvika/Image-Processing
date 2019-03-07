import SimilarityFinder.SimilarityMatrixCreator
import TaskHelpers.GetTop3Contributors
import TaskHelpers.RetriveKOutput


def processTask2(db):
    imageData = db.imageData
    image_input = input("Enter ImageId, Model , value of 'k' separated by space")
    input_list = image_input.split(' ')
    imageSimilarityValues = SimilarityFinder.SimilarityMatrixCreator.createSimilarityMatrix(imageData, input_list[1],
                                                                                            input_list[0], "imageId")

    imagesTopKValues = TaskHelpers.RetriveKOutput.getTopKValues(imageSimilarityValues, input_list[2])

    for key, value in imagesTopKValues.items():
        print("ImageId - {0}, similarity value - {1}".format(key, value))

    TaskHelpers.GetTop3Contributors.findTopContributors(imagesTopKValues, imageData, input_list[0], input_list[1],
                                                            'imageId')
