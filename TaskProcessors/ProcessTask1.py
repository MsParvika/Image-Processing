import SimilarityFinder.SimilarityMatrixCreator
import TaskHelpers.GetTop3Contributors
import TaskHelpers.RetriveKOutput


def processTask1(db):
    userData = db.userData

    user_input = input("Enter UserId, Model , value of 'k' separated by space")
    input_list = user_input.split(' ')

    userSimilarityMatrix = SimilarityFinder.SimilarityMatrixCreator.createSimilarityMatrix(userData, input_list[1],
                                                                                           input_list[0], "userId")
    userTopKValues = TaskHelpers.RetriveKOutput.getTopKValues(userSimilarityMatrix,
                                                              input_list[2])
    for key, value in userTopKValues.items():
        print("userId - {0}, similarity value - {1}".format(key, value))
    TaskHelpers.GetTop3Contributors.findTopContributors(userTopKValues, userData, input_list[0],
                                                        input_list[1], 'userId')
